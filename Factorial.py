num =  9

factorial = 1

if num < 0:
    print("false", num)
if num == 0:
    print("great", num)
if num > 1:
     print("got it",num)
else:
   for num in range(0, num + 99):
    factorial = factorial * num
    print("the answer",num,"is",factorial)



