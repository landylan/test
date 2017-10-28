import csv, json

filename = u'IV'

with open(u'static/data/'+filename+'.csv', encoding = 'utf8') as f:
  reader = csv.DictReader(f)
  data = list(reader)
  
  # print(attr)
  
with open(u'static/data/'+filename+'.json', 'w') as f:
  json.dump(data,f)
  
with open(u'static/data/'+filename+'.json') as f:
  read_data = json.load(f)
  
  print(read_data)