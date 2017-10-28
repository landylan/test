import csv, json

filename = u'升級所需星魄元丹'

with open(u'static/data/'+filename+'.csv', encoding = 'utf8') as f:
  reader = csv.DictReader(f)
  data = list(reader)
  
# csv 讀出來的都是字串，要自己把一些欄位轉成適當的格式（據說 Pandas 比較聰明）
for d in data:
  # IV
  # d['iv_sum'] = int(d['iv_sum'])
  
  # 元神
  '''
  d['id'] = int(d['id'])
  # d['rank'] = int(d['rank'])
  d['CP40'] = int(d['CP40'])
  d['HP_SQRT_LV'] = float(d['HP_SQRT_LV'])
  # d['skill_value'] = int(d['skill_value'])
  '''
  
  # 屬性
  # d['id'] = int(d['id'])
  
  # 我的元神
  '''
  if d['no.'].isnumeric(): d['no.'] = int(d['no.'])
  if d['id'].isnumeric(): d['id'] = int(d['id'])
  if d['CP'].isnumeric(): d['CP'] = int(d['CP'])
  if d['HP'].isnumeric(): d['HP'] = int(d['HP'])
  if d['IV'].isnumeric(): d['IV'] = int(d['IV'])
  if d['upgrade_spirit'].isnumeric(): d['upgrade_spirit'] = int(d['upgrade_spirit'])
  if d['upgrade_candy'].isnumeric(): d['upgrade_candy'] = int(d['upgrade_candy'])
  d['Level'] = float(d['Level'])
  if d['skill1_value'].isnumeric(): d['skill1_value'] = int(d['skill1_value'])
  # d['skill1_2_times'] = int(d['skill1_2_times'])
  if d['skill2_value'].isnumeric(): d['skill2_value'] = int(d['skill2_value'])
  if d['STAB1'].isnumeric(): d['STAB1'] = float(d['STAB1'])
  if d['STAB2'].isnumeric(): d['STAB2'] = float(d['STAB2'])
  if d['CP1'].isnumeric(): d['CP1'] = float(d['CP1'])
  if d['CP40'].isnumeric(): d['CP40'] = int(d['CP40'])
  if d['HP_SQRT_LV'].isnumeric(): d['HP_SQRT_LV'] = float(d['HP_SQRT_LV'])
  # if d['skill1_value'].isnumeric(): d['Average_Att'] = float(d['Average_Att'])
  '''
  
  # 升級所需星魄元丹
  if d['Level'].isnumeric(): d['Level'] = float(d['Level'])
  if d['upgrade_spirit'].isnumeric(): d['upgrade_spirit'] = int(d['upgrade_spirit'])
  if d['upgrade_candy'].isnumeric(): d['upgrade_candy'] = int(d['upgrade_candy'])
  
  
  # print(attr)
  
with open(u'static/data/'+filename+'.json', 'w') as f:
  json.dump(data,f)
  
with open(u'static/data/'+filename+'.json') as f:
  read_data = json.load(f)
  
  print(read_data)