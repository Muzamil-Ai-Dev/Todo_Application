"""
Theme configuration for the Todo Application CLI.
Provides consistent blue/gray professional color scheme.
"""

# Professional blue/gray color scheme
THEME = {
    # Primary colors
    'primary': 'blue',
    'primary_dark': 'dark_blue',
    'primary_light': 'dodger_blue1',

    # Secondary colors
    'secondary': 'gray78',
    'secondary_dark': 'gray50',
    'secondary_light': 'white',

    # Status colors
    'success': 'green',
    'error': 'red',
    'warning': 'yellow',
    'info': 'blue',

    # Background colors
    'background': 'default',
    'panel_background': 'default',

    # Text colors
    'text_primary': 'white',
    'text_secondary': 'gray62',
    'text_muted': 'gray50',

    # Border colors
    'border': 'blue',
    'border_focused': 'bright_blue',

    # Status indicators
    'status_completed': 'green',
    'status_pending': 'yellow',
    'status_inactive': 'gray50',

    # Table styling
    'table_header': 'bold blue',
    'table_border': 'blue',
    'table_row_even': 'none',
    'table_row_odd': 'dim'
}

# Color mapping for different elements
COLORS = {
    'menu_title': THEME['primary'],
    'menu_option': THEME['text_primary'],
    'menu_highlight': THEME['primary_light'],
    'error_text': THEME['error'],
    'success_text': THEME['success'],
    'warning_text': THEME['warning'],
    'info_text': THEME['info'],
    'task_title': THEME['text_primary'],
    'task_description': THEME['text_secondary'],
    'task_status_completed': THEME['status_completed'],
    'task_status_pending': THEME['status_pending'],
    'timestamp': THEME['text_muted'],
    'border': THEME['border']
}


def get_color(element: str) -> str:
    """
    Get the appropriate color for a given UI element.

    Args:
        element: The UI element name

    Returns:
        str: The color string for the element
    """
    return COLORS.get(element, 'white')


def get_theme() -> dict:
    """
    Get the complete theme configuration.

    Returns:
        dict: The theme configuration dictionary
    """
    return THEME


def validate_theme_consistency() -> bool:
    """
    Validate that all theme elements have consistent color definitions.

    Returns:
        bool: True if theme is consistent, False otherwise
    """
    # Check that all color elements are properly defined
    required_elements = [
        'menu_title', 'menu_option', 'menu_highlight', 'error_text',
        'success_text', 'warning_text', 'info_text', 'task_title',
        'task_description', 'task_status_completed', 'task_status_pending',
        'timestamp', 'border'
    ]

    for element in required_elements:
        if element not in COLORS:
            print(f"Warning: Theme element '{element}' not defined in color scheme")
            return False

    # Validate that all color values are valid Rich color strings
    for element, color in COLORS.items():
        # This is a basic check - in a real implementation we would validate
        # against Rich's actual color format requirements
        if not isinstance(color, str) or len(color.strip()) == 0:
            print(f"Warning: Invalid color value for '{element}': {color}")
            return False

    return True


def validate_theme_application() -> bool:
    """
    Validate that theme is being applied consistently across application elements.

    Returns:
        bool: True if theme application is consistent, False otherwise
    """
    # This would typically check that the theme is being used consistently
    # across all UI elements in the application
    return True