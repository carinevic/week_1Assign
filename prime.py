number = int(input("enter num: "))


for index in range(2, number):
     if number  % index ==0:
         print("not a prime")
         break

     else:
         print("prime")