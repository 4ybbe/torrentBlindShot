# Torrent Blind Shot
> Scan em massa de IP's atualizados

## Dependencias
```sh
Python
 - libtorrent
Nmap
```
## Sobre
- Pega a lista de seeder e leecher do torrent e executa um script generico do nmap e salva caso for vulneravel
- Recomendo rodar em uma VPN
- Nao me responsabilizo por seja la quem for usar isso

## Instalacao
Linux:
```sh
libtorrent:
    - sudo apt-get install python3-libtorrent
nmap:
    - sudo apt-get install nmap
```
Windows:
```sh
Libtorrent:
    - Boa sorte com isso:
        - https://www.libtorrent.org/python_binding.html
Nmap:
    - https://nmap.org/download.html
```

## Uso:
Especifique o caminho do arquivo .torrent (Linha 9)
