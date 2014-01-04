# -*- coding: utf-8 -*-
'''
Script Gerador de Arquivos SEFAZ
Copyright (C) 2014 - Marcilio Leite

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import json
import kinterbasdb
import time

# Carrega configs
print "Carregando configurações..."

file = open('config.json')
cfg_json = json.load(file)

cfg = {}
cfg['dsn'] = cfg_json['firebird']['dsn'].encode('latin-1')
cfg['usr'] = cfg_json['firebird']['usr'].encode('latin-1')
cfg['psw'] = cfg_json['firebird']['psw'].encode('latin-1')

info = {}
info['data_ini'] = cfg_json['datas']['ini'].encode('latin-1')
info['data_fin'] = cfg_json['datas']['fin'].encode('latin-1')

sefaz_doc = '' 

print "Configurações carregadas"

# Conecta ao BD
print "Conectado ao banco de dados..."

con = kinterbasdb.connect(dsn=cfg['dsn'], user=cfg['usr'], password=cfg['psw'])

print "Conexão estabelecida"

# Bloco 0
# Linha 0000
print "Gerando Bloco 0..."

l_0000 = open('templates/0000.txt').read();
l_0000 = l_0000.replace("{@data_inicial}",  info['data_ini']).replace('/', '')
l_0000 = l_0000.replace("{@data_final}",    info['data_fin']).replace('/', '')

print l_0000
