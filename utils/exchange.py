
from utils.lbank import get_trading_depth as depth, orderBatch as orders
from utils.bitmartdata import get_trading_depth as depth2, orderBatch as orders2


def get_trading_depth(pair, exchange):
    if exchange == "1":
        return depth(pair=pair)
    if exchange == "2":
        return depth2(pair=pair)


def exchangeOrder(data, api_key, private_key, acton, exchange, priority,memo, self):
    if exchange == "1":
        return orders(data, api_key, private_key, acton, priority, self)
    if exchange == "2":
        return orders2(data, api_key, private_key, acton, priority, memo , self)
