from brownie import config, FundMe, network, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCK_ENVIRONMENTS
from web3 import Web3



def deploy_FundMe():
    account = get_account()
    # pass the price feed address to our fundme contract
    
    #if we are on a persistent network like kovan, use the associated address
    #otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCK_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]['eth_usd_price_feed']
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        


    fund_me = FundMe.deploy(price_feed_address,{"from":account},publish_source=config['networks'][network.show_active()].get('verify'))
    print(f"contract deployed to{fund_me.address}")
    return fund_me

def main():
    deploy_FundMe()
    
