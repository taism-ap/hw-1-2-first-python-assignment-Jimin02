x = input("Enter your first number: ")
y = input("Enter your second number: ")

print ("Select operation")
print ("1.+")
print ("2.-")
print ("3.*")
print ("4./")
operation = input("Enter your choice (1/2/3/4/): ")

if operation == "1":
  print (int(x)+int(y))
elif operation == "2":
  print (int(x)-int(y))
elif operation == "3":
  print (int(x)*int(y))
elif operation == "4":
  print (int(x)/int(y))
else:
  print("Invalid input")
  
