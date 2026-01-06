"""
Utility functions for Rich formatting in the Todo Application CLI.
Provides common formatting functions for consistent professional appearance.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt
from rich.style import Style


class RichFormatter:
    """
    A utility class for Rich formatting functions used throughout the application.
    """

    def __init__(self):
        self.console = Console()

    def create_menu_panel(self, content: str) -> Panel:
        """
        Create a professional menu panel with blue/gray theme.

        Args:
            content: The content to display in the panel

        Returns:
            Panel: A Rich panel with professional styling
        """
        return Panel(
            content,
            title="Todo Application",
            title_align="center",
            border_style="blue",
            padding=(1, 2)
        )

    def create_task_table(self) -> Table:
        """
        Create a professional task table with blue/gray theme.

        Returns:
            Table: A Rich table with professional styling
        """
        table = Table(
            title="Task List",
            title_style="bold blue",
            show_header=True,
            header_style="bold blue",
            border_style="blue",
            row_styles=["none", "dim"]
        )
        table.add_column("ID", style="cyan", width=4)
        table.add_column("Title", style="white", min_width=15)
        table.add_column("Description", style="white", min_width=20)
        table.add_column("Status", style="green", width=10)
        table.add_column("Created", style="magenta", width=18)
        table.add_column("Updated", style="magenta", width=18)
        return table

    def format_status(self, completed: bool) -> Text:
        """
        Format task status with appropriate symbols and colors.

        Args:
            completed: Whether the task is completed

        Returns:
            Text: Formatted status text with symbols and colors
        """
        if completed:
            return Text("[✓] Completed", style="green")
        else:
            return Text("[ ] Pending", style="yellow")

    def display_error(self, message: str):
        """
        Display an error message with professional styling.

        Args:
            message: The error message to display
        """
        error_text = Text(f"[ERROR] {message}", style="bold red")
        self.console.print(error_text)

    def display_success(self, message: str):
        """
        Display a success message with professional styling.

        Args:
            message: The success message to display
        """
        success_text = Text(f"[SUCCESS] {message}", style="bold green")
        self.console.print(success_text)

    def display_warning(self, message: str):
        """
        Display a warning message with professional styling.

        Args:
            message: The warning message to display
        """
        warning_text = Text(f"[WARNING] {message}", style="bold yellow")
        self.console.print(warning_text)

    def display_info(self, message: str):
        """
        Display an info message with professional styling.

        Args:
            message: The info message to display
        """
        info_text = Text(message, style="blue")
        self.console.print(info_text)


# Global formatter instance
formatter = RichFormatter()


class BackwardCompatibilityLayer:
    """
    A compatibility layer to ensure existing functionality is preserved
    while adding Rich formatting enhancements.
    """

    def __init__(self):
        self.console = Console()

    def print(self, *args, **kwargs):
        """
        Compatibility wrapper for print() function.
        """
        text = " ".join(str(arg) for arg in args)
        self.console.print(text, **kwargs)

    def display_menu_original(self):
        """
        Display the original menu format for compatibility testing.
        """
        menu_content = (
            "==== Todo Application ====\n"
            "1. Add Task\n"
            "2. View Tasks\n"
            "3. Update Task\n"
            "4. Delete Task\n"
            "5. Mark Task as Complete\n"
            "6. Mark Task as Incomplete\n"
            "7. Exit\n"
            "\n"
            "Choose an option (1-7):"
        )
        self.console.print(menu_content)

    def display_error_original(self, message: str):
        """
        Display error in original format for compatibility.
        """
        self.console.print(f"Error: {message}")

    def display_success_original(self, message: str):
        """
        Display success in original format for compatibility.
        """
        self.console.print(message)


# Global compatibility instance
compatibility = BackwardCompatibilityLayer()