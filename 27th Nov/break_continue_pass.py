#Break - stops all the iterations 
items = [10,20,40,110,20,506,70,80,90,500,120]
print("Break")
for i in items:
    if i >= 100:
        break
    print(i)
#Continue - will only skip the iteration
print("Continue")
for i in items:
    if i >= 100:
        continue
    print(i)
#odd or even
print("Odd Numbers")
for i in range(1,51):
    if i % 2 == 0:
        continue
    print(i)
#Pass
print("Odd Numbers")
for i in range(1,51):
    if i % 2 != 0:
        pass
    else:
        print(i)