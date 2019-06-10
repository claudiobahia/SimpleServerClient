import psutil

user_lists = []
name_lists = []
pid_lists = []
stat_lists = []

for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name()
        name_lists.append(processName)
        processID = proc.pid
        pid_lists.append(processID)
        processUser = proc.username()
        user_lists.append(processUser)
        processStat = proc.status()
        stat_lists.append(processStat)


    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

def user_list():
    return user_lists

def name_list():
    return name_lists

def pid_list():
    return pid_lists

def stat_list():
    return stat_lists
