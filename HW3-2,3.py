from pymongo import MongoClient
import json
import pandas as pd

client = MongoClient('localhost', 27017)
db = client['hh']
hh_vacancy = db.vacancy
ef fetch_vacancy_by_salary(min_salary):
    return list(hh_vac.find({'$or':  ({'Минимальная зарплата': {'$gt': min_salary}},
                                      {'Максимальная зарплата': {'$gt': min_salary}}
                                     )
                             }))
fetch_vacancy_by_salary(150000)[:20]

def add_to_db_only_new_items(vacancy :dict):
    find_condition = {'Ссылка': vacancy['Ссылка']}
    elements_for_update = vacancy
    elements_for_update.pop('Ссылка')
    elements_for_update = {'$set': elements_for_update}
    # Кладем в метод
    result_update = hh_vac.update_one(find_condition, elements_for_update)
    result_matched = result_update.matched_count
    if result_matched == 0:
        hh_vac.insert_one(vacancy)
        return 1
    return 0
with open('result.json') as file:
    vacancies = json.loads(file.read())
df = pd.DataFrame(vacancies).fillna('')

vacancies = []
for ind in df.index:
    vacancies.append(df.loc[ind].to_dict())
%%time
cnt = 0
for vac in vacancies:
    cnt += add_to_db_only_new_items(vacancy=vac)
print(f'Добавлено {cnt} новых элементов')