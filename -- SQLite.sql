


-- select seller, buyer, token_identifier, nft_token_id, tx_hash, nft_contract_address, token_identifier_test from trades
-- where token_identifier_test ='\xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb3614'
-- Limit 500;


-- -- Create token_identifier_test column

--ALTER TABLE trades ADD COLUMN token_identifier_test VARCHAR(200);
-- delete from trades
-- where [nft_token_id] is null

--UPDATE trades SET token_identifier_test = (nft_contract_address || nft_token_id || '_' ||ttoken_identifier_test



-- verify 18 stück
-- SELECT seller, buyer, token_identifier, usd_amount, block_time, token_identifier_test FROM trades WHERE nft_contract_address = '\xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb' ORDER by block_time LIMIT 50

