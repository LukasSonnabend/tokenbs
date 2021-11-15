import sqlite3
import datetime
import time
# Datenbank erstellen+verbinden
conn = sqlite3.connect('lubos.db')
c = conn.cursor()

# delete old shit
f = open("newscript.txt", "w")
f.write("")
f.close()
# prepare write
f = open("newscript.txt", "a")



# ADD token_identifier, Problem: Multiple tokens can have the same ID (e.g. RARIBLE LIRONEL)
c.execute('UPDATE trades SET token_identifier = nft_contract_address + nft_token_id')

# Get distinct collections
c.execute('SELECT DISTINCT nft_contract_address FROM trades')
distinct_collections = c.fetchall()
count = 0
collection_count = 0
result = []
start_time = time.time()
# get dataset for one collection
for collection in distinct_collections:
    data = c.execute('SELECT seller, buyer, token_identifier, usd_amount, block_time, token_identifier_test FROM trades WHERE nft_contract_address = ? ORDER by block_time LIMIT 250000', (collection))
    collection_count += 1
    # iterate through this collection (data variable saved in memory)

    allRows = []
    tradesDictBuyers = {}
    tradesDictSeller = {}

    # check if key already exists if not add to array buyers object
    for row in data:
        if row[1] in tradesDictBuyers:
            tradesDictBuyers[row[1]].append(row)
        else:
            tradesDictBuyers[row[1]] = [row]
        
        if row[0] in tradesDictSeller:
            tradesDictSeller[row[0]].append(row)
        else:
            tradesDictSeller[row[0]] = [row]

    count = 0
    for key, values in tradesDictBuyers.items():
        # key = unique buyer address
        buyer_id = key
        # find buyer as seller  in tradesDictSeller
        if buyer_id in tradesDictSeller:
            # iterate through all sales of the buyer check if they reference the same token_identifier_test
            buysOfBuyer = tradesDictBuyers[buyer_id]
            salesOfBuyer = tradesDictSeller[buyer_id]
            seller_id = tradesDictSeller[key][0][0]
            for i in range(0, len(salesOfBuyer)):
                token_id_sale = salesOfBuyer[i][5]
                for j in range(0, len(values)):
                    token_id_buy = values[j][5]
                    if token_id_buy == token_id_sale:
                        print("Buyer: " + str(key) + " resold token " + str(values[j][5]) + " to " + str(tradesDictSeller[key][i][1]))
                        print("BuyTransaction: " + str(values[j]) + "\nSellTransaction: " + str(salesOfBuyer[i]) + "\n")
                        count += 1
                        break
    print(count)
    
    # testing only break after one collection
  #  break


f.close()

print("--- %s seconds ---" % (time.time() - start_time))





