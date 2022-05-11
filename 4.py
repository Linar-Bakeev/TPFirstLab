string = input()
cout = 1
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            cout += 1
        else:
            a = string[i]
            print(cout, string[i])
            cout = 1
print(cout, string[i])
