import pandas as pd


# 直接讀取 json 檔案
# df = pd.read_json(u'static/data/元神.json')

# 直接讀取 csv 檔案
df = pd.read_csv(u'static/data/元神.csv', encoding='utf-8') # 後面可加參數 sep='|', names=['name', 'cattegory'], skipinitialspace=True, quotechar="`"

df.replace(u'\xa0',u'', regex=True, inplace=True)

print(df.head())
print(df.columns)
print(df.index)
print(df.loc[134])
df = df.set_index('name')
print(df.loc[u'戰神呂布'])
print(df.ix[u'戰神呂布'])
print(df.ix[134])
df = df.reset_index()
print(df.iloc[134])

# 把 dataframe 存成 json 檔案（groupby 之後，to_json會有問題。。。）
json = df.to_json(u'static/data/元神-2.json', orient='records') # [split, records, index, columns, values]

df = df.sort_values(by='CP40', ascending=0)
df1 = df.groupby('attr1')
df2 = df.groupby('attr2')

# 按照屬性分組，存到 Excel 檔案的各屬性工作表中
print(df2.groups.keys())
with pd.ExcelWriter(u'static/data/各屬性元神.xlsx') as writer:
  for field in df2.groups.keys():
    df_tmp = pd.concat([df1.get_group(field),df2.get_group(field)]).sort_values(by='CP40', ascending=0)
    df_tmp.to_excel(writer, sheet_name=field)
    '''
    print('\n\n'+field)
    print(df_tmp.head())
    # print(df2.get_group(field).head(5))
    '''

df = pd.read_excel(u'static/data/各屬性元神.xlsx', sheetname=None, parse_cols=[0,1,2,4,8,9,10,11])  # 這樣才會讀入所有工作表，並只讀入指定欄位
print(df)
