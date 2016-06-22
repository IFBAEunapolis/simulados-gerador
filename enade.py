#!/usr/bin/python3

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

    def __init__(self, codigo, nome, ano, semestre, conceito):
        """TODO: to be defined1. """
        self.codigo = codigo
        self.nome = nome
        self.ano = ano
        self.semestre = semestre
        self.conceito = conceito

alunos = []

def find_aluno(matricula):
    for idx, item in enumerate(alunos):
        if item.matricula == matricula:
            return (True, idx)

    return (False, None)

with open('Disciplinas aprovadas.csv', 'rt') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        disciplina = Disciplina(row['CODIGO DISCIPLINA'], row['NOME DISCIPLINA'], row['ANO'], row['SEMESTRE'], row['CONCEITO'])

        # Encontrar aluno
        encontrado, index = find_aluno(row['MATRÍCULA'])

        if encontrado:
            alunos[index].add_disciplina(disciplina)
        else:
            novo_aluno = Aluno(row['NOME'], row['MATRÍCULA'])
            novo_aluno.add_disciplina(disciplina)
            alunos.append(novo_aluno)

# Salvar alunos no arquivo 'names.csv'
with open('names.csv', 'w') as csvfile:
    fieldnames = ['name', 'disciplinas']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for aluno in alunos:
        print(aluno.get_format_disciplinas())
        writer.writerow({'name': aluno.nome.title(), 'disciplinas':
                         aluno.get_format_disciplinas()})
