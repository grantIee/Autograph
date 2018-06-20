#!/usr/bin/env python3
"""
    api.py
    2 May 2018

"""
import subprocess
import sys
import argparse
import json
import urllib.request
import urllib.parse
import base64

def get_new_block():
    api_url_base = "https://blockchain.info/q/latesthash"
    request = urllib.request.Request(api_url_base)
    data = urllib.request.urlopen(request).read()
    string_from_server = data.decode('utf-8')
    return string_from_server

def get_block_details(block_hash):
    api_url_base = "https://blockchain.info/rawblock/{0}"
    url = api_url_base.format(block_hash)
    request = urllib.request.Request(url)
    data = urllib.request.urlopen(request).read()
    string_from_server = data.decode('utf-8')
    data_list = json.loads(string_from_server)
    results_list = []
    data_list = data_list['tx'] 
    for tx_dictionary in data_list:
        time = tx_dictionary['time']

    return string_from_server
    

def main(args):

    if args.request == 'transactions':
        latest_hash = get_new_block()
        block = get_block_details(latest_hash)
        print(block)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get Information on blockchain')

    request = parser.add_argument('request',
                        help='request a information about a blockchain',
                        choices=['transactions', 'top', 'search'])

    args = parser.parse_args()

    requiredNamed = parser.parse_args()

    main(args)    
