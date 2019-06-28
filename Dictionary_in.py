#dictionary deals mostly with keys. every key has a value,
#dictionary starts with {}.
# to get acces to a dictionary you most know the key. (grocery["phone"])
# to add grocery ["storenum"] = "store234"
#to update grocery["quatity"] = 12
# to delete a value grocery["quatity"]
# to loop via. for (key, value) in grocery.item():
# print(key) print(value)

#MODULE:create file and transfer the file to another file.
# statement to import from myLibray inmport calculate factorial.
#from mylibrary  import *
#import mylibrary
#import should always be on the top
#def cal_factorial(number):
#result =1

def calculate_factorial(number):
    result =1
    for index in range (1, number +1):
        result *= index
        return result


try:
        number = int(input("enter number"))
        result = calculate_factorial(number)
except ValueError:
        print("please enter only number")
except:
        print("something bad happened")

        try:
            print("try")
        finally:
            print("finally")