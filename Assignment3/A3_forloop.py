from hashlib import sha256
import base64
from datetime import datetime as dt
import requests

hash_of_preceding_coin = "a9c1ae3f4fc29d0be9113a42090a5ef9fdef93f5ec4777a008873972e60bb532"

input_ = "1"
id_of_miner = sha256(input_.encode('utf-8')).hexdigest()


print("public miner id")
print(id_of_miner)

time_took = []
start_time = dt.now()
for i in range (0x0, 0x10000000):
    coin_blob = str(i)
    a = sha256(("CPEN 442 Coin" + "2022" + hash_of_preceding_coin + coin_blob + id_of_miner).encode('utf-8')).hexdigest()
    if a.startswith("0000000"):
        end_time = dt.now()
        time_took.append((end_time - start_time).total_seconds() * 1000)
        print("hash value: " + a)
        print("coin blob: " + coin_blob)
        b = base64.b64encode(bytes(coin_blob, 'utf-8'))
        base64_str = b.decode('utf-8')
        print("encoded blob: " + base64_str)
        start_time = dt.now()
        
print("the average milisecond it takes to mine a coin is " + str(sum(time_took)/len(time_took)))




        