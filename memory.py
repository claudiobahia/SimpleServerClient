import psutil

def size():
    return round(psutil.virtual_memory().total/1024**3,2)

def percentage():
    return psutil.virtual_memory().percent

def free():
    return round(psutil.virtual_memory().free/1024**3,2)

def used():
    return round(psutil.virtual_memory().used/1024**3,2)

