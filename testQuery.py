import sqlite3 as sl

con = sl.connect('crypto.db')
json_ds = []


with con:
    ds = con.execute("SELECT * FROM cryptocurrency")
    for row in ds:
      json_dict = {'id': row[0], 'name': row[1], 'price': row[2], 'volume_24h': row[3],'timestamp': row[4]}
      json_ds.append(json_dict)
      print(row)
    
    print('Data: ')
    print(json_ds)