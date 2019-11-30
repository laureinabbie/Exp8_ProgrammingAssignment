import pandas as pd
sasakyan = pd.read_csv('cars.csv')
kotse = pd.DataFrame
odd = sasakyan.iloc[0:5,0::2]
car1 = sasakyan.loc[[0]]
Car2 = sasakyan.loc[[23],['Model','cyl']]
c = sasakyan.loc[[1,28,18],['Model','cyl','gear']]