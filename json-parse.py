with open('pkm') as f:
    pknames = [line.rstrip() for line in f]

import json

with open('cn-pkmn.json', encoding="utf8") as f:
    data = json.load(f)

cndict = dict(zip([entry["name"] for entry in data],[entry["cn"] for entry in data]))

desc = [cndict[pk] for pk in pknames]
print(desc)#

with open("descriptions.txt", mode='w', encoding="utf8",) as f:
    for line in desc:
        f.write(line[0])