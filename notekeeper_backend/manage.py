#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notekeeper_backend.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # ✅ Improved Error Message
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and accessible.\n"
            "🔹 Run: pip install django\n"
            "🔹 Ensure you activated your virtual environment: venv\\Scripts\\activate (Windows) OR source venv/bin/activate (Mac/Linux)"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
