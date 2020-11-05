name = input("What is your name? ")
amount_needed = input("How much loan do you want? ")
your_income = input("What is your or your family's monthly income in Rs.? ")
your_credit_score = input("What is your credit score? ")
num_of_legal_rec = input("Do you have any legal issue? How many in number? ")
if int(amount_needed) <= 10000000 and int(your_income) >= 800000 and int(your_credit_score) >= 700 and int(num_of_legal_rec) == 0:
    print(name + ", We will be happy to give you a loan.")
else:
    print("Sorry! we are afraid that we can not provide you a loan.")
