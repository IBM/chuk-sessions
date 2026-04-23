from datetime import datetime, timezone


def utc_now_iso() -> str:
    """Return the current UTC time as an ISO 8601 string with a Z suffix."""
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


__all__ = ["utc_now_iso"]
