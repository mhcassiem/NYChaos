def minimumBribes(q):
    bribed = [0] * len(q)
    i = 0
    while i < len(q):
        if q[i] != i + 1 and q[i] > q[i + 1]:
            bribed[q[i]-1] += 1
            q[i], q[i + 1] = q[i + 1], q[i]
            i = i - 1 if i > 0 else i
        else:
            i += 1
    if all(item <= 2 for item in bribed):
        print(sum(bribed))
        return
    print('Too chaotic')
