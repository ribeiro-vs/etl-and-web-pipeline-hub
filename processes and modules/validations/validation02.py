import pandas as pd
from reports import GReport24
from verifiers import send_message

path= GReport24().default_destination_path[0]

df    = pd.read_csv(path)
print(df.columns)
df    = df[['Cupones aun no classificados']]
dfcol = df['Cupones aun no classificados']

lines = [
dfcol.iloc[0],
dfcol.iloc[1],
dfcol.iloc[2],
dfcol.iloc[3],
dfcol.iloc[4],
dfcol.iloc[5]
] 

message = """
Hola <!channel>, lamentablemente tenemos estos cupones que requieren clasificación:
"""
subtext = []

ignore_list=['Nenhum','Cupom']

for line in lines:
    if line not in ignore_list and pd.isna(line) == False :
        subtext.append('    - '+line)
    else:
        pass

final_message = message + '\n'.join(subtext)

if subtext:
    send_message(final_message,'mx-classificación-cupones')
else: 
    pass