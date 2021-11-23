import random, string
upper = string.ascii_uppercase
lower = string.ascii_lowercase
num = string.digits
punct =string.punctuation

Try = True
while Try:
    user = int(input("Strength of password? \n 1: weak \n 2: strong \n 3: excellent \n"))
    if user==3:
        first = "".join(random.sample(upper,1))
        second = "".join(random.sample(lower,5))
        third = "".join(random.sample(num,2))
        last = "".join(random.sample(punct,1))
        password = first+second+third+last
        print(password)

    elif user==2:
        first = "".join(random.sample(upper,1))
        second = "".join(random.sample(lower,4))
        third = "".join(random.sample(num,1))
        password = first+second+third
        print(password)
    else:
        first = "".join(random.sample(upper,1))
        second = "".join(random.sample(lower,6))
        password = first+second
        print(password)

    retry = input("try again? y/n \n")
    if retry!="y":
        Try=False

