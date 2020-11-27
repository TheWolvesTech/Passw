import  random
alpha = "abcdefghijklmnopqrstuvwxyz" 
number = "0123456789"
simbol = "!@#$%*{}.[]\/-_"
all = alpha + alpha.upper() + number + simbol
length = random.randint(13,15)
passd = "".join(random.sample(all,length))
print(passd)