# In Little Flowers Public School, there are many students with same first names. You are given a task to find the students with same names.
# You will be given a string comprising of all the names of students and you have to tell the name and count of those students having same. If all the names are unique, print -1 instead.
# Note: We don't have to mention names whose frequency is 1.

# Sample Input 1:

# Abhishek harshit Ayush harshit Ayush Iti Deepak Ayush Iti

# Sample Output 1:

# harshit 2
# Ayush 3
# Iti 2

def differentNames(l):
    d = {}
    for i in range(len(l)):
        d[l[i]] = d.get(l[i], 0) + 1
    for ele in d.copy():
        if d[ele] < 2:
            del d[ele]
    return d

# Main
names=input().strip().split()
m=differentNames(names)
if m:
    for name in m:
        print(name, m[name])
else:
    print(-1)

