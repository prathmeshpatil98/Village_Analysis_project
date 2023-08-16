
import gspread
import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

gc = gspread.service_account(filename="DSSheetprathmesh.json")
wks = gc.open("ProjectWorkDS").worksheet("ALLDATA")
values = wks.get_all_values()

headers = values[0]
df = pd.DataFrame(values[1:], columns=headers)
df

#familyhead = df.iloc[1,1:14]
#familyhead