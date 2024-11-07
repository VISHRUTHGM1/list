import math
oddsr = []
evensr = []
reg = []
start = int(input("Enter starting number"))
end = int(input("Enter end number"))
step = 1
for j in range(start, end + 1, step):
    reg.append(j)
for i in range(start, end + 1, step):
    sqrt = math.sqrt(i)
    if int(sqrt) % 2 == 0:
        evensr.append(sqrt)
    else:
        oddsr.append(sqrt)
print(f"Even square roots are {evensr}")
print(f"Odd square roots are {oddsr}")    
