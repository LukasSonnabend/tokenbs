#old table gets dropped
#remember to add token_identifier
import sqlite3
import pandas

conn=sqlite3.connect("lubos.db")
c = conn.cursor()

c.execute('DROP TABLE trades')


#DATA types NULL, INTEGER, REAL, TEXT
c.execute('''CREATE TABLE IF NOT EXISTS trades (
        block_time text,
        nft_project_name text,
        nft_token_id text,
        erc_standard text,
        platform text,
        platform_version text,
        trade_type text,
        number_of_items text,
        category text,
        evt_type text,
        usd_amount text,
        seller text,
        buyer text,
        original_amount text,
        original_amount_raw text,
        original_currency text,
        original_currency_contract text,
        currency_contract text,
        nft_contract_address text,
        exchange_contract_address text,
        tx_hash,
        block_number text,
        nft_token_ids_array text,
        senders_array text,
        recipients_array text,
        erc_types_array text,
        nft_contract_addresses_array text,
        erc_values_array text,
        tx_from text,
        tx_to text,
        trace_address text,
        evt_index text,
        trade_id text,
        leer text
    )''')


#read data into the table
for i in list(range(0,5)):
    file=str(i)+'00-'+str(i+1)+'00.csv'
    df=pandas.read_csv(file)
    df.to_sql('trades', conn, if_exists='append', index=False)

c.execute('ALTER TABLE trades ADD COLUMN token_identifier')


#Commit and close connection
conn.commit()
conn.close()


