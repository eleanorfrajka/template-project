import time
from pathlib import Path
from template_project import logger


def test_setup_logger_creates_file_and_logs():
    logger.enable_logging()

    logger.setup_logger(array_name="testlog")
    logger.log.info("This is an info message")
    for handler in logger.log.handlers:
        handler.flush()

    time.sleep(0.1)
    log_file = next(Path("logs").glob("TESTLOG_*_read.log"), None)
    assert log_file is not None, "No log file matching pattern TESTLOG_*_read.log found"

    with open(log_file) as f:
        contents = f.read()
        print(contents)
        assert "This is an info message" in contents

    log_file.unlink()


def test_enable_and_disable_logging():
    logger.enable_logging()
    logger.disable_logging()


def test_log_warning_creates_entry():
    logger.enable_logging()

    logger.setup_logger(array_name="testwarn")
    logger.log_warning("This is a warning!")
    for handler in logger.log.handlers:
        handler.flush()

    time.sleep(0.1)
    log_file = next(Path("logs").glob("TESTWARN_*_read.log"), None)
    assert (
        log_file is not None
    ), "No log file matching pattern TESTWARN_*_read.log found"

    print(f"Contents of the 'logs' directory: {list(Path('logs').iterdir())}")

    with open(log_file) as f:
        contents = f.read()
        assert "This is a warning!" in contents

    log_file.unlink()
