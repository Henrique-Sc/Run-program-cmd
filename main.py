from os import system


with open('name-program.txt', 'r') as arquivo:
    name_program = arquivo.read()
system('start notepad')
