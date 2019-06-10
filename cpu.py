import psutil, cpuinfo

def freq():
    return psutil.cpu_freq()
def cores_fisicos():
    return psutil.cpu_count(logical=False)
def cores():
    return psutil.cpu_count()
def name():
    return cpuinfo.get_cpu_info()['brand']
def idle_process():
    return psutil.cpu_times_percent()
def process():
    return psutil.cpu_percent()
def process_in_use_percentage_each_core():
    return psutil.cpu_percent(percpu=True)
def cpu_archteture():
    return cpuinfo.get_cpu_info()["arch"]

