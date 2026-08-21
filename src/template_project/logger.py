"""
Logging configuration for template_project.

This module provides a centrally configured logger for the project,
with support for file and console output at different verbosity levels.
"""

import datetime
import logging
import sys
from pathlib import Path
from typing import Any

# Global logger instance (will be configured by setup_logger)
log = logging.getLogger("template_project")
log.setLevel(logging.DEBUG)  # capture everything; handlers filter later

# Global logging flag
# Set to True to enable logging, False to disable
LOGGING_ENABLED = True


def enable_logging() -> None:
    """Enable logging globally."""
    global LOGGING_ENABLED
    LOGGING_ENABLED = True


def disable_logging() -> None:
    """Disable logging globally."""
    global LOGGING_ENABLED
    LOGGING_ENABLED = False


def log_info(message: str, *args: Any) -> None:
    """Log an info message, if logging is enabled."""
    if LOGGING_ENABLED:
        log.info(message, *args, stacklevel=2)


def log_warning(message: str, *args: Any) -> None:
    """Log a warning message, if logging is enabled."""
    if LOGGING_ENABLED:
        log.warning(message, *args, stacklevel=2)


def log_error(message: str, *args: Any) -> None:
    """Log an error message, if logging is enabled."""
    if LOGGING_ENABLED:
        log.error(message, *args, stacklevel=2)


def log_debug(message: str, *args: Any) -> None:
    """Log a debug message, if logging is enabled."""
    if LOGGING_ENABLED:
        log.debug(message, *args, stacklevel=2)


def log_to_stdout(level: int = logging.INFO) -> logging.StreamHandler:
    """Send the package logger's messages to stdout.

    Handy in notebooks and scripts where you want to *see* library log output
    without configuring a file logger. Idempotent — calling it more than once
    does not add duplicate stdout handlers.

    Parameters
    ----------
    level : int
        Minimum level to show on stdout (default ``logging.INFO``).

    Returns
    -------
    logging.StreamHandler
        The stdout handler (new, or the existing one if already attached).

    """
    for h in log.handlers:
        if (
            isinstance(h, logging.StreamHandler)
            and getattr(h, "stream", None) is sys.stdout
        ):
            h.setLevel(level)
            return h
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))
    log.addHandler(handler)
    return handler


def setup_logger(array_name: str, output_dir: str = "logs") -> None:
    """Configure the global logger to output to a file for the given array.

    Parameters
    ----------
    array_name : str
        Name of the observing array (e.g., 'move', 'rapid', etc.).
    output_dir : str
        Directory to save log files. Resolved relative to the current working
        directory.

    """
    if not LOGGING_ENABLED:
        return
    # Resolve output directory relative to the working directory (not the installed
    # package location), so logs never land inside site-packages / the src/ tree.
    output_path = Path.cwd() / output_dir
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%dT%H")
    log_filename = f"{array_name.upper()}_{timestamp}_read.log"
    log_path = output_path / log_filename

    # A file handler for this exact path is already attached — nothing to do.
    if any(
        isinstance(h, logging.FileHandler) and h.baseFilename == str(log_path)
        for h in log.handlers
    ):
        return

    # Remove stale file handlers from previous runs, but preserve any stream/stdout
    # handlers the caller attached (e.g. via log_to_stdout()) — clearing all handlers
    # would silently drop console output the user explicitly enabled.
    for h in list(log.handlers):
        if isinstance(h, logging.FileHandler):
            log.removeHandler(h)
            h.close()

    file_handler = logging.FileHandler(log_path, encoding="utf-8", mode="w")
    file_handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s %(levelname)-8s %(funcName)s %(message)s",
            datefmt="%Y%m%dT%H%M%S",
        )
    )
    log.addHandler(file_handler)
    log.info("Logger initialized for array: %s, writing to %s", array_name, log_path)
