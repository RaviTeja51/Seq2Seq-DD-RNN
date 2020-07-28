import re
import os


PATH = "/home/raviteja/ibm_sandhi/Nalacharitham/Nalacharitham"

# get all the files from the folder
files = os.listdir(PATH)

# sanskrit words range from \u900 - \u97F
begin = ord("ऀ") # integer equivalent of  \u900
end = ord("ॿ")   # integer equivalent of \u097F


Words = []
for i in files:
    with open(PATH+f"/{i}") as f:
        file = f.readlines()[16:]
        for line in file:
            ans = []
            for char in line:
                if begin <= ord(char) <= end and char != "।":
                    ans.append(char)
                else:
                    if ans:
                        Words.append("".join(ans))
                        ans = []
print(len(Words))
Words = "\n".join(Words)
with open(PATH+"combined.txt","w") as f:
    for i in Words:
        f.write(i)
