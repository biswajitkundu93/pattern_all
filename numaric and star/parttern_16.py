'''

   *       *
  * *     * *
 * * *   * * *
* * * * * * * *
* * * * * * * *
 * * * * * * *
  * * * * * *
   * * * * *
    * * * *
     * * *
      * *
       *

'''

n = int(input("Enter any number.....!"))

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    for j in range(2*(n-i-1)):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()

for row in range((n*2),0,-1):
    for space in range((n*2)-row):
        print(" ",end="")
    for col in range(row, 0, -1):
        print("* ",end="")
    print()
