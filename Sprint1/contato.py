#

#Exemplo 3, expressões regulares

import re

contactInfo = 'Daniel, 11611EAU017: 9999-0000'

infos = re.search(r'(\w+), (\w+): (\S+)', contactInfo)

nome = infos.group(1)
matricula = infos.group(2)
telefone = infos.group(3)

print(nome)
print(matricula)
print(telefone)
