import platform
import os

print(f"System: {platform.system()}")
print(f"Hostname: {os.uname()[1]}")
