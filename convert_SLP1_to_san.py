from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

list_of_files = ["astadhyayi.txt","bhagvadgita.txt","literature.txt","uoh.txt"]
PATH = "/home/raviteja/ibm_sandhi/sanskrit_sandhi_corpus-master/"

for file in list_of_files:
    file_path = PATH + file

    with open(file_path) as f:
        text = f.readlines()

    with open(file_path,"w") as f:
        for  line in text:
            f.write(transliterate(line, sanscript.SLP1, sanscript.DEVANAGARI))
