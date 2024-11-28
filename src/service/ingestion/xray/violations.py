from service.models.xray_violations.models import Violations, Model
from service.lib.xray_api import get_violations
import datetime
from database.database import database, sqlengine_type
from database.models.xray_violations.models import (
    violations_table,
    violations_hwm_table,
)
from sqlalchemy import select, func, delete, insert, update, and_ as _and
from service.lib.utils import json_object_converter
from datetime import timedelta


def get_all_violations():

    query = select(violations_hwm_table.c.created_hwm)
    result = database.execute_sync(query)
    hwm = result.fetchone()
    hwms: datetime.datetime = (
        hwm[0] if hwm else datetime.datetime(1999, 1, 16, 0, 0)
    )
    hwms = hwms.replace(tzinfo=datetime.timezone.utc).isoformat()
    offset = 1
    filter = {
        "pagination": {
            "limit": 1000,
            "offset": offset,
        },
        "created_from": hwms,
        "filters": {"created_from": hwms},
    }

    filter = json_object_converter(filter)
    filter["filters"]["created_from"] = filter["created_from"]
    filter.pop("created_from")

    print("FILTER", filter)
    while True:

        violations = get_violations(filter)
        all_violations = Model(**violations)

        if len(all_violations.violations) == 0:
            break

        for _violation in all_violations.violations:
            violation_record = Violations(**_violation)
            violation_record.created = datetime.datetime.fromisoformat(
                violation_record.created
            )
            hwms = violation_record.created
            database.sm_add(violation_record)

        database.execute_sync(delete(violations_hwm_table))

        database.execute_sync(
            insert(violations_hwm_table).values(
                created_hwm=hwms + timedelta(seconds=1)
            )
        )
        offset += 1
        filter["pagination"]["offset"] = offset
        filter = json_object_converter(filter)

        print(f"Offset: {offset}")
