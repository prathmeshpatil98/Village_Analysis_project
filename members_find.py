
import gspread
import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

gc = gspread.service_account(filename="DSSheetprathmesh.json")
wks = gc.open("ProjectWorkDS").worksheet("ALLDATA")
values = wks.get_all_values()

headers = values[0]
df = pd.DataFrame(values[1:], columns=headers)

data = []
family_data = []

# for i in range(len(df)):
#     family_head = df.iloc[i, 1:14]  
#     family_data.append({
#         'family_head': family_head.tolist(),  
#     })

# data.extend(family_data)  

# data_df = pd.DataFrame(data)

# print(data_df)
familyhead = df.iloc[1,1:14]
familyhead