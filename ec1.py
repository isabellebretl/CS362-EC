#author: Isabelle Bretl
#file: ec1.py
#date: 06/04/2021
#description: program that takes in a sentence and reverses the order of the words


#method to reverse the order of elements in a list
def reverse(list):
    words = int(len(list)/2)
    idx = len(list)-1
    for i in range(0,words):
        temp = list[idx]
        list[idx] = list[i]
        list[i] = temp
        idx = idx - 1
    return list

#gets a sentence from the user
inp = str(input("Enter a sentence: "))
#turn it into a list of seperate strings
list = inp.split(" ")
newList = reverse(list)
test = " "
#make the list into a sentence
reversedS = test.join(newList)
#print results
print(reversedS)