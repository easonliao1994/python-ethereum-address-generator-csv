import os
import csv
from ethereum.utils import privtoaddr, checksum_encode, sha3

def generate_ethereum_addresses(n):
    addresses = []
    for _ in range(n):
        key = sha3(os.urandom(4096))
        address = checksum_encode(privtoaddr(key))
        private_key = key.hex()
        addresses.append([address, private_key])
    return addresses

n = int(input("Enter the number of addresses to generate: "))
addresses = generate_ethereum_addresses(n)

filename = "ethereum_addresses.csv"
with open(filename, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Address", "Private Key"])
    csvwriter.writerows(addresses)

print(f"Generated Ethereum addresses saved to {filename}.")
