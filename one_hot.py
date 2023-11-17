# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
# print(data.head())

# Преобразование в one-hot c get_dummies:
one_hot_encoded = pd.get_dummies(data['whoAmI']).astype(int)
result = pd.concat([data, one_hot_encoded], axis=1)

# Преобразование в one-hot без get_dummies:
mapp = {'robot': 0, 'human': 1}
data['human'] = data['whoAmI'].map(mapp)
data['robot'] = 1 - data['human']

print(result.head(), '\n', data.head())