#author: Isabelle Bretl
#file: ec3.py
#date: 06/04/2021
#description: program that takes an array of integers and a target sum,
#   and returns the array of two integers that equal the target sum

def target(list, targetSum):
    n = len(list)
    for i in range (0,n):
        num1 = list[i]
        for j in range (1, n):
            num2 = list[j]
            if(num1 + num2 == targetSum):
                return [num1, num2]


testList = [2,7,11,15]
testList2 = [13, 9, 2, 4, 10, 0, 1, 2]
print("------Example 1-------")
print("Array: ", testList)
print("Target Sum: 9")
print("Result: ", target(testList, 9))
print("")
print("------Example 2-------")
print("Array: ", testList2)
print("Target Sum: 11")
print("Result: ", target(testList2, 11))
print("")