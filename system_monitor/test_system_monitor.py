from system_monitor import get_cpu_usage, get_memory_usage

def test_cpu_usage_range():
    cpu = get_cpu_usage()
    assert 0 <= cpu <= 100

def test_memory_usage_format():
    used, total, percent = get_memory_usage()
    assert percent <= 100
