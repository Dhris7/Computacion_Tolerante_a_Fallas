import sys
import time

def check_arguments():
    if len(sys.argv) == 1:
        print('Este programa no funciona sin argumentos')
        sys.exit(0)

def get_blocked_sites():
    return sys.argv[1:]

def block_sites(sites):
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    with open(hosts_path, 'a') as file:
        for site in sites:
            file.write('127.0.0.1 {}\n'.format(site))

if __name__ == '__main__':
    check_arguments()
    sites_to_block = get_blocked_sites()
    while True:
        block_sites(sites_to_block)
        time.sleep(60)  # Bloquea los sitios cada 60 segundos
