import argparse
import sys
from trading.loopring_rest_sample import LoopringRestApiSample
from time import sleep

loopring_exported_account = {
    "exchangeName"    : "LoopringDEX: Beta 1",
    "exchangeAddress" : "0x944644Ea989Ec64c2Ab9eF341D383cEf586A5777",
    "exchangeId"      : 2,
    "accountAddress"  : "USER'S account address",
    "accountId"       : 1234,
    "apiKey"          : "USER'S api key",
    "publicKeyX"      : "USER's publicKeyX",
    "publicKeyY"      : "USER's publicKeyY",
    "privateKey"      : "USER's privateKey"
}

if __name__ == "__main__":
    # Connect the account
    loopring_rest_sample = LoopringRestApiSample()
    loopring_rest_sample.connect(loopring_exported_account)

    # Specify order params
    pair = "LRC-USDT"
    base_token, quote_token = pair.split("-")
    buy = True
    price = 0.18 # Make sure the price is lower than the current mid price
    volume = 50 # base_token
    nr_of_orders_to_create = 3

    # Build orders
    orders = []
    for _ in range(nr_of_orders_to_create):
        order_params = loopring_rest_sample.create_order_params(base_token, quote_token, buy, price, volume)
        orders.append(order_params)

    loopring_rest_sample.submit_multiple_orders(orders)
    sleep(5)



