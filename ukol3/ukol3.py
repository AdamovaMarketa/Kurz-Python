import json
with open('body.json', encoding='utf-8') as input_file:
    pisemka_body = json.load(input_file)

pisemka_prospech = {}
for jmeno, pocet_bodu in pisemka_body.items():
    if pocet_bodu >= 60:
        pisemka_prospech[jmeno] = "Pass"
    else:
        pisemka_prospech[jmeno] = "Fail" 

with open("prospech.json", mode='w', encoding='utf-8') as output_file:
    #print(pisemka_prospech, file=output_file)
    json.dump(pisemka_prospech, output_file, ensure_ascii=False)

#BONUS

with open('bonusy.json', encoding='utf-8') as bonus_file:
    bonus_body = json.load(bonus_file)

for jmeno, bonus in bonus_body.items():
    if jmeno in pisemka_body:
        pisemka_body[jmeno] = bonus + pisemka_body[jmeno]
    else:
        pisemka_body[jmeno] = bonus

znamky = {}
for jmeno, pocet_bodu in pisemka_body.items():
    if pocet_bodu >= 90:
        znamky[jmeno] = "1"
    elif pocet_bodu >= 70:
        znamky[jmeno] = "2"
    elif pocet_bodu >= 50:
        znamky[jmeno] = "3"
    elif pocet_bodu >= 30:
        znamky[jmeno] = "4"
    else:
        znamky[jmeno] = "5"

with open("znamky.json", mode='w', encoding='utf-8') as output2_file:
    #print(znamky, file=output2_file)
    json.dump(znamky, output2_file, ensure_ascii=False)