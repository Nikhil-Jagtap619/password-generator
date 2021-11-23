import random 


user = int(input("strength of password: \n 1: weak \n 2: strong \n choose any one: "))
small = list(map(chr,range(97,123)))
upper = list(map(chr,range(65,93)))
num = random.sample(list(map(str,range(10))),2)
# num = map(str,num)
# num = "".join(num)
sign = "".join(random.sample(["!","@","#","$","%","^","&","*"],1))

if user == 1:
    smallcase = random.sample(small,5)
    smallcase = "".join(smallcase)
    uppercase = random.sample(upper,1)
    password = "".join(uppercase)+smallcase
    print(password)

else:
    smallcase = "".join(random.sample(small,5))
    uppercase = "".join(random.sample(upper,1))
    password = uppercase+smallcase+"".join(num)+sign
    print(password)

