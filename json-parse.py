import json
import re

with open('pkm-names.txt') as f:
    pknames = [line.rstrip() for line in f]

with open('scraper-output.json', encoding="utf8") as f:
    data = json.load(f)

cndict = dict(zip([entry["name"] for entry in data],[entry["cn"] for entry in data]))

with open("pkm-dict.txt", mode='w', encoding="utf8",) as f:
    for entry in data:
        name = entry["name"]
        desc = entry["desc"][0]
        desc = re.sub(r" *<[^>]*?title=\\\"([\w\s]*)\\[^>]*?> *", r" \1 ", desc)
        desc = re.sub(r"<[^>]*>", r"", desc)
        cn = re.findall(r"[> ]([^ ]*?) (?![^ ]+ )", entry["cn"][0])[0]
        f.write(f"{cn}\t\t{name} {desc}")

# desc = [cndict[pk] for pk in pknames]
# print(desc)#

# with open("descriptions.txt", mode='w', encoding="utf8",) as f:
#     for line in desc:
#         f.write(line[0])
