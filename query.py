import sqlite3

conn=sqlite3.connect(r'C:\Users\klein\Documents\DATABASE\data.db')
c = conn.cursor()

#Is returned as a Python list
c.execute('SELECT COUNT(tx_hash) FROM trades')
#c.execute('UPDATE trades SET token_identifier = nft_contract_address || nft_token_id')
#c.execute('SELECT DISTINCT category from trades')
#lol=c.execute('SELECT COUNT(DISTINCT nft_contract_address) FROM trades')
#c.execute('SELECT block_time FROM trades LIMIT 100')
items = c.fetchall()
print(items)
#print(lol)