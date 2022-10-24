from hashlib import sha256
import base64
import datetime as dt

hash_of_preceding_coin = "a9c1ae3f4fc29d0be9113a42090a5ef9fdef93f5ec4777a008873972e60bb532"

input_ = "1"
id_of_miner = sha256(input_.encode('utf-8')).hexdigest()


print("Hash")
print(id_of_miner)

start_time = dt.datetime()
time_took = []
for i in range (0x0, 0x100000):
    coin_blob = str(i)
    a = sha256(("CPEN 442 Coin" + "2022" + hash_of_preceding_coin + coin_blob + id_of_miner).encode('utf-8')).hexdigest()
    if a.startswith("000000"):
        end_time = dt.datetime()
        time_took.push((end_time - start_time).total_seconds())
        print("Mining this coin took: " + end_time-start_time)
        print("hash value")
        print(a)
        print("coin blob")
        b = base64.b64encode(bytes(coin_blob, 'utf-8')) # bytes
        base64_str = b.decode('utf-8') # convert bytes to string
        print(base64_str)
    start_time = dt.datetime()
        
print("the average amount of time it takes to mine a coin is ")
        