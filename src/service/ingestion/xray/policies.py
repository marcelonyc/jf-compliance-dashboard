from service.models.policies.models import (
    Policies,
    Rule,
    Criteria,
    Exposures,
    OpRiskCustom,
    CvssRange,
    Actions,
)

from service.lib.xray_api import get_policies
import datetime
from database.database import database, sqlengine_type
from sqlalchemy import select, func, delete, insert, update, and_ as _and
from service.lib.utils import json_object_converter
from sqlalchemy.exc import IntegrityError


def get_all_policies():

    policies = get_policies()

    for _policy in policies:
        policy_record = Policies(**_policy)

        try:
            database.sm_add(policy_record)
        except IntegrityError as e:
            database.execute_sync(
                update(Policies)
                .where(Policies.name == policy_record.name)
                .values(
                    type=policy_record.type,
                    author=policy_record.author,
                    rules=policy_record.rules,
                    created=policy_record.created,
                    modified=policy_record.modified,
                    description=policy_record.description,
                    project_key=policy_record.project_key,
                )
            )
