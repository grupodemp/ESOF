#

#Exemplo 1, expressões regulares

import re #Importando módulo para Expressões Regulares

string_base = 'olá este é o primeiro sprint para esof'

padrao = re.search('\w\w\w\w', string_base) #Procura as primeiras 4 letras seguidas

print(padrao.group())



