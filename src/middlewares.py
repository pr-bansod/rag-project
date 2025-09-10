import logging

logger = logging.getLogger(__name__)


#  Simplified middleware for learning purposes
# Production-grade middleware will be added in later weeks

def log_request(method: str, path: str) -> None:
    """Simple request logging """
    logger.info(f"{method} {path}")


def log_error(error: str, method: str, path: str) -> None:
    """Simple error logging"""
    logger.error(f"Error in {method} {path}: {error}")
