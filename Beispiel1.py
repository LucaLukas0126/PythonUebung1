
land="AT"
blz="38282"
konto= "3026713"
check = "96"

for i in range(len(konto), 11, 1):
    konto = "0" + konto

p1 = land + check
p2 = blz[0:4]
print(p1,p2)



print("Kontonummer:",konto)
print()


