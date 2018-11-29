#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import threading
import requests





def updatePriceDict():
    try:
        global name_dict
        global symbol_dict
        url = "http://data.block.cc/api/v1/price"
        response = requests.get(url, ).json()
        # print(json.dump(response, indent=2))
        dataArray = response['data']
        temp_name_dict = dict()
        temp_symbol_dict = dict()
        for data in dataArray :
            name = str(data['name']).upper()
            symbol = str(data['symbol']).upper()
            temp_name_dict[name] = data
            temp_symbol_dict[symbol] = data
        name_dict = temp_symbol_dict
        symbol_dict = temp_symbol_dict
    except Exception as e:
        print(str(e))
    global timer
    timer = threading.Timer(60, updatePriceDict)
    timer.start()


def getLatestInfo(code):
    name = str(code).upper().strip()
    try:
        if (name_dict == None or symbol_dict == None):
            return None
        if (name in  name_dict.keys()):
            return name_dict[name]
        elif  (name in symbol_dict.keys()):
            return symbol_dict[name]
        else:
            return None
    except:
        return None