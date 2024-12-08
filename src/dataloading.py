from service.ingestion.artifactory.repos import get_all_artifactory_repos
from service.ingestion.artifactory.licenses import update_license_inventory
from service.ingestion.xray.violations import get_all_violations
from service.ingestion.xray.watches import get_all_watches
from service.ingestion.xray.policies import get_all_policies
from rq_scheduler import Scheduler
from config.app_config import get_settings

import time
from redis import Redis
from rq import Queue
from datetime import datetime, timezone, timedelta
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.CRITICAL)

q = Queue(
    connection=Redis(host="redis", port=6379, db=1), default_timeout=10000
)
scheduler = Scheduler(queue=q, connection=q.connection)

app_settings = get_settings()


scheduler.schedule(
    scheduled_time=datetime.now(),
    func=get_all_artifactory_repos,
    interval=60 * app_settings.JFROG_UPDATE_LONG_INTERVAL,
    timeout=60 * 10,
    ttl=6300,
    repeat=None,
)

scheduler.schedule(
    scheduled_time=datetime.now(),
    func=get_all_watches,
    interval=60 * app_settings.JFROG_UPDATE_LONG_INTERVAL,
    timeout=60 * 10,
    ttl=6300,
    repeat=None,
)

scheduler.schedule(
    scheduled_time=datetime.now(),
    func=get_all_policies,
    interval=60 * app_settings.JFROG_UPDATE_LONG_INTERVAL,
    timeout=60 * 10,
    ttl=6300,
    repeat=None,
)

scheduler.schedule(
    scheduled_time=datetime.now(),
    func=get_all_violations,
    interval=60 * app_settings.JFROG_UPDATE_SHORT_INTERVAL,
    ttl=6300,
    timeout=60 * 10,
    repeat=None,
)


scheduler.schedule(
    scheduled_time=datetime.now(),
    func=update_license_inventory,
    interval=60 * 60 * 24,
    ttl=6300,
    timeout=60 * 10,
    repeat=None,
)

while True:
    time.sleep(1)
