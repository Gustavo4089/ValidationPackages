# this archive it´s the main path
from ValidationPackages import cpf # import function cpf
import sqlite3 # import package 

connect = sqlite3.connect('processo_seletivo.db') # connecting database
cur = connect.cursor() # database cursor enabled
lista = cur.execute('SELECT cpf FROM lista') # list all cpf´s into database

for c in lista.fetchall():
    print(cpf(c[0]).cpf_is_valid())