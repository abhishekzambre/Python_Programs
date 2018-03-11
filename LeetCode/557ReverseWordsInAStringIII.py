def reverseWords(s):
    return ' '.join(x[::-1] for x in s.split())

def reverseWords2(s):
    print(s)
    print((' '.join(s.split()[::-1]))[::-1])
    return ' '.join(s.split()[::-1])[::-1]


print(reverseWords2("Abhishek Zambre"))