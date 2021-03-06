#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import subprocess
import glob

def perguntar(texto):
    resposta = str(input(texto + " ?(y/n) "))
    return(resposta)

if (perguntar("Instalar os pacotes samba") == "y"):
    subprocess.call(["apt-get install -y krb5-user bind9 samba winbind"], shell=True)

if (perguntar("Configurar tzdata") == "y"):
    subprocess.call(["dpkg-reconfigure tzdata"], shell=True)

if (perguntar("Subir samba no dominio") == "y"):
    dominio = str(input("Digite o nome do dominio(Ex: cooperativa.local):"))
    usuario = str(input("Digite o nome do usuario administrador:"))
    servidor = str(input("Digite o nome do servidor para ingressar:"))
    subprocess.call(["systemctl unmask samba-ad-dc"], shell=True)
    subprocess.call(["systemctl enable samba-ad-dc"], shell=True)
    subprocess.call(["samba-tool domain join " + dominio + " DC -U " + usuario + "@" + dominio +  "  --dns-backend=BIND9_DLZ --server=" + servidor + "." + dominio], shell=True)
    subprocess.call(["systemctl start samba-ad-dc"], shell=True)
    subprocess.call(["cp named.conf.local /etc/bind"], shell=True)
    subprocess.call(["chgrp bind /var/lib/samba/bind-dns/named.conf"], shell=True)
    subprocess.call(["chgrp bind /var/lib/samba/bind-dns"], shell=True)
    subprocess.call(["systemctl restart bind9"], shell=True)

