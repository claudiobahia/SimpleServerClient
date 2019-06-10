import ip, pid
import socket, pickle

import pygame

# nmap tem que pegar um IP capturar todos dentro dessa classe que responderão meu servidor e listar as portas.

IP_SERVER = "127.0.0.1"
PORT_SERVER = 9991
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IP_SERVER,PORT_SERVER))

pygame.init()
telax = 1200
telay = 600
tela = pygame.display.set_mode((telax, telay))
intermediate = pygame.surface.Surface((telax, telay *(len(pid.pid_list())/16)-1200))
pygame.display.set_caption('Projeto de Bloco -- Cliente')
clock = pygame.time.Clock()

boxImg = pygame.image.load('cliente.png')
boxImg = pygame.transform.scale(boxImg, (175, 75))

# mudar entre toolbar
changerInfo = 1
changerBarx = 0

# pid part
scroll_y_pid = 0

pattern_font = pygame.font.Font('freesansbold.ttf', 20)


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
def show_cpu_info(arch, name, freq, logicalcore, fisicalcores, processment_in_use, processment_idle, per_core):
    cpu_name = f"Nome da CPU: {name}"
    cpu_arch = f"Arquitetura: {arch}"
    speed_cpu = f"Velocidade: {freq} Ghz"
    cores_logical = f"Cores: {logicalcore}"
    cores_fisics = f"Cores fisicos: {fisicalcores}"
    used = f"Processamento em uso: {round(processment_in_use, 1)} %"
    idle = f"Processamento em espera: {round(processment_idle, 1)} %"

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

    cpuspeedsuface = pattern_font.render(speed_cpu, True, (255, 255, 255))
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

def show_disk_info(dir, total, used, free, percentage):
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
    name = name
    MAC = MACaddress
    IPV4 =IPV4address
    IPV6 = IPV6address
    sent_bytes = f"Enviado {sent_bytes} bytes ou {round(sent_bytes / 1024 ** 3, 4)} GB"
    received_bytes = f"Recebido {received_bytes} bytes ou {round(received_bytes / 1024 ** 3, 4)} GB"
    sent_packets = f"Enviado  pacote de {sent_packets} bytes ou {round(sent_packets / 1024 ** 3, 4)} GB"
    received_packets = f"Recebido pacote de {received_packets} bytes ou {round(received_packets / 1024 ** 3, 4)} GB"

    name_surface = pattern_font.render(name, False, (255, 255, 255))
    tela.blit(name_surface, (10, 100))

    MAC_surface = pattern_font.render(MAC, False, (255, 255, 255))
    tela.blit(MAC_surface, (10, 130))

    IPV4_surface = pattern_font.render(IPV4, False, (255, 255, 255))
    tela.blit(IPV4_surface, (10, 160))

    IPV6_surface = pattern_font.render(IPV6, False, (255, 255, 255))
    tela.blit(IPV6_surface, (10, 190))

    sent_bytes_surface = pattern_font.render(sent_bytes, False, (255, 255, 255))
    tela.blit(sent_bytes_surface, (10, 220))

    received_bytes_surface = pattern_font.render(received_bytes, False, (255, 255, 255))
    tela.blit(received_bytes_surface, (10, 250))

    sent_packets_surface = pattern_font.render(sent_packets, False, (255, 255, 255))
    tela.blit(sent_packets_surface, (10, 280))

    received_packets_surface = pattern_font.render(received_packets, False, (255, 255, 255))
    tela.blit(received_packets_surface, (10, 310))


def show_pid_info(user, process_name, pid, status):
    user = user
    process_name = process_name
    pid = pid
    status = status


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

    for user in user:
        creat_text_list(user, height_var, var_widght)
        height_var += 30

    var_widght = 335
    height_var = 0

    for name in process_name:
        creat_text_list(name, height_var, var_widght)
        height_var += 30

    var_widght = 625
    height_var = 0

    for pid in pid:
        creat_text_list(pid, height_var, var_widght)
        height_var += 30

    var_widght = 750
    height_var = 0

    for status in status:
        creat_text_list(status, height_var, var_widght)
        height_var += 30


portas = []

crashed = False
while not crashed:

    data, addr = sock.recvfrom(1024*10)
    var_pickle = pickle.loads(data)
    print(var_pickle)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if changerInfo == 5:
                if event.button == 4: scroll_y_pid = min(scroll_y_pid + 15, 0)
                if event.button == 5: scroll_y_pid = max(scroll_y_pid - 15, -(len(pid.pid_list())*30-450))
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
                changerInfo = 7
                changerBarx = 120 * 6
            if changerInfo == 8:
                changerInfo = 1
                changerBarx = 0

    tela.fill((0, 0, 0))

    if changerInfo == 5:
        tela.blit(intermediate, (0, scroll_y_pid))
        user_pid = var_pickle[29]
        name_pid = var_pickle[30]
        pid_pid = var_pickle[31]
        status_pid = var_pickle[32]

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
    pygame.draw.rect(tela, (50, 50, 100), (120 * 7, 0, 2, 50))
    # texts
    cpu_info_surf = pattern_font.render("CPU", False, (255, 255, 255))
    disk_info_surf = pattern_font.render("DISK", False, (255, 255, 255))
    memory_info_surf = pattern_font.render("MEMORY", False, (255, 255, 255))
    ip_info_surf = pattern_font.render("IP", False, (255, 255, 255))
    pid_info_surf = pattern_font.render('PID', False, (255, 255, 255))
    nmap_info_surf = pattern_font.render('NMAP', False, (255, 255, 255))
    dir_info_surf = pattern_font.render('DIR', False, (255, 255, 255))
    tela.blit(ip_info_surf, (410, 20))
    tela.blit(memory_info_surf, (255, 20))
    tela.blit(disk_info_surf, (155, 20))
    tela.blit(cpu_info_surf, (40, 20))
    tela.blit(pid_info_surf, (523, 20))
    tela.blit(nmap_info_surf, (635, 20))
    tela.blit(dir_info_surf, (760, 20))

    # cpu selected
    if changerInfo == 1:
        # capturing data to add the def

        cpuprocess = var_pickle[8]

        cpu_name = var_pickle[0]
        arch = var_pickle[1]
        speed_cpu = var_pickle[2]
        cores_logical = var_pickle[3]
        cores_fisics = var_pickle[4]
        processment_per_sec_used = var_pickle[5]
        processment_per_sec_idle = var_pickle[6]
        cpuidleprocess = var_pickle[9]
        ################ each core bar ########################
        per_core = var_pickle[7]

        # infos captured and passed to screen
        show_cpu_info(arch, cpu_name, speed_cpu, cores_logical, cores_fisics, processment_per_sec_used,
                      processment_per_sec_idle,per_core)

    # disk selected
    if changerInfo == 2:
        # capturing data to add the def

        diskprocess = var_pickle[15]
        i = 0
        listaPartMount = var_pickle[10]
        free_disk = var_pickle[13]
        total_disk = var_pickle[11]
        used_disk = var_pickle[12]
        percentage_disk = var_pickle[14]
        show_disk_info(listaPartMount[0], total_disk, used_disk, free_disk, percentage_disk)

    # memory selected
    if changerInfo == 3:
        # capturing data to add the def
        memoryprocess = var_pickle[20]

        used_memory = var_pickle[18]
        free_memory = var_pickle[17]
        percentage_memory = var_pickle[19]
        size_memory = var_pickle[16]
        show_memory_info(size_memory, percentage_memory, free_memory, used_memory)

    # ip selected
    if changerInfo == 4:
        # capturing data to add the def
        ipprocess = ip.info()
        # 1 = MAC 2 =IPV4 3 = IPV6
        MACaddress = var_pickle[22]
        IPV4address = var_pickle[23]
        IPV6address = var_pickle[24]
        name = var_pickle[21]
        sent_bytes = var_pickle[25]
        received_bytes = var_pickle[26]
        sent_packets = var_pickle[27]
        received_packets = var_pickle[28]
        show_ip_info(name, MACaddress, IPV4address, IPV6address, sent_bytes, received_bytes, sent_packets,
                     received_packets)

    if changerInfo == 6:
        portas = var_pickle[36]
        ip_used = var_pickle[33]
        warning_surface = pattern_font.render("(Para alterar o ip basta localizar linha 382 do servidor)", False, (255, 255, 0))
        tela.blit(warning_surface, (10, 100))
        aa_surface = pattern_font.render("Endereço escaneado: '127.0.0.1'", False, (255, 255, 255))
        tela.blit(aa_surface, (10, 130))
        porta_surface = pattern_font.render(str(portas), False, (255, 255, 255))
        tela.blit(porta_surface, (10, 160))


    if changerInfo == 7:
        nn = var_pickle[34]
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
        folders = var_pickle[35]
        for i in folders:
            creat_text(i, height_var, widght_var)
            height_var += 30
            if height_var == telay - 150:
                height_var = 0
                widght_var += 300
    #########################33
    InfoBarUsed()
    InfoBarIdle()

    tela.blit(boxImg, (telax - 175, telay - 75))
    pygame.display.update()
    # tick frames per second
    clock.tick(100)

pygame.quit()
quit()
