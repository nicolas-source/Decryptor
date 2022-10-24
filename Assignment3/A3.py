from hashlib import sha256
import requests

hash_of_preceding_coin = "a9c1ae3f4fc29d0be9113a42090a5ef9fdef93f5ec4777a008873972e60bb532"
# id_of_miner = sha256("1")

input_ = "1"
id_of_miner = sha256(input_.encode('utf-8')).hexdigest()
print("id_of_miner")
print(id_of_miner)

coin_blob = "0000"  # we need to find this that satisfies the hash
a = sha256(("CPEN 442 Coin" + "2022" + hash_of_preceding_coin + coin_blob + id_of_miner).encode('utf-8')).hexdigest()

print("a")
print(a)

# Need to verify with http://cpen442coin.ece.ubc.ca/verify_example_coin
url = "http://cpen442coin.ece.ubc.ca/verify_example_coin"

def verify_coin(coin_blob, id_of_miner):
    data = {
        "coin_blob": coin_blob,
        "id_of_miner": id_of_miner
    }

    response = requests.post(url, json=data)
    print("Verification result: " + response + "\n")