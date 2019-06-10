import psutil,platform

def info():
    return psutil.net_io_counters(pernic=False)
def IpAddress(type,ip):
    return psutil.net_if_addrs()[type][ip]
def pc_name():
    return platform.uname().node
