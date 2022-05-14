name=input("enter your name")
infile=open("lama.txt",'r')
l=infile.readlines()
infile.close()
n=0
print("anser true or false")
for i in l:
    q=i.rstrip().split('=')
    print(q[0])
    a=input()
    if a==q[1]:
        n+=1
print("user name:",name,"result:", n)
outfile=open("resault.txt",'w')
outfile.writelines(name)
outfile.writelines("\n")
outfile.writelines(str(n))
outfile.close()
