# Given a string, determine if it is a palindrome, considering only alphanumeric characters.


word = input()
start = 0
end = len(word)-1
flag = True
while True:
    if word[start]!=word[end]:
        flag = False
        break
    if start == end or start > end:
        break
    start += 1
    end -= 1

if flag:
    print("true")
else:
    print("false")
