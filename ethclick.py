import requests
import json
import datetime
from clickhouse_driver import Client

def eth_blockNumber(url):
    headers = {'content-type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 0
    }
    print("--eth_blocknumber---")
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    blockNumberI = int(response["result"],16)
    blockNumberH = hex(blockNumberI)
    print("eth_blockNumber : ", blockNumberI)
    eth_getBlockByNumber(url, blockNumberH)

def eth_getBlockByNumber(url, block):
    headers = {'content-type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [block, True],
        "id": 0
    }
    print("--eth_getBlockByNumber---")
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    epoch_time =  (int(response['result']['timestamp'],16))
    timestamp = datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
    miner = str(response['result']['miner'])
    hash1 = str(response['result']['hash'])
    block_number = int(block,16)
    print(' - eth_blockNumber = ', block_number)
    print(' - miner0 = ', miner)
    print(' - timestamp = ' + timestamp)
    print(' - hash1 = ' + str(response['result']['hash']))

    add_data(block_number, epoch_time, miner, hash1)

def add_data(data1, data2, data3, data4):
    connection = Client(host='localhost')
    connection.execute(
        "INSERT INTO ethdb (*) VALUES", [{
            'numb': data1,
            'timestamp': data2,
            'miner': data3,
            'hash': data4
        }]
    )

if __name__ == "__main__":
    url = "http://localhost:8545"
    eth_blockNumber(url)