def main():
    with open("/home/raviteja/ibm_sandhi/sanskrit_sandhi_corpus-master/combined_inp.txt") as f:
        inp = f.readlines()

    with open("/home/raviteja/ibm_sandhi/sanskrit_sandhi_corpus-master/combined_out.txt") as g:
        out = g.readlines()

    with open("/home/raviteja/ibm_sandhi/sanskrit_sandhi_corpus-master/sandhi_pos.txt","w") as h:
        for i,j in zip(inp,out):
            ip = i.strip("\n")
            op = j.strip("\n")
            n = len(ip)
            m = len(op)
            max_split = op.count("+")
            l = 0
            k = 0
            count = 0
            ans = []
            while l < n and k < m:
                if ip[l] != op[k]:
                    count += 1
                    if count > max_split:
                        break
                    ans.append(str(l))
                    if op[k] != "+":
                        l += 1
                    while k < m and  op[k] != "+":
                        k += 1
                    if k< m and op[k]=="+" and op[k-1]=="्" and k+1 < m and op[k+1]=="अ":
                        k += 2
                    if k < m and op[k] == "+":
                        k += 1
                    temp1 = k
                    temp = l

                    while temp < l+3 and temp < n:
                        temp1 = k
                        while temp1 < k+2 and temp1 < m and  op[temp1] != ip[temp]:
                            temp1 += 1


                        if temp < n and temp1 < m and ip[temp] == op[temp1]:

                            break
                        temp += 1
                    if temp < n and temp1 < m and ip[temp] == op[temp1]:
                        l = temp+1
                        k = temp1+1
                    else:
                        l += 1
                        k += 1
                else:
                    l += 1
                    k += 1
            h.write(",".join(ans)+"\n")
if __name__ == '__main__':
    main()
