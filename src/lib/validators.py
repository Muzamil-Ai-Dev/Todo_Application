from typing import Optional
import re


def validate_task_title(title: str) -> tuple[bool, Optional[str]]:
    """
    Validate the task title according to the requirements.

    Args:
        title: The title to validate

    Returns:
        A tuple containing:
        - Boolean indicating if the title is valid
        - Error message if invalid, None if valid
    """
    # Check if title is empty
    if not title or not title.strip():
        return False, "Task title cannot be empty"

    # Check if title length is within the allowed range (1-200 characters)
    if len(title) < 1 or len(title) > 200:
        return False, f"Task title must be between 1 and 200 characters, got {len(title)}"

    return True, None


def validate_task_id(task_id: str, existing_task_ids: list) -> tuple[bool, Optional[str]]:
    """
    Validate the task ID.

    Args:
        task_id: The task ID to validate (as string, needs to be converted to int)
        existing_task_ids: List of existing task IDs to check against

    Returns:
        A tuple containing:
        - Boolean indicating if the task ID is valid
        - Error message if invalid, None if valid
    """
    try:
        # Try to convert to integer
        task_id_int = int(task_id)
    except ValueError:
        return False, "Task ID must be a valid integer"

    # Check if the task ID is positive (valid task IDs should be positive)
    if task_id_int <= 0:
        return False, "Task ID must be a valid integer"

    # Check if the task ID exists in the current task list
    if task_id_int not in existing_task_ids:
        return False, f"Task with ID {task_id_int} does not exist"

    return True, None


def validate_menu_choice(choice: str) -> tuple[bool, Optional[str]]:
    """
    Validate the menu choice.

    Args:
        choice: The menu choice to validate

    Returns:
        A tuple containing:
        - Boolean indicating if the choice is valid
        - Error message if invalid, None if valid
    """
    try:
        choice_int = int(choice)
    except ValueError:
        return False, "Menu choice must be a valid integer"

    # Check if choice is within the valid range (1-7)
    if choice_int < 1 or choice_int > 7:
        return False, f"Menu choice must be between 1 and 7, got {choice_int}"

    return True, None


def validate_confirmation_input(confirmation: str) -> tuple[bool, Optional[str]]:
    """
    Validate the confirmation input ('y'/'n').

    Args:
        confirmation: The confirmation input to validate

    Returns:
        A tuple containing:
        - Boolean indicating if the confirmation is valid
        - Error message if invalid, None if valid
    """
    confirmation_lower = confirmation.lower().strip()

    if confirmation_lower not in ['y', 'n']:
        return False, f"Confirmation must be 'y' or 'n', got '{confirmation}'"

    return True, None


def validate_task_description(description: str) -> tuple[bool, Optional[str]]:
    """
    Validate the task description.

    Args:
        description: The description to validate

    Returns:
        A tuple containing:
        - Boolean indicating if the description is valid
        - Error message if invalid, None if valid
    """
    # For now, we just check if it's too long
    # The requirements don't specify a maximum length for description
    # but we'll set a reasonable limit to prevent abuse
    if len(description) > 1000:  # Arbitrary limit, can be adjusted
        return False, "Task description is too long (max 1000 characters)"

    return True, None


def is_valid_datetime_format(dt_str: str) -> bool:
    """
    Check if the datetime string matches the expected ISO 8601 format YYYY-MM-DD HH:MM:SS
    and has valid date/time values.

    Args:
        dt_str: The datetime string to validate

    Returns:
        Boolean indicating if the format and values are valid
    """
    import datetime

    # First check if it matches the pattern YYYY-MM-DD HH:MM:SS
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
    if not re.match(pattern, dt_str):
        return False

    # Then try to parse it to ensure the values are valid
    try:
        parsed = datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False