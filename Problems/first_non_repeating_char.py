# In a given string, find the first non-repeating character .You are given a string, that can contain repeating characters. Your task is to return the first character in this string that does not repeat. i.e., occurs exactly once. The string will contain characters only
# from English alphabet set, i.e., ('A' - 'Z') and ('a' - 'z'). If there is no non-repeating character print the first character of string.

# Sample Input 1 :

# aDcadhc

# Sample Output 1:

# D

# Sample Input 2 :

# gdhIgHada

# Sample Output 2 :

# h

def nonRepeatingChar(string):
    d = {}
    for i in range(len(string)):
        d[string[i]] = d.get(string[i], 0) + 1
    for s in string:
        if d.get(s) == 1:
            return s

# Main
string = input()
print(nonRepeatingChar(string))


