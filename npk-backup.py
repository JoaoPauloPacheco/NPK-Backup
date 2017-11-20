#!/usr/bin/env python3.6
# encoding: utf-8
"""
Um pequeno utilitário para automatizar a cópia de segurança de uma determinada
pasta (por exemplo, cópias de segurança locais de uma base de dados Filemaker,
uma coleção de scripts e aplicações do Pythonista, etc.), criando arquivos 
*zip* individuais a partir de cada pasta principal nalocalização especificada e
fazendo *upload* dos mesmos para a Dropbox. O programa mantém um registo
simples, por forma a nao repetir as tarefas de compressão e upload já
realizadas.

© 2017 Victor Domingos (http://victordomingos.com)
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""

import shutil
import datetime
import os

import dropbox


TIMESTAMP = str(datetime.datetime.now())


# ------- Configurar estas variáveis antes de usar. ---------

# Caminho completo para a pasta que contém os ficheiros e pastas a arquivar e copiar.
INPUT_FOLDER = os.path.expanduser('~/Documents/Filemaker_backups/NPK-Backup/')

# Caminho completo para o arquivo zip temporário a criar para o upload.
ARCHIVE_NAME = os.path.expanduser('~/Documents/Filemaker_backups/NPK-Backup/npk-backup__' + TIMESTAMP)

# Caminho completo para o ficheiro de registo
BACKUP_LOG_FILE = os.path.expanduser('~/Documents/Filemaker_backups/NPK-Backup/backup-log.txt')

# Token de acesso ao Dropbox
TOKEN = 'GetYourAppTokenFromDropboxAndInsertItHere'

# ----------------------------------------------------------


def obter_registo(BACKUP_LOG_FILE):
	""" Obtém do ficheiro de registo a lista das pastas já copiadas. """
	pass


def comprimir_pasta(origem, destino):
	""" Comprime a pasta de origem para o destino especificado. """
    try:
        arq = shutil.make_archive(destino, 'zip', origem)
        return arq
    except Exception as e:
        print('Ocorreu um erro durante a compressão:')
        print(e)
        return None
        

def upload_dropbox(archive):
	""" Faz upload do ficheiro especificado para a Dropbox. """
    try:
        dbx = dropbox.Dropbox(TOKEN)
        with open(archive, 'rb') as f:
            dbx.files_upload(f, archive)
        return True
    except Exception as e:
        print('Ocorreu um erro durante o upload para a Dropbox:')
        print(e)
        return None

def apagar_arquivo(archive):
	""" Apaga o ficheiro especificado no sistema de ficheiros local. """
    try:
        upload_dropbox(ARCHIVE_NAME)
    except Exception as e:
        print('Ocorreu um erro ao apagar o arquivo zip:')
        print(e)
        

def adiciona_registo(folder):
	""" Adiciona o caminho especificado ao ficheiro de registo. """
    pass


arq = comprimir_pasta(INPUT_FOLDER, ARCHIVE_NAME)
type(arq)

print(arq)


if arq:
    if upload_dropbox(arq):
        adiciona_registo(INPUT_FOLDER)
    apagar_arquivo(ARCHIVE_NAME)
    pass # continue
else:
    pass # continue