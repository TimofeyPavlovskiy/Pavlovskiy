users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

Common = len(users)
UniqueUsers = set(users)
UniqueUsersLengh = len(UniqueUsers)

Beginning = 0

dict_ = {"Общее количество": 0,
     "Уникальные посещения": 0
     }

dict_["Общее количество"] = Common
dict_["Уникальные посещения"] = UniqueUsersLengh

print(dict_)
