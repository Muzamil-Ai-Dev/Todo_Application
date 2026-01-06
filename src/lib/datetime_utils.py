from datetime import datetime


def format_datetime_iso(dt: datetime) -> str:
    """
    Format a datetime object to ISO 8601 format (YYYY-MM-DD HH:MM:SS).

    Args:
        dt: The datetime object to format

    Returns:
        Formatted datetime string in ISO 8601 format
    """
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def format_datetime_display(dt: datetime) -> str:
    """
    Format a datetime object for display purposes (YYYY-MM-DD HH:MM).

    Args:
        dt: The datetime object to format

    Returns:
        Formatted datetime string for display
    """
    return dt.strftime('%Y-%m-%d %H:%M')


def parse_datetime_iso(dt_str: str) -> datetime:
    """
    Parse a datetime string in ISO 8601 format (YYYY-MM-DD HH:MM:SS) to a datetime object.

    Args:
        dt_str: The datetime string in ISO 8601 format

    Returns:
        Parsed datetime object
    """
    return datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')


def get_current_datetime() -> datetime:
    """
    Get the current datetime.

    Returns:
        Current datetime object
    """
    return datetime.now()


def get_current_datetime_iso() -> str:
    """
    Get the current datetime formatted as ISO 8601 string.

    Returns:
        Current datetime as ISO 8601 formatted string
    """
    return format_datetime_iso(get_current_datetime())