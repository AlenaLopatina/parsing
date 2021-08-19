from pymongo import MongoClient
import json
import pandas as pd

client = MongoClient('localhost', 27017)
db = client['hh']
hh_vacancy = db.vacancy

with open('hh.json') as file:
    all = json.loads(file.read())
df = pd.DataFrame(all).fillna('')
all = []
for i in df.index:
    all.append(df.loc[i].to_dict())
hh_vacancy.insert_many(all)