import json

from sqlalchemy import create_engine, Column, Float, Integer, String, Enum
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine(u'sqlite:///英雄夢.db', echo=False)

class Iv(Base):
  __tablename__ = 'iv'
  
  iv = Column(String, primary_key=True)
  iv_sum = Column(Integer)
  
  def __repr__(self):
    return u"資質：%s ==> IV和：%s"%(self.iv, self.iv_sum)
    
'''
Iv.metadata.create_all(engine, checkfirst=True)  # 建立 table

# 從 json 檔案讀取資料
filename = u'IV'
with open(u'static/data/'+filename+'.json') as f:
  # read_data = json.load(f)  # 變成 list
  read_str = f.read()

# print(read_str)
  
# 從 json 轉為 dict
read_data = json.loads(read_str)

# print(read_data)
#'''

# 建立 session
Session = sessionmaker(bind=engine)
session = Session()

'''
# 將所有資料寫入資料庫
iv_rows = [Iv(**i) for i in read_data]
# print(iv_rows)

session.add_all(iv_rows)
session.commit()
#'''

print(u"資料列數：%i\n"%session.query(Iv).count())

q88 = session.query(Iv).filter(Iv.iv_sum > 30)
print(list(q88))

def inst2dict(inst, delete_id=False):
  dat = {}
  for column in inst.__table__.columns:
    dat[column.name] = getattr(inst, column.name)
  if delete_id:
    dat.pop('id')
  return dat
  
q_result = [inst2dict(q) for q in q88]
print(q_result)
