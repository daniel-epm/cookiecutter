import subprocess

from hooks.pre_gen_project import RESET_ALL

MESSAGE_COLOR = "\x1b[33m"
RESET_ALL = "\x1b[0m"

print("Initializing a Git repository {RESET_ALL}")

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Initial commit"])

print(f"{MESSAGE_COLOR} ¡Project generated succesfully! {RESET_ALL}")