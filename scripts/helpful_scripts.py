from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENT = ['mainnet-fork','mainnet-fork-dev']
LOCAL_BLOCK_ENVIRONMENTS = ['development','ganache-local']
DECIMALS= 8
INICIAL_VALUE = 200000000000

def get_account():
    if network.show_active() in LOCAL_BLOCK_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENT:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]['from_key'])

def deploy_mocks():
    print(f"the active network is {network.show_active}")
    print('deploying mocks...')
    if len(MockV3Aggregator)<=0:
        MockV3Aggregator.deploy(18, Web3.toWei(2000,"ether"), {'from':get_account()})
    print('mocks deployed')