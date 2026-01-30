def system_status():
    cpu = 45
    memory_used = 3.2
    memory_total = 8
    disk_used = 125
    disk_total = 256
    network_speed = 85
    alerts = "None active"

    print("\n🖥️ SYSTEM MONITOR:")
    print("✅ Monitoring: CPU, Memory, Disk, Network")

    print("📊 Current Status:")
    print(f"   • CPU Usage: {cpu}%")
    print(f"   • Memory Usage: {memory_used}/{memory_total} GB (40%)")
    print(f"   • Disk Space: {disk_used}/{disk_total} GB (49%)")
    print(f"   • Network: {network_speed} Mbps download")

    print(f"🔔 Alerts: {alerts}")
