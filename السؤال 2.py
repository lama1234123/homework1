i=int(input('enter number'))
b=[]
while True:
    b.append(str(i%2))
    i//=2
    if i==0:
        break
b.reverse()
r=''.join(b)
print(r)
