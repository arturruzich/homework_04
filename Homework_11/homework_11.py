import logging
import pytest

import homework_10
from homework_10 import log_event

def log_file(tmpdir):
    return tmpdir.join("test_login_system.log")

def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
    )
    return log_file

def test_log_event_success(setup_logging):
    log_event("user1", "success")

    with open(setup_logging, "r") as log:
        log_contents = log.read()
        assert "INFO" in log_contents
        assert "Login event - Username: user1, Status: success" in log_contents

def test_log_event_expired(setup_logging):
    log_event("user2", "expired")

    with open(setup_logging, "r") as log:
        log_contents = log.read()
        assert "WARNING" in log_contents
        assert "Login event - Username: user2, Status: expired" in log_contents

def test_log_event_failed(setup_logging):
    log_event("user3", "failed")

    with open(setup_logging, "r") as log:
        log_contents = log.read()
        assert "ERROR" in log_contents
        assert "Login event - Username: user3, Status: failed" in log_contents