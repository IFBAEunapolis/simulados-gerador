#!/usr/bin/python2
# -*- coding: iso-8859-15 -*-

import csv

class Aluno(object):
    """Docstring for MyClass. """
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.disciplinas = []

        self.disciplinas.append

    def add_disciplina(self, disciplina):
        """ Método para adicionar disciplinas ao aluno """
        self.disciplinas.append(disciplina)


    def get_format_disciplinas(self):
        disciplinas_str = ''
        for disc in self.disciplinas:
            disciplinas_str = disciplinas_str + disc.codigo + ';'

        return disciplinas_str

class Disciplina(object):

    """Docstring for Disciplina. """

    def __init__(self, codigo, nome):
        """TODO: to be defined1. """
        self.codigo = codigo
        self.nome = nome

alunos = []

def find_aluno(matricula):
    for idx, item in enumerate(alunos):
        if item.matricula == matricula:
            return (True, idx)

    return (False, None)

with open('arquivos/alunos.csv', 'rt') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        disciplina = Disciplina(row['CÓDIGO DA DISCIPLINA'].strip(), row['NOME DA DISCIPLINA'])

        if row['MATRÍCULA']:
            ultimo_aluno = row['MATRÍCULA']

            novo_aluno = Aluno(row['NOME'], row['MATRÍCULA'])
            novo_aluno.add_disciplina(disciplina)
            alunos.append(novo_aluno)
        else:
            # Encontrar aluno
            encontrado, index = find_aluno(ultimo_aluno)

            if encontrado:
                alunos[index].add_disciplina(disciplina)

# Salvar alunos no arquivo 'alunos.csv'
with open('arquivos/alunos.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'disciplinas']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for aluno in alunos:
        writer.writerow({'id': aluno.matricula, 'name': aluno.nome, 'disciplinas':
                         aluno.get_format_disciplinas()})
