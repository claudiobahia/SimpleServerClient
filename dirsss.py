import os, psutil

def info():
    return psutil.disk_partitions()
listaPartMount = []
listaPartFS = []
for i in range(len(info())):
    listaPartMount.append(info()[i].mountpoint)
    listaPartFS.append(info()[i].fstype)

partition = listaPartMount[0]
def folders_name():
    os.chdir(partition)
    for paths,dirs,files in os.walk(partition):
        return dirs
        break
