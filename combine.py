list_of_files = ["astadhyayi.txt","bhagvadgita.txt","literature.txt","uoh.txt"]
PATH = "/sanskrit_sandhi_corpus-master/"

with open(PATH+"combined_inp.txt","w") as f, open(PATH+"combined_out.txt","w") as g:
    for file in list_of_files:
        file_path = PATH+file
        with open(file_path) as h:
            text = h.readlines()

        for line in text:
            inp,out = line.split(",")
            f.write(inp.replace(" ","")+"\n")
            g.write(out.replace(" ",""))
