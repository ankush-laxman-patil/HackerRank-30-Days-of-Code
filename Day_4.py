N=int(input())

def testcase(N):
    if N%2 !=0:
        print("weird")
    elif N%2 ==0:
        if 2 <=N <=5:
            print("Not Weird")
        elif 6 <=N <=20:
            print("weird")
        elif N > 20:
            print("Not weird")
    return;

testcase(N)
