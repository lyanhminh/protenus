#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 18:51:24 2021
Given a url, this application polls a target web application for its status
@author: minhly
"""

import time
import requests

def poll(url, t=60):
    """Application main function to poll a website every t seconds for a given url
            Parameters:
                url (str): a website url string
                t (int): time between requests in seconds
    """
    while True:
        try:
            fetch(url)
            time.sleep(t)
        except:
            url = handle_exception(url)
            if url == '':
                break

    
def fetch(url):
    """Returns tuple pair of http response code and time required to make 
    request for a given input url string and prints them out to stdout
            Parameters:
                url (str): url string 
                
            Returns:
                2-tuple (requests.models.Response, float): http response, time to make fetch 
    """
    print(f'--------------------------------------------\ngetting {url}..')
    try:       
        tick = time.time()
        response = requests.get(url)
        response.raise_for_status()
        tock = time.time()
        fetch_time = tock-tick
        print(f'\nStatus code returned: {response.status_code}')
        print(f'Fetch time: {fetch_time}s\n')
        return (response, fetch_time)
    except requests.exceptions.HTTPError as errh:
        print ("\nHttp Error:")
        raise Exception
    except requests.exceptions.Timeout as to:
        print("\nTimeout Error")
        raise Exception
    except requests.exceptions.ConnectionError as errc:
        print("\nConnection Error")
        raise Exception
    except Exception:
        print("\nThat didn't work at all. Is your url correct? Did you forget to include the request protocol, http(s)?")
        raise Exception

def handle_exception(url):
    """Prompts user for action after an exception and returns back 
    appropriate url string
            Parameters:
                url (str): url string
                
            Returns:
                (str): appropriately mapped and formatted url string
    
    """
    user_input = input(f"1. Press enter to quit, \n2. 'r' to try pinging {url} again, or \n3. enter a new url:\n").strip()
    if user_input == 'r':
        return url
    return user_input

if __name__ == '__main__':
    url = input('Enter a url including the request protocol, eg. "http://localhost:8081": ')
    poll(url)