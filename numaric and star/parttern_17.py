'''
   *       *
  * *     * *
 * * *   * * *
* * * * * * * *
* * a m u l * *
* * * * * * * *
 * * * * * * *
  * * * * * *
   * * * * *
    * * * *
     * * *
      * *
       *

'''
num = int(input("Enter a number ......"))
msg = input("Enter any message.........")
l = len(msg)
n = num//2

for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1),end="")
    if num%2 == 0:
        for j in range(2*(n-i-1)):
            print(" ",end="")
    else:
        for j in range(2*(n-i-1)+1):
            print(" ",end="")
    for j in range(i+1):
        print("* ",end="") 
    print()

if ((num%2 != 0) and (l%2 == 0)) or ((num%2 == 0) and (l%2 != 0)):
    print("* "*((num-l)//2)+" ".join(msg)+" *"*(((num-l)//2)+1))
else:
    print("* "*((num-l)//2)+" ".join(msg)+" *"*((num-l)//2))
for i in range(num, 0 ,-1):
    print(" "*(num-i)+"* "*i)