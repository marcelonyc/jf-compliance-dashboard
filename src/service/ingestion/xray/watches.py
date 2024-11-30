from service.models.watches.models import (
    Watches,
    GeneralData,
    ProjectResources,
    AssignedPolicy,
    TicketGeneration,
    WatchesPreProcess,
)
from service.lib.xray_api import get_watches
import datetime
from database.database import database, sqlengine_type
from sqlalchemy import select, func, delete, insert, update, and_ as _and
from service.lib.utils import json_object_converter
from sqlalchemy.exc import IntegrityError


def get_all_watches():

    watches = get_watches()

    for _watch in watches:
        watch_pre_process = WatchesPreProcess(**_watch)
        watch_record = Watches(
            id=watch_pre_process.general_data.id,
            name=watch_pre_process.general_data.name,
            active=watch_pre_process.general_data.active,
            project_key=watch_pre_process.general_data.project_key,
            description=watch_pre_process.general_data.description,
            project_resources=watch_pre_process.project_resources.model_dump(),
            assigned_policies=watch_pre_process.assigned_policies,
            ticket_generation=watch_pre_process.ticket_generation.model_dump(),
            watch_recipients=watch_pre_process.watch_recipients,
            create_ticket_enabled=watch_pre_process.create_ticket_enabled,
            ticket_profile=watch_pre_process.ticket_profile,
        )
        try:
            database.sm_add(watch_record)
        except IntegrityError as e:
            database.execute_sync(
                update(Watches)
                .where(Watches.name == watch_record.name)
                .values(
                    active=watch_record.active,
                    project_key=watch_record.project_key,
                    description=watch_record.description,
                    project_resources=watch_record.project_resources,
                    assigned_policies=watch_record.assigned_policies,
                    ticket_generation=watch_record.ticket_generation,
                    watch_recipients=watch_record.watch_recipients,
                    create_ticket_enabled=watch_record.create_ticket_enabled,
                    ticket_profile=watch_record.ticket_profile,
                )
            )
