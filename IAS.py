def N_to_B(n):
    n = int(n)
    ans = ""
    while n!=0:
        ans = str(n%2) + ans
        n//=2
    ans = '0'*(12-len(ans)) + ans
    return ans

def N_to_B_D(n):
    n = int(n)
    ans = ""
    while n!=0:
        ans = str(n%2) + ans
        n//=2
    ans = '0'*(40-len(ans)) + ans
    return ans

def get(n):
    with open("binary.text","r") as f:
        i = 1
        for l in f:
            if i==n:
                return l.strip()
            i+=1

def store(n,s):
    with open("binary.text","r") as f:
        lines = f.readlines()
    lines[n-1] = s + "\n"
    with open("binary.text","w") as f:
        f.writelines(lines)

PC = 1
IBR = ""
IR = ""
MAR = ""
AC = 0
while True:
    if IBR == "":
        MBR = get(PC).strip().split()
        IR  = MBR[0][:8]
        MAR = MBR[0][8:]
        IBR = MBR[1]
    else:
        IR  = IBR[:8]
        MAR = IBR[8:]
        IBR = ""
    if IR == "11111111" and MAR!= "000000000000":
        MBR = get(int(MAR,2))
        AC = int(MBR,2)
    elif IR =="00100001":
        store(int(MAR,2),N_to_B_D(AC))
    elif IR =="00000101":
        MBR = get(int(MAR,2))
        AC = AC + int(MBR,2)
    elif IR == "00000110":
        MBR = get(int(MAR,2))
        AC = AC - int(MBR,2)
    elif IR == "00001101":
        PC = int(MAR,2)
        IBR = ""
        print(f"PC = {PC}\nMBR = {MBR}\nIR = {IR}\nMAR = {MAR}\nAC = {AC}\n\n")
        continue
    elif IR == "00001110":
        PC = int(MAR,2)
        MBR = get(PC).strip().split()
        IBR = MBR[1]
        print(f"PC = {PC}\nMBR = {MBR}\nIR = {IR}\nMAR = {MAR}\nAC = {AC}\n\n")
        continue
    elif IR == "00001111":
        if AC >=0:
            PC = int(MAR,2)
            IBR = ""
            print(f"PC = {PC}\nMBR = {MBR}\nIR = {IR}\nMAR = {MAR}\nAC = {AC}\n\n")
            continue
    elif IR == "00010000":
        if AC >=0:
            PC = int(MAR,2)
            MBR = get(PC).strip().split()
            IBR = MBR[1]
            print(f"PC = {PC}\nMBR = {MBR}\nIR = {IR}\nMAR = {MAR}\nAC = {AC}\n\n")
            continue
    elif IR =="00000000":
        print(f"PC = {PC}\nMBR = {MBR}\nIR = {IR}\nMAR = {MAR}\nAC = {AC}\n\n")
        break
    elif IR =="00000001":
        pass
    print(f"PC = {PC}\nMBR = {MBR}\nIR = {IR}\nMAR = {MAR}\nAC = {AC}\n\n")
    if IBR == "":
        PC += 1
print(f"Fib({int(get(17),2)}) = {int(get(20),2)}")