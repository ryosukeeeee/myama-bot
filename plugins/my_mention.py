# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import urllib
import json
import random

@listen_to('まつのや')
@listen_to('松の家')
@listen_to('松之屋')
@listen_to('松のや')
@listen_to('とんかつ')
@listen_to('トンカツ')
def listen_func(message):
    message.reply('松のやは神')

@default_reply
def reply2hello(message):
    message.reply(random.choice([':myama1', ':myama2:', ':tonkatsu:']))

@listen_to('大迫')
def reply2Osako(message):
	message.reply('半端ないって')

@respond_to('きょうのてんき')
@respond_to('きょうの天気')
@respond_to('今日の天気')
def weather(message):
	url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
	# '130010'とすると東京の情報を取得してくれる
	# ここを変えれば任意の地域の天気情報を取得できる
	city_id = '080020'
	html = urllib.request.urlopen(url + city_id)
	jsonfile = json.loads(html.read().decode('utf-8'))
	title = jsonfile['title']
	telop = jsonfile['forecasts'][0]['telop']
	#telopが晴れだったら晴れのスラックのアイコンとか場合分け
	telop_icon = ''
	if telop.find('雪') > -1:
	    telop_icon = ':showman:'
	elif telop.find('雷') > -1:
	    telop_icon = ':thinder_cloud_and_rain:'
	elif telop.find('晴') > -1:
	    if telop.find('曇') > -1:
	        telop_icon = ':partly_sunny:'
	    elif telop.find('雨') > -1:
	        telop_icon = ':partly_sunny_rain:'
	    else:
	        telop_icon = ':sunny:'
	elif telop.find('雨') > -1:
	    telop_icon = ':umbrella:'
	elif telop.find('曇') > -1:
	    telop_icon = ':cloud:'
	else:
	    telop_icon = ':fire:'
	text = title + '\n' + '今日の天気　' + telop + telop_icon
	message.send(text)
    description = jsonfile['description']['text']
    message.send(description)

@respond_to('あしたの天気')
@respond_to('あしたのてんき')
@respond_to('明日の天気')
def weather(message):
	url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
	# '130010'とすると東京の情報を取得してくれる
	# ここを変えれば任意の地域の天気情報を取得できる
	city_id = '080020'
	html = urllib.request.urlopen(url + city_id)
	jsonfile = json.loads(html.read().decode('utf-8'))
	title = jsonfile['title']
	telop = jsonfile['forecasts'][1]['telop']
	#telopが晴れだったら晴れのスラックのアイコンとか場合分け
	telop_icon = ''
	if telop.find('雪') > -1:
	    telop_icon = ':showman:'
	elif telop.find('雷') > -1:
	    telop_icon = ':thinder_cloud_and_rain:'
	elif telop.find('晴') > -1:
	    if telop.find('曇') > -1:
	        telop_icon = ':partly_sunny:'
	    elif telop.find('雨') > -1:
	        telop_icon = ':partly_sunny_rain:'
	    else:
	        telop_icon = ':sunny:'
	elif telop.find('雨') > -1:
	    telop_icon = ':umbrella:'
	elif telop.find('曇') > -1:
	    telop_icon = ':cloud:'
	else:
	    telop_icon = ':fire:'
	text = title + '\n' + '今日の天気　' + telop + telop_icon
	message.send(text)
    description = jsonfile['description']['text']
    message.send(description)
