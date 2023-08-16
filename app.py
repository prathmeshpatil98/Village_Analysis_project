import gspread
import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

gc = gspread.service_account(filename="DSSheetprathmesh.json")
wks = gc.open("ProjectWorkDS").worksheet("ALLDATA")
values = wks.get_all_values()

headers = values[0]



df = pd.DataFrame(values[1:], columns=headers)
num_rows = df.columns
#print("Number of rows:", num_rows)
data = []
family = {} 

for i in range(len(df)):
    dfHead = df.iloc[i:i+1, range(15)]
    dfHome = df.iloc[i:i+1, 15:27]
    dfAnimals = df.iloc[i:i+1, 27:35]
    dfGeneral = df.iloc[i:i+1, 35:50]
    dfPersin1 = df.iloc[i:i+1, 50:65]
    dfPerson2 = df.iloc[i:i+1, 65:80]
    dfPerson3 = df.iloc[i:i+1, 80:95]
    
    family[df["कुटुंब प्रमुखाचे नावं "][i]] = {
        'dfHead': dfHead,
        'dfHome': dfHome,
        'dfAnimals': dfAnimals,
        'dfGeneral': dfGeneral,
        'dfPersin1': dfPersin1,
        'dfPerson2': dfPerson2,
        'dfPerson3': dfPerson3
    }

data.append(family) 
print(data)