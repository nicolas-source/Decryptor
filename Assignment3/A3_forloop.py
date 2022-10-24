from hashlib import sha256
import base64
import datetime as dt
import requests

hash_of_preceding_coin = "a9c1ae3f4fc29d0be9113a42090a5ef9fdef93f5ec4777a008873972e60bb532"

input_ = "1"
id_of_miner = sha256(input_.encode('utf-8')).hexdigest()


print("public miner id")
print(id_of_miner)

time_took = []
for i in range (0x0, 0x100000):
    start_time = dt.datetime()
    coin_blob = str(i)
    a = sha256(("CPEN 442 Coin" + "2022" + hash_of_preceding_coin + coin_blob + id_of_miner).encode('utf-8')).hexdigest()
    if a.startswith("000000"):
        end_time = dt.datetime()
        time_took.push((end_time - start_time).total_seconds())
        print("hash value: " + a)
        print("coin blob: " + coin_blob)
        b = base64.b64encode(bytes(coin_blob, 'utf-8'))
        base64_str = b.decode('utf-8')
        print("encoded blob: " + base64_str)
    start_time = dt.datetime()
        
print("the average amount of time it takes to mine a coin is " + sum(time_took)/len(time_took))

url = "http://cpen442coin.ece.ubc.ca/verify_example_coin"

def verify_coin(coin_blob, id_of_miner):
    data = {
        "coin_blob": coin_blob,
        "id_of_miner": id_of_miner
    }

    response = requests.post(url, json=data)
    print("Verification result: " + response + "\n")
        