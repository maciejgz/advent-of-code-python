import os




input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    lines = f.readlines()

a = [l.strip() for l in lines][0]
a = [int(x) for x in a]
#print(a)

sum = 0
block = 0
last = len(a)-1
for i in range(len(a)):
    #if last<=i:
        #break
    v=int(a[i])
    if i%2==0:
        for _ in (range(v)):
            sum+=((i//2)*block)
            block+=1
            #print((i//2), end='')
    elif last>i:
        for _ in range(v):
            while last>i and a[last]==0:
                last-=2
            if last<=i:
                break
            sum+=((last//2)*block)
            #print((last//2), end='')
            block+=1
            a[last]-=1
#print('')
print(sum)
