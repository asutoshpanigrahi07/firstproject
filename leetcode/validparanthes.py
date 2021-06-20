p="[{[]}](())"
dict = {"{":"}", "[":"]", "(":")"}
l=[]
for i in range(0,len(p)):
    print(l)
    print(p[i])
    
    if p[i] in '([{':
        l.append(p[i])
    elif l and p[i] == dict[l[-1]]:
        l.pop()
    else:
        print(False)
if(len(l) == 0):
    print("Valid")
else:
    print("invalid")

while("{}" in p or "[]" in p or "()" in p):
    p =p.replace("()", "").replace("[]", "").replace("{}", "");        
    
if(len(p) == 0):
    print("Valid")
else:
    print("invalid")
