import email
import sqlite3
from agenda import Contato
import json

contatos = Contato
conexao = sqlite3.connect('contatos.db')
cursor = conexao.cursor()
def achar_nome():
    try:
        with open('contatos.json', 'r', encoding='utf-8') as f:
            nome = f
            return nome
    except FileNotFoundError:
        return("não deu certo")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        email TEXT UNIQUE
    )
''')


