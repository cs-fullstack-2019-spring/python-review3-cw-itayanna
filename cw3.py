# Python Review Misc Topics

def main():
    #problem1()
    #problem2()
    problem3()

#Given a number n, return ```True``` if n is in the range 1..10, inclusive.
# Unless outside_mode is ```True```, in which case return True if the number is less or equal to 1, or greater or equal to 10.
# Print the result returned from your function.

def int1to10(n,outside_mode):
    if outside_mode==True:
        if n<=10 and n>=1:
            return ("True")
        else:
            return ("False")
    elif outside_mode==False:
        if n<=10 and n>=1:
            return ('False')
        else:
            return ("True")




# Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign, ask them to input another string.
#
# Once the user enters the equal sign to quit, print all the strings that were entered as one line with each word separated by a comma and space.


def problem1():
    userInt= int(input("enter a number between 1 and 10"))
    print(int1to10(userInt,True))
    print(int1to10(userInt,False))




def problem2():
     userstring= input("Enter a word. Enter = to quit")
     wordsList= []
     while userstring != "=":
        userstring= input("Enter a word. Enter = to quit")
        wordsList.append(userstring)
     wordsList.pop(len(wordsList)-1)
     s= ","
     s= s.join(wordsList)
     print(s)

import random
def near_ten(num):
    if num%10==0 or (num-1)%10==0 or (num-2)%10==0 or (num+1)%10==0 or (num+2)%10==0:
        print('True')
    else:
        print('False')
# Given a non-negative number "num", return ```True``` if num is within ```2``` of a *multiple of 10*. Print the result from your function.

def problem3():
    userNum= int(input("enter a non-negative number"))
    near_ten(userNum)


























if __name__ == '__main__':
    main()