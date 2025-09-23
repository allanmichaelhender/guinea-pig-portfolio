from urllib.request import urlopen
import json

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

datefrom = "2015-01-01"
dateto = "2025-09-01"

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def create_url(symbol,datefrom,dateto,apikey):
    return "https://financialmodelingprep.com/stable/historical-price-eod/full?" + f"apikey={apikey}" + f"&from={datefrom}" + f"&to={dateto}" + f"&symbol={symbol}"
    
    
FTSE_url = create_url('^FTSE',datefrom,dateto,API_KEY)
SNP500_url = create_url('^GSPC',datefrom,dateto,API_KEY)
NIKKEI225_url = create_url('^N225',datefrom,dateto,API_KEY)


FTSE_data_raw = get_jsonparsed_data(FTSE_url)
SNP500_data_raw = get_jsonparsed_data(SNP500_url)
NIKKEI225_data_raw = get_jsonparsed_data(NIKKEI225_url)

def create_list_of_data(data):
    data_tuples = []
    for x in data:
        new_row = (x['date'], x['open'], x['high'], x['low'], x['close'], x['volume'], x['change'], x['changePercent'])
        data_tuples.append(new_row)
    return data_tuples

FTSE_data = create_list_of_data(FTSE_data_raw)
SNP500_data = create_list_of_data(SNP500_data_raw)
NIKKEI225_data = create_list_of_data(NIKKEI225_data_raw)

