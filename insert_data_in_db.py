import pandas as pd
from sqlalchemy import Column, Date, DateTime, Integer, MetaData, String, Table, Text, Time, create_engine


metadata = MetaData()
engine = create_engine('postgresql://postgres:postgres@195.133.26.16:5432/postgres')

DeliveryRequests = Table(
    'DeliveryRequests', metadata,
    Column('InternalId', Integer, primary_key=True),
    Column('LoadDate', DateTime),
    Column('CustomerName', String(255)),
    Column('DeliveryCity', String(100)),
    Column('DeliveryAddress', String(255)),
    Column('DeliveryDate', Date),
    Column('DeliveryTime', Time),
    Column('PackageType', String(50)),
    Column('Comment', Text)
)

DeliveryStatusCurrent = Table(
    'DeliveryStatusCurrent', metadata,
    Column('InternalId', Integer, primary_key=True),
    Column('LoadDate', DateTime),
    Column('StatusName', String(255)),

)


DeliveryStatusHistory = Table(
    'DeliveryStatusHistory', metadata,
    Column('InternalId', Integer, primary_key=True),
    Column('LoadDate', DateTime, primary_key=True),
    Column('StatusName', String(255))
)

metadata.create_all(engine)

csv_file = 'DeliveryData.csv'
df = pd.read_csv(csv_file, delimiter=';', quotechar='"')
df.to_sql('DeliveryRequests', engine, index=False, if_exists='replace')

csv_file = 'DeliveryData 2.csv'
df = pd.read_csv(csv_file, delimiter=';', quotechar='"')
df.to_sql('DeliveryStatusCurrent', engine, index=False, if_exists='replace')

csv_file = 'DeliveryData 3.csv'
df = pd.read_csv(csv_file, delimiter=';', quotechar='"')
df.to_sql('DeliveryStatusHistory', engine, index=False, if_exists='replace')

