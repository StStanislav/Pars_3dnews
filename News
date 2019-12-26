#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time


Api = 'https://3dnews.ru/'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/cMCIlvY3aJFHAY6C1bllqDBbPev0cIPfg5QXEWIuXr5'

def post_ifttt_webhook(value):
    value = '<br>'.join(value)
    data = {'value1': value}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format('News')
    requests.post(ifttt_event_url, json=data)

def html_put(): 
    req = requests.get(Api)
    req.encoding = 'utf8'
    html = req.content
    soup = BeautifulSoup(html,'lxml')
    return soup

'''def history_f():
    historys = []
    soup = html_put(Api)
    x=0
    for x in soup.find_all('div',attrs = {'class':'allnews-col lncol'}):
        for one in x.find_all('li',attrs= {'class':"header"}):
            text = one.find('a').text
            site = one.find('a',attrs='').get('href') 
            date = one.find(attrs={'class':"date"}).text
            if str(site[0:5]) in 'https':
                history = '{}: <b>{}</b> {}'.format(date, site, text)
            else:
                history = '{}: <b>{}</b> {}'.format(date, 'https://3dnews.ru/'+site, text)
            
            historys.append(history)
            '<br>'.join(historys)
    ''' # не работает падла =)

def format_f():
    soup = html_put()   
    rows=[]
    x=0
    for x in soup.find_all('div',attrs = {'class':'allnews-col lncol'}):
        for one in x.find_all('li',attrs= {'class':"header"}):
            text = one.find('a').text
            site = one.find('a',attrs='').get('href') 
            date = one.find(attrs={'class':"date"}).text
            if str(site[0:5]) in 'https':
                row = '<b>{}</b>: {} - {}'.format(date, site, text)
            else:
                row = '<b>{}</b>: {} - {}'.format(date, 'https://3dnews.ru/'+site, text)
            rows.append(row)
    return '<br>'.join(rows)

def main():
	while True:
	    rows = format_f()
	    rows = rows.split('<br>')
	    x = int(len(rows)/2)
	    post_ifttt_webhook(rows[0:x])
	    post_ifttt_webhook(rows[x:len(rows)+1])

	    time.sleep(60*60*8)

if __name__ == '__main__':
    main()
