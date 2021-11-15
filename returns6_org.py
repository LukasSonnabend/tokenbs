import sqlite3
import sys
import time

#Datenbank erstellen+verbinden
conn=sqlite3.connect('lubos.db')
c = conn.cursor()

# delete old shit
f = open("oldscript.txt", "w")
f.write("")
f.close()
# prepare write
f = open("oldscript.txt", "a")



#ADD token_identifier, Problem: Multiple tokens can have the same ID (e.g. RARIBLE LIRONEL)
c.execute('UPDATE trades SET token_identifier = nft_contract_address + nft_token_id')

#Get distinct collections
c.execute('SELECT DISTINCT nft_contract_address FROM trades LIMIT 1')
distinct_collections=c.fetchall()
count=0
collection_count=0
result = []
start_time = time.time()
#get dataset for one collection
for collection in distinct_collections:
    data=c.execute('SELECT seller, buyer, token_identifier, usd_amount, block_time, token_identifier_test FROM trades WHERE nft_contract_address = ? ORDER by block_time LIMIT 18', (collection))
    collection_count += 1
    #iterate through this collection (data variable saved in memory)
    allRows = []
    for row in data:
        allRows.append(row)

    for i in range(0, len(allRows)):
        seller=allRows[i][0]
        token_identifier=allRows[i][5]
        #for every transaction iterate to find if there is a matching buy transaction, to be programmed: start iteration from current transaction backwards
        # for i in range(data.len, i, -1):
        for j in reversed(range(len(allRows)-i)):
#        for match in data:
            #only get the last sale, to be programmed!! what does break do?
            if allRows[j][1] == seller and allRows[j][5] == allRows[i][5]:
                f.write("Seller: " + str(allRows[i][0]) + ",Buyer: " + str(allRows[i][1]) + ",TokenID: " + str(allRows[i][5]) +  ",Block_time: " + str(allRows[i][4]) + "\n")
                f.write("Seller: " + str(allRows[j][0]) + ",Buyer: " + str(allRows[j][1]) + ",TokenID: " + str(allRows[j][5]) +  ",Block_time: " + str(allRows[j][4]) + "\n")
                ##f.write(str(allRows[j]))
                try:
                    #needed holding period, return, seller, buy tx_hash
                    usd_return=(float(allRows[i][3])-float( allRows[j][3]))/float(allRows[j][3])
                    result.append(usd_return)   
                    print(token_identifier)
                except Exception:
                    pass

                
                
                #print(usd_return)
                count += 1
                #print('my_sql_query_will_be_here')
                break
    print(collection_count)    
#print(result)        
    
    
            
#print(usd_return)   
print(count)
f.close()
print("--- %s seconds ---" % (time.time() - start_time))
