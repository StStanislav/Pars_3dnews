#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time
from datetime import datetime
 
BITCOIN_PRICE_THRESHOLD = 10000
BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/cMCIlvY3aJFHAY6C1bllqDBbPev0cIPfg5QXEWIuXr5'
 
def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    return float(response_json[0]['price_usd'])  # Конвертирует курс в число с плавающей запятой
 
def post_ifttt_webhook(event, value):
    data = {'value1': value}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)  # Вставка желаемого события
    requests.post(ifttt_event_url, json=data)  # Отправка запроса HTTP POST в URL вебхука
 
def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')  # Форматирует дату в строку: '24.02.2018 15:09'
        price = bitcoin_price['price']
        # тег <b> делает текст полужирным
        row = '{}: $<b>{}</b>'.format(date, price)  # 24.02.2018 15:09: $<b>10123.4</b>
        rows.append(row)
 
    # Используйте тег <br> для создания новой строки
    return '<br>'.join(rows)
 
def main():
    bitcoin_history = []
    while True:
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})
 
        # Отправка срочного уведомления
        if price > BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_price_emergency', price)
 
        # Отправка уведомления в Telegram
        if len(bitcoin_history) == 5:  # После получения 5 объектов в bitcoin_history – отправляем обновление
            post_ifttt_webhook('bitcoin_price_update', format_bitcoin_history(bitcoin_history))
            # Сброс истории
            bitcoin_history = []
 
        time.sleep(3600)  # Сон на 5 минут(Для тестовых целей вы можете указать меньшее число)
 
if __name__ == '__main__':
    main()
