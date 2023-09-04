import libtorrent as lt
import time
import os
import subprocess


def getTorrent():
    ses = lt.session()
    info = lt.torrent_info('/CHANGEME') #CAMINHO ARQUIVO .torrent
    h = ses.add_torrent({'ti': info, 'save_path': os.getcwd()})
    s = h.status()

    while (not s.is_seeding):
        s = h.status()
        p = h.get_peer_info()

        print("Lista de IPs dos peers:")
        for peer_info in p:
            nmapTest(peer_info.ip[0])

        
        time.sleep(5)

def nmapTest(ip):
    check = subprocess.check_output('nmap -T5 --script vuln ' + ip ,shell=True, universal_newlines=True)
    if check.strip == 'VULNERABLE':
        print('[Z] Vulneravel:' + ip)
        with open ('vuln' 'a') as vuln:
            vuln.write(ip + '\n')
    else:
        print('[X] ' + ip)


if __name__ == '__main__':
    getTorrent()




   
