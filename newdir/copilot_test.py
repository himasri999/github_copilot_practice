import os
import platform
import subprocess

def get_system_uptime():
    system = platform.system()
    if system == "Windows":
        # Windows doesn't have a direct uptime command, use 'net stats srv'
        try:
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    print("System Uptime Start:", line)
                    break
        except Exception as e:
            print(f"Error obtaining uptime on Windows: {e}")
    elif system == "Linux" or system == "Darwin":
        try:
            # Try using the 'uptime' command
            output = subprocess.check_output("uptime -p", shell=True, text=True)
            print("System Uptime:", output.strip())
        except Exception:
            # Fallback to /proc/uptime on Linux
            try:
                with open('/proc/uptime', 'r') as f:
                    uptime_seconds = float(f.readline().split()[0])
                    hours = int(uptime_seconds // 3600)
                    minutes = int((uptime_seconds % 3600) // 60)
                    print(f"System Uptime: {hours} hours, {minutes} minutes")
            except Exception as e:
                print(f"Error obtaining uptime: {e}")
    else:
        print(f"Unsupported OS: {system}")

if __name__ == "__main__":
    get_system_uptime()
