
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

combined_names = str(name1 + name2)

T = combined_names.count('t')
R = combined_names.count('r')
U = combined_names.count('u')
E = combined_names.count('e')
L = combined_names.count('l')
O = combined_names.count('o')
V = combined_names.count('v')
E = combined_names.count('e')

true = int(T + R + U + E)
love = int(L + O + V + E)

result = int(str(true) + str(love))

if result < 10 or result > 90:
  print(f"Your score is {result} , you go together like coke and mentos.")
elif result >= 40 or result <= 50:
  print(f"Your score is {result}, you are alright together.")
else:
  print(f"Your score is {result}.")



