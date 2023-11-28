import platform
import os

print(f"Retrieving System Information...\n")
print(f"System: {platform.system()}")
print(f"Hostname: {os.uname()[1]}")
