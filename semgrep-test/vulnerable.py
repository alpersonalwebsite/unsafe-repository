# Example file for semgrep
import os

# Hardcoded password (should be flagged)
password = "supersecret"

# Insecure subprocess usage (should be flagged)
os.system('ls -l')
