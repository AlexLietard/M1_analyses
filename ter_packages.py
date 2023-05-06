import regex as re
import pandas as pd

l = []
b = {}
with open("./packages.txt", mode = "r") as txt:
    for line in txt:
        a = line.split(sep = " ")
        for elem in a:
            print(elem)
            if elem == "" or re.search("\[\.\]", elem) == True or elem == "\n":
                pass
            else:   
                l.append(elem)

for pack in l:
    if re.search("\[", pack):
        l.remove(pack)

for pack in l:
    unpack = pack.split("_")
    unpack[1] = unpack[1].replace("\n", "")
    b[unpack[0]] = unpack[1]

df = pd.DataFrame.from_dict(data = b, orient = "index", columns= ["Version"])
df.index.name = "Bibliothèques"
df.to_csv("./data/packages.csv", sep = ";")
print(df)
