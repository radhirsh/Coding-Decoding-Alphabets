Alphabets=["0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Alphabets1=["0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
string1=str(input("Do you want to know the word total?"))
empty=[]
empty1=[]
upper=[]
lower=[]
for i in string1:
    empty.append(i)

for j in empty:
    if j.isupper():
        upper.append(j)
    else:
        lower.append(j)

for c in upper:
    empty1.append(Alphabets.index(c))

for c in lower:
    empty1.append(Alphabets1.index(c))


print(sum(empty1))
