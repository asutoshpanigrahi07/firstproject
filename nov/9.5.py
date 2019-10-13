n=input("Enter a string:")
s=("Enter substring:")
l=len(n)
ls=len(s)
start=count=0
end=l

while true:
    pos=n.find(sub,start,end)
    if pos!=-1:
        count+=1
        start=pos+ls
    else:
        break
    if start>=l:
        break
    print("No. of occurrences of",s,':',count)
    
