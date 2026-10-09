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

codes = {
    "LOAD":"11111111",
    "STOR":"00100001",
    "ADD" :"00000101",
    "SUB" :"00000110",
    "JUMP_L":"00001101",
    "JUMP_R":"00001110",
    "JUMP+_L":"00001111",
    "JUMP+_R":"00010000",
    "HALT":"00000000",
    "NOP":"00000001"
}

with open("assembly.txt","r") as f:
    for line in f:
        c = line.split()
        res = ""
        if len(c)>3:
            for i in range(0,3,2):
                if c[i][0]=='J':
                    if c[i]=='JUMP' and (c[i+1].split(','))[1][:-1]=='0:19':
                        res+=codes["JUMP_L"]
                    elif c[i]=='JUMP' and (c[i+1].split(','))[1][:-1]=='20:39':
                        res+=codes["JUMP_R"]
                    elif c[i]=='JUMP+' and (c[i+1].split(','))[1][:-1]=='0:19':
                        res+=codes["JUMP+_L"]
                    elif c[i]=='JUMP+' and (c[i+1].split(','))[1][:-1]=='20:39':
                        res+=codes["JUMP+_R"]
                    res+=N_to_B(c[i+1].split(',')[0][2:])
                else:
                    res+=codes[c[i]]
                    res+=N_to_B(c[i+1][2:-1])
                res+=" "
        elif len(c) > 1:
            i = 0
            for j in range(2):
                if c[i]=='HALT':
                    res+=codes[c[i]]
                    res+=N_to_B('0')
                    i=1
                elif c[i]=='NOP':
                    res+=codes[c[i]]
                    res+=N_to_B('0')
                    i=1
                else:
                    if c[i][0]=='J':
                        if c[i]=='JUMP' and (c[i+1].split(','))[1][:-1]=='0:19':
                            res+=codes["JUMP_L"]
                        elif c[i]=='JUMP' and (c[i+1].split(','))[1][:-1]=='20:39':
                            res+=codes["JUMP_R"]
                        elif c[i]=='JUMP+' and (c[i+1].split(','))[1][:-1]=='0:19':
                            res+=codes["JUMP+_L"]
                        elif c[i]=='JUMP+' and (c[i+1].split(','))[1][:-1]=='20:39':
                            res+=codes["JUMP+_R"]
                        res+=N_to_B(c[i+1].split(',')[0][2:])
                    else:
                        res+=codes[c[i]]
                        res+=N_to_B(c[i+1][2:-1])
                    i=2
                res+=" "
        else:
            res+=N_to_B_D(c[0])
        with open("binary.text","a") as f1:
            f1.write(res+'\n')