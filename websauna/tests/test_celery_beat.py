"""See that cron'd tasks run."""

import subprocess
import time
import os

from pyramid.testing import DummyRequest

from websauna.system.core.redis import get_redis
from websauna.tests import scheduledtasks


def test_run_scheduled(init):
    """Scheduled tasks run properly on the celery worker + celery beat process."""

    ini_file = os.path.join(os.path.dirname(__file__), "scheduler-test.ini")

    cmdline = ["ws-celery", "worker", "-A", "websauna.system.task.celery.celery_app", "--ini", ini_file]

    if False:
        # You can start manually ws-celery worker -A websauna.system.task.celery.celery_app --ini websauna/tests/scheduler-test.ini

        print("Running ", " ".join(cmdline))
        worker = subprocess.Popen(cmdline, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(2.0)

        worker.poll()
        if worker.returncode is not None:
            raise AssertionError("Scheduler process did not start up: {}".format(" ".join(cmdline)))

    # You can run manually ws-celery beat -A websauna.system.task.celery.celery_app --ini websauna/tests/scheduler-test.ini

    cmdline = ["ws-celery", "beat", "-A", "websauna.system.task.celery.celery_app", "--ini", ini_file]
    print(" ".join(cmdline))
    beat = subprocess.Popen(cmdline, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    time.sleep(1.0)
    beat.poll()
    if beat.returncode is not None:
        worker.terminate()
        AssertionError("Beat process did not start up")

    try:
        # Reset test database
        redis = get_redis(init.config.registry)
        redis.delete("foo", "bar")

        # scheduledtasks.ticker should beat every second and reset values in Redis
        # sets foo
        time.sleep(2)

        redis = get_redis(init.config.registry)
        foo = redis.get("foo")

        assert beat.returncode is None
        assert worker.returncode is None
        assert foo == b"foo"  # Set back by its original value by 1 second beat

    finally:
        try:
            worker.terminate()
        except ProcessLookupError:
            pass

        try:
            beat.terminate()
        except ProcessLookupError:
            pass