import psutil

def info():
    return psutil.disk_partitions()

listaPartMount = []
listaPartFS = []
for i in range(len(info())):
    listaPartMount.append(info()[i].mountpoint)
    listaPartFS.append(info()[i].fstype)

partition = listaPartMount[0]


def used():
    return round(psutil.disk_usage(partition).used/1024**3,2)
def percent():
    return psutil.disk_usage(partition).percent
def total():
    return round(psutil.disk_usage(partition).total/1024**3,2)
def free():
    return round(psutil.disk_usage(partition).free/1024**3,2)