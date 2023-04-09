# For a given input string(str), write a function to print all the possible substrings.
# Sample Input 1:
# abc
# Sample Output 1:
# a 
# ab 
# abc 
# b 
# bc 
# c 

word = input()

for i in range(len(word)):
    slice_index = i
    while True:
        print(word[i:slice_index+1])
        slice_index += 1
        if slice_index >= len(word):
            break
