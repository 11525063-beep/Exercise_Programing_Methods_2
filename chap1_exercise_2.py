string=" TEMP_DATA:25.678 "
c=string.strip()
num=float(c[10:16])
print(string)
print(type(num))
print(f"{num:.2f}")