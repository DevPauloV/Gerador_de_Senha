import random 
# import que mistura os dados fornecidos aleatoriamente 


# função só com letra minuscula
min = 'abcdefghijklmnopqrstuvwxyz'

# função só com letra maiuscula 
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# função só com numero
num = '0123456789'

qnt = input('Digite o tamanho da senha desejado: ')
qntInt = int(qnt)
length = qntInt

#fazendo senha com todos
all = min + max + num 
senhatodos = "".join(random.sample(all,length))

#só maiúsculas e números
MAXnum = max + num
senha_max_num = "".join(random.sample(MAXnum,length))

#só minusculas e maiúsculas
MAXmin = max + min
senha_min_max = "".join(random.sample(MAXmin,length))

print ('senhatodos = ' + senhatodos) 
print ('senha_max_num = ' + senha_max_num) 
print ('senha_min_max = ' + senha_min_max)
  