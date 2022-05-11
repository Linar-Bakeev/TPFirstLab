space = {}
n = int(input())
for i in range(n):
    person = input().split()
    if person[2] in space:
        space[person[2]].append([person[0], person[1]])
    else:
        space[person[2]] = [[person[0], person[1]]]

num = int(input())
arr = [input() for _ in range(num)]

for word in arr:
    if word in space:
        arr = sorted(space[word], key=lambda x: (int(x[1]), x[0]))
        st = ''
        for x in arr:
            st += ' '.join(x) + ' '
        print(st.rstrip())
    if word not in space:
        print()
