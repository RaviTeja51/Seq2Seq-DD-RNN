PATH = "/home/raviteja/ibm_sandhi/sanskrit_sandhi_corpus-master/"
list_of_files = ["combined_inp","combined_out"]

for file in list_of_files:
    with open(PATH+file+".txt") as f:
        text = f.readlines()
    with open(PATH+file+"_num.txt","w") as f:

        for line in text:
            ans = []
            for char in line.strip("\n"):
                if char != "+":
                    ans.append(str(int(hex(ord(char))[-2:],16)+1))
                else:
                    ans.append("129")
            f.write(",".join(ans)+"\n")
