__author__ = 'Robert'

T = int(input())

for i in range(T):

    N,C,M = str(input()).split()
    N,C,M = int(N),int(C),int(M)


    # Compute Answer
    x = N//C
    answer = x
    while True:
        w = x//M
        r = x%M
        answer += w
        x = w + r
        if x < M: break


    print(answer)

