def check_alerts(cpu_usage):
    if cpu_usage > 80:
        print("High CPU usage alert")