#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import datetime
# "name": "bitcoin",
# "symbol": "BTC",
# "price": 8479.55536524,
# "high": 9035.32025454,
# "low": 8408.00329598,
# "timestamps": 1526095815874,
# "volume": 873630.8683,
# "change_hourly": -0.0022,
# "change_daily": -0.0534,
# "change_weekly": -0.1315,
# "change_monthly": 0.2224

def getPriceContent(data):
    price = data['price']
    high = data['high']
    low = data['low']
    symbol = data['symbol']
    volume = data['volume']
    change_hourly = data['change_hourly']
    change_daily = data['change_daily']
    change_weekly = data['change_weekly']
    change_monthly = data['change_monthly']
    currentTime = datetime.datetime.fromtimestamp(data['timestamps']/1000).strftime('%Y-%m-%d %H:%M:%S')

    content = '         💲{}最新行情💲: \n' \
              '——————————————\n'\
              '💡最新价格：{:.2f}\n' \
              '💡24小时最低价格：{:.2f}\n' \
              '💡24小时最高价格：{:.2f}\n' \
              '💡24小时交易量：{:.2f}\n'\
              '💡一小时内价格变化：{:.2%}\n' \
              '💡一天内价格变化：{:.2%}\n' \
              '💡一周内价格变化：{:.2%}\n' \
              '💡一月内价格变化：{:.2%}\n' \
              '更新于：{}'.format(symbol,
                                                price, low, high, volume,
                                                change_hourly, change_daily,
                                                change_weekly, change_monthly,
                                                currentTime)

    return content

def removeAtNickName(content, nickName):
    if (content != None and len(content) != 0):
        return str(content).replace('@'+nickName,'')
