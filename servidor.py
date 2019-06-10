import cpu, disk, memory, ip, pid, dirsss
import socket, pickle

import pygame


IP_SERVER = "127.0.0.1"
PORT_SERVER = 9991
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pygame.init()
telax = 1200
telay = 600
tela = pygame.display.set_mode((telax, telay))
intermediate = pygame.surface.Surface((telax, telay * (len(pid.pid_list()) / 16) - 1200))
pygame.display.set_caption('Projeto de Bloco -- Servidor')
clock = pygame.time.Clock()

boxImg = pygame.image.load('box.png')
boxImg = pygame.transform.scale(boxImg, (175, 75))

# mudar entre toolbar
changerInfo = 1
changerBarx = 0

# pid part
scroll_y_pid = 0

cpu = cpu
memory = memory
disk = disk
ip = ip
pid = pid
dirsss = dirsss

pattern_font = pygame.font.Font('freesansbold.ttf', 20)




def send_infos_to_client():
    lista_infos_cpu = [cpu_name, cpu_arch, speed_cpu, cores_logical, cores_fisics, used, idle, per_core, cpuprocess,
                       cpuidleprocess]

    lista_infos_disk = [dir_name, total_size, used_size, free_size, percentage_in_use, diskprocess]

    lista_infos_memory = [size_memory, free_memory, used_memory, percentage_memory, memoryprocess]

    lista_infos_ip = [name_disk, MAC, IPV4, IPV6, sent_bytes_, received_bytes_, sent_packets_, received_packets_]

    lita_infos_pid = [user_, process_name_, pid_, status_]

    lista_infos_dirs = [nn, folders, portas]

    lista_infos_final = lista_infos_cpu + lista_infos_disk + lista_infos_memory + lista_infos_ip + lita_infos_pid + lista_infos_dirs

    send_socket_pickle_infos = pickle.dumps(lista_infos_final)
    sock.sendto((send_socket_pickle_infos), (IP_SERVER, PORT_SERVER))

# atualizaçãr bar
def InfoBarUsed():
    if changerInfo == 1:  # cpu
        pygame.draw.rect(tela, (50, 50, 50), (10, 250, 100 * 5, 50))
        pygame.draw.rect(tela, (50, 50, 100), (10, 250, (cpuprocess) * 5, 50))
    if changerInfo == 2:  # disk
        pygame.draw.rect(tela, (50, 50, 50), (10, 250, 100 * 5, 100))
        pygame.draw.rect(tela, (50, 50, 100), (10, 250, (diskprocess) * 5, 100))

    if changerInfo == 3:  # memory
        pygame.draw.rect(tela, (50, 50, 50), (10, 220, 100 * 5, 100))
        pygame.draw.rect(tela, (50, 50, 100), (10, 220, (memoryprocess) * 5, 100))


def InfoBarIdle():
    if changerInfo == 1:
        backbar = pygame.draw.rect(tela, (50, 50, 50), (10, 340, 100 * 5, 50))
        frontbar = pygame.draw.rect(tela, (50, 50, 100), (10, 340, cpuidleprocess * 5, 50))

#################### cpu things ####################
def show_cpu_info(arch, name, freq, logicalcore, fisicalcores, processment_in_use, processment_idle, cpuprocess,
                   cpuidleprocess):
    cpu_name = f"Nome da CPU: {name}"
    cpu_arch = f"Arquitetura: {arch}"
    speed_cpu = f"Velocidade: {freq} Ghz"
    cores_logical = f"Cores: {logicalcore}"
    cores_fisics = f"Cores fisicos: {fisicalcores}"
    used = f"Processamento em uso: {round(processment_in_use, 1)} %"
    idle = f"Processamento em espera: {round(processment_idle, 1)} %"

    ################ each core bar ########################
    per_core = cpu.process_in_use_percentage_each_core()

    def creat_lil_bars(per_core, n):  # criar barras para cara núcleo
        pygame.draw.rect(tela, (50, 50, 50), (30 + n, telay - 160, 50, 100 * 1.5))  # backbar
        pygame.draw.rect(tela, (50, 50, 100), (30 + n, telay - 10, 50, -per_core * 1.5))  # frontbar

    widght_var = 0
    for i in per_core:
        creat_lil_bars(i, widght_var)
        widght_var += 70
    ##############    each core bar end ##############

    cpunamesuface = pattern_font.render(cpu_name, False, (255, 255, 255))
    tela.blit(cpunamesuface, (10, 100))

    cpu_arch_suface = pattern_font.render(cpu_arch, False, (255, 255, 255))
    tela.blit(cpu_arch_suface, (10, 70))

    cpuspeedsuface = pattern_font.render(speed_cpu, False, (255, 255, 255))
    tela.blit(cpuspeedsuface, (10, 130))

    cpucoreslogicalsuface = pattern_font.render(cores_logical, False, (255, 255, 255))
    tela.blit(cpucoreslogicalsuface, (10, 160))

    cpucoresficissuface = pattern_font.render(cores_fisics, False, (255, 255, 255))
    tela.blit(cpucoresficissuface, (10, 190))

    cpuusedsuface = pattern_font.render(used, False, (255, 255, 255))
    tela.blit(cpuusedsuface, (10, 220))

    cpuidlesuface = pattern_font.render(idle, False, (255, 255, 255))
    tela.blit(cpuidlesuface, (10, 310))

    cpuidlesuface = pattern_font.render('Gráficos de cada núcleo', False, (255, 255, 255))
    tela.blit(cpuidlesuface, (10, 410))


#################### cpu things end ####################
#################### memory things end ####################

def show_memory_info(size, percentage_in_use, free, used):
    size_memory = f"Tamanho da memória: {size} GB"
    free_memory = f"Memória livre: {free} Gb"
    used_memory = f"Memória usada: {used} Gb"
    percentage_memory = f"Porcentagem em uso: {percentage_in_use}%"

    memory_size_suface = pattern_font.render(size_memory, False, (255, 255, 255))
    tela.blit(memory_size_suface, (10, 100))

    memory_free_suface = pattern_font.render(free_memory, False, (255, 255, 255))
    tela.blit(memory_free_suface, (10, 130))

    memory_used_suface = pattern_font.render(used_memory, False, (255, 255, 255))
    tela.blit(memory_used_suface, (10, 160))

    memory_percentage_surface = pattern_font.render(percentage_memory, False, (255, 255, 255))
    tela.blit(memory_percentage_surface, (10, 190))


#################### memory things end ###################

# #################### disk things #####################

def show_disk_info(dir, total, used, free, percentage, diskprocess):
    dir_name = f"Nome da partição: {dir}"
    total_size = f"Tamanho total: {total} GB"
    used_size = f"Tamanho usado: {used} GB"
    free_size = f"Tamanho livre: {free} GB"
    percentage_in_use = f"Porcentagem em uso: {percentage}%"

    dir_name_surface = pattern_font.render(dir_name, False, (255, 255, 255))
    tela.blit(dir_name_surface, (10, 100))

    total_size_surface = pattern_font.render(total_size, False, (255, 255, 255))
    tela.blit(total_size_surface, (10, 130))

    used_size_surface = pattern_font.render(used_size, False, (255, 255, 255))
    tela.blit(used_size_surface, (10, 160))

    free_size_surface = pattern_font.render(free_size, False, (255, 255, 255))
    tela.blit(free_size_surface, (10, 190))

    percentage_in_use_surface = pattern_font.render(percentage_in_use, False, (255, 255, 255))
    tela.blit(percentage_in_use_surface, (10, 220))


#################### disk things end ####################
#################### ip things #########################
def show_ip_info(name, MACaddress, IPV4address, IPV6address, sent_bytes, received_bytes, sent_packets,
                 received_packets):
    name_disk = f"Nome da máquina: {name}"
    MAC = f"MAC: {MACaddress}"
    IPV4 = f"IPV4: {IPV4address}"
    IPV6 = f"IPV6: {IPV6address}"
    sent_bytes_ = f"Enviado {sent_bytes} bytes ou {round(sent_bytes / 1024 ** 3, 4)} GB"
    received_bytes_ = f"Recebido {received_bytes} bytes ou {round(received_bytes / 1024 ** 3, 4)} GB"
    sent_packets_ = f"Enviados {sent_packets} pacotes"
    received_packets_ = f"Recebidos {received_packets} pacotes"

    name_surface = pattern_font.render(name_disk, False, (255, 255, 255))
    tela.blit(name_surface, (10, 100))

    MAC_surface = pattern_font.render(MAC, False, (255, 255, 255))
    tela.blit(MAC_surface, (10, 130))

    IPV4_surface = pattern_font.render(IPV4, False, (255, 255, 255))
    tela.blit(IPV4_surface, (10, 160))

    IPV6_surface = pattern_font.render(IPV6, False, (255, 255, 255))
    tela.blit(IPV6_surface, (10, 190))

    sent_bytes_surface = pattern_font.render(sent_bytes_, False, (255, 255, 255))
    tela.blit(sent_bytes_surface, (10, 220))

    received_bytes_surface = pattern_font.render(received_bytes_, False, (255, 255, 255))
    tela.blit(received_bytes_surface, (10, 250))

    sent_packets_surface = pattern_font.render(sent_packets_, False, (255, 255, 255))
    tela.blit(sent_packets_surface, (10, 280))

    received_packets_surface = pattern_font.render(received_packets_, False, (255, 255, 255))
    tela.blit(received_packets_surface, (10, 310))


def show_pid_info(user, process_name, pid, status):
    global user_, process_name_, pid_, status_
    user_ = user
    process_name_ = process_name
    pid_ = pid
    status_ = status

    # arrumação
    name_surface = pattern_font.render("Usuário", True, (255, 255, 25))
    intermediate.blit(name_surface, (25, 100))
    user_surface = pattern_font.render("Nome do processo", True, (255, 255, 25))
    intermediate.blit(user_surface, (370, 100))
    pid_surface = pattern_font.render("PID", True, (255, 255, 25))
    intermediate.blit(pid_surface, (625, 100))
    status_surface = pattern_font.render("Status", True, (255, 255, 25))
    intermediate.blit(status_surface, (800, 100))

    # separators
    pygame.draw.rect(intermediate, (50, 50, 100), (300, 80, 2, 10000))
    pygame.draw.rect(intermediate, (50, 50, 100), (600, 80, 2, 10000))
    pygame.draw.rect(intermediate, (50, 50, 100), (700, 80, 2, 10000))

    # listas
    ################# criador de text
    def creat_text_list(folder_name, var_height, var_widght):
        write = pattern_font.render(str(folder_name), False, (255, 255, 255))
        intermediate.blit(write, (10 + var_widght, 130 + var_height))

    ##################
    height_var = 0
    var_widght = 0

    for user in user_:
        creat_text_list(user, height_var, var_widght)
        height_var += 30

    var_widght = 335
    height_var = 0

    for name in process_name_:
        creat_text_list(name, height_var, var_widght)
        height_var += 30

    var_widght = 625
    height_var = 0

    for pid in pid_:
        creat_text_list(pid, height_var, var_widght)
        height_var += 30

    var_widght = 750
    height_var = 0

    for status in status_:
        creat_text_list(status, height_var, var_widght)
        height_var += 30

def globalization():
    global cpu_name, cpu_arch, speed_cpu, cores_logical, cores_fisics, used, idle, per_core, cpuprocess, cpuidleprocess
    cpuprocess = cpu.process()
    cpuidleprocess = cpu.idle_process().idle
    cpu_arch = cpu.cpu_archteture()
    speed_cpu = round(cpu.freq().current / 1000, 1)
    cores_fisics = cpu.cores_fisicos()
    cores_logical = cpu.cores()
    cpu_name = cpu.name()
    idle = cpuidleprocess
    used = cpuprocess
    per_core = cpu.process_in_use_percentage_each_core()

    global dir_name, total_size, used_size, free_size, percentage_in_use, diskprocess
    diskprocess = disk.percent()
    dir_name = (disk.listaPartMount[0][0])
    free_size = disk.free()
    total_size = disk.total()
    used_size = disk.used()
    percentage_in_use = diskprocess

    global size_memory, free_memory, used_memory, percentage_memory, memoryprocess
    memoryprocess = memory.percentage()
    used_memory = memory.used()
    free_memory = memory.free()
    percentage_memory = memoryprocess
    size_memory = memory.size()

    global name_disk, MAC, IPV4, IPV6, sent_bytes_, received_bytes_, sent_packets_, received_packets_
    ipprocess = ip.info()
    # 1 = MAC 2 =IPV4 3 = IPV6
    MAC = ip.IpAddress('Ethernet', 0).address
    IPV4 = ip.IpAddress('Ethernet', 1).address
    IPV6 = ip.IpAddress('Ethernet', 2).address
    name_disk = ip.pc_name()
    sent_bytes_ = ipprocess.bytes_sent
    received_bytes_ = ipprocess.bytes_recv
    sent_packets_ = ipprocess.packets_sent
    received_packets_ = ipprocess.packets_recv

    global user_, process_name_, pid_, status_
    user_ = pid.user_list()
    process_name_ = pid.name_list()
    pid_ = pid.pid_list()
    status_ = pid.stat_list()

    global ip_used
    ip_used = "127.0.0.1"

    global nn, folders
    nn = (f"Partição em uso: {dirsss.partition}")
    folders = dirsss.folders_name()

    global portas
    portas = []

crashed = False

while not crashed:

    globalization()
    send_infos_to_client()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if changerInfo == 5:
                if event.button == 4: scroll_y_pid = min(scroll_y_pid + 15, 0)
                if event.button == 5: scroll_y_pid = max(scroll_y_pid - 15, -(len(pid.pid_list()) * 30 - 450))
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changerInfo -= 1
                changerBarx -= 120
            if event.key == pygame.K_RIGHT:
                changerInfo += 1
                changerBarx += 120
            if changerInfo == 0:
                changerInfo = 6
                changerBarx = 120 * 5
            if changerInfo == 7:
                changerInfo = 1
                changerBarx = 0

    tela.fill((0, 0, 0))

    if changerInfo == 5:
        tela.blit(intermediate, (0, scroll_y_pid))
        user_pid = pid.user_list()
        name_pid = pid.name_list()
        pid_pid = pid.pid_list()
        status_pid = pid.stat_list()

        show_pid_info(user_pid, name_pid, pid_pid, status_pid)

    # changebar
    pygame.draw.rect(tela, (100, 100, 225), (changerBarx + 1, 50, 120, 10))
    # line
    pygame.draw.rect(tela, (0, 0, 0), (0, 0, 1200, 50))
    pygame.draw.rect(tela, (50, 50, 100), (0, 50, 1200, 2))
    # separators line
    pygame.draw.rect(tela, (50, 50, 100), (120, 0, 2, 50))
    pygame.draw.rect(tela, (50, 50, 100), (120 * 2, 0, 2, 50))
    pygame.draw.rect(tela, (50, 50, 100), (120 * 3, 0, 2, 50))
    pygame.draw.rect(tela, (50, 50, 100), (120 * 4, 0, 2, 50))
    pygame.draw.rect(tela, (50, 50, 100), (120 * 5, 0, 2, 50))
    pygame.draw.rect(tela, (50, 50, 100), (120 * 6, 0, 2, 50))
    # texts
    cpu_info_surf = pattern_font.render("CPU", False, (255, 255, 255))
    disk_info_surf = pattern_font.render("DISK", False, (255, 255, 255))
    memory_info_surf = pattern_font.render("MEMORY", False, (255, 255, 255))
    ip_info_surf = pattern_font.render("IP", False, (255, 255, 255))
    pid_info_surf = pattern_font.render('PID', False, (255, 255, 255))
    dir_info_surf = pattern_font.render('DIR', False, (255, 255, 255))
    tela.blit(ip_info_surf, (410, 20))
    tela.blit(memory_info_surf, (255, 20))
    tela.blit(disk_info_surf, (155, 20))
    tela.blit(cpu_info_surf, (40, 20))
    tela.blit(pid_info_surf, (523, 20))
    tela.blit(dir_info_surf, (645, 20))

    # cpu selected
    if changerInfo == 1:
        # capturing data to add the def
        # time.sleep(0.3)

        cpuprocess = cpu.process()
        cpuidleprocess = cpu.idle_process().idle
        arch = cpu.cpu_archteture()
        speed_cpu = round(cpu.freq().current / 1000, 1)
        cores_fisics = cpu.cores_fisicos()
        cores_logical = cpu.cores()
        cpu_name = cpu.name()
        processment_per_sec_idle = cpuidleprocess
        processment_per_sec_used = cpuprocess

        # infos captured and passed to screen
        show_cpu_info(arch, cpu_name, speed_cpu, cores_logical, cores_fisics, processment_per_sec_used,
                      processment_per_sec_idle, cpuprocess, cpuidleprocess)

    # disk selected
    if changerInfo == 2:
        # capturing data to add the def
        diskprocess = disk.percent()
        i = 0
        listaPartMount = list(disk.listaPartMount)
        free_disk = disk.free()
        total_disk = disk.total()
        used_disk = disk.used()
        percentage_disk = diskprocess
        show_disk_info(listaPartMount[0], total_disk, used_disk, free_disk, percentage_disk, diskprocess)

    # memory selected
    if changerInfo == 3:
        # capturing data to add the def
        memoryprocess = memory.percentage()

        used_memory = memory.used()
        free_memory = memory.free()
        percentage_memory = memoryprocess
        size_memory = memory.size()
        show_memory_info(size_memory, percentage_memory, free_memory, used_memory)

    # ip selected
    if changerInfo == 4:
        # capturing data to add the def
        ipprocess = ip.info()
        # 1 = MAC 2 =IPV4 3 = IPV6
        MACaddress = ip.IpAddress('Ethernet', 0).address
        IPV4address = ip.IpAddress('Ethernet', 1).address
        IPV6address = ip.IpAddress('Ethernet', 2).address
        name = ip.pc_name()
        sent_bytes = ipprocess.bytes_sent
        received_bytes = ipprocess.bytes_recv
        sent_packets = ipprocess.packets_sent
        received_packets = ipprocess.packets_recv
        show_ip_info(name, MACaddress, IPV4address, IPV6address, sent_bytes, received_bytes, sent_packets,
                     received_packets)

    # dirss selected
    if changerInfo == 6:
        nn = (f"Partição em uso: {dirsss.partition}")
        dirsurff = pattern_font.render(nn, False, (255, 255, 255))
        ok = pattern_font.render('Diretórios:', False, (255, 255, 25))
        tela.blit(ok, (10, 90))
        tela.blit(dirsurff, (10, 60))


        #################3
        def creat_text(folder_name, var_height, widght_var):  # criar barras para cara núcleo
            write = pattern_font.render(folder_name, False, (255, 255, 255))
            tela.blit(write, (10 + widght_var, 130 + var_height))


        height_var = 0
        widght_var = 0
        folders = dirsss.folders_name()
        for i in folders:
            creat_text(i, height_var, widght_var)
            height_var += 30
            if height_var == telay - 150:
                height_var = 0
                widght_var += 300

    #########################

    InfoBarUsed()
    InfoBarIdle()

    tela.blit(boxImg, (telax - 175, telay - 75))
    pygame.display.update()
    # tick frames per second
    clock.tick(100)

pygame.quit()
quit()
