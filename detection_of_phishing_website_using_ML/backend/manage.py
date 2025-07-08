#!/usr/bin/env python
import os
import sys
import sys
from pathlib import Path

# Add this line to help Python find your apps
sys.path.append(str(Path(__file__).parent))

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phishing_detector.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Is it installed and available on your PYTHONPATH environment variable? "
            "Did you forget to activate your virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
