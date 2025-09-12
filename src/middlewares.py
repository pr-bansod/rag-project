import logging

logger = logging.getLogger(__name__)


# Phase 1: Simplified middleware for learning purposes
# Production-grade middleware will be added in later phases

def log_request(method: str, path: str) -> None:
    """Simple request logging for Phase 1."""
    logger.info(f"{method} {path}")


def log_error(error: str, method: str, path: str) -> None:
    """Simple error logging for Phase 1."""
    logger.error(f"Error in {method} {path}: {error}")
