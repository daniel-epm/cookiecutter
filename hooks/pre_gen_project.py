
import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

MESSAGE_COLOR = "\x1b[32m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Initializing a new project")
print(f"Creating project at {os.getcwd()}{RESET_ALL}")