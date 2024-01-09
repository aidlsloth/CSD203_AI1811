lis = []
while True:
    try:
        Input = int(input("Enter a value: "))
        lis.append(Input)
    except:
        break   
avg = float(sum(lis)/len(lis))
nearest = sum(lis)
for i in range(len(lis)):
    dist = abs(lis[i] - avg)
    if dist < nearest:
        nearest = dist
print(nearest)
print(lis.index(nearest + avg))

