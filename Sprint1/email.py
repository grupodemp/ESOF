#

#Exemplo 2, expressões regulares

import re

email = str(input("Digite um email:"))

padrao_email = re.search(r'\w+@\w+\.\w+', email)

if padrao_email.group() == email:
	print("É email")
else:
	print("Não é email")
