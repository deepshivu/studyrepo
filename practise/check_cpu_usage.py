import psutil

cpu_usage = psutil.cpu_percent(interval=1)
if cpu_usage > 20:
    print(f"Warning! High CPU usage detected: {cpu_usage}%")