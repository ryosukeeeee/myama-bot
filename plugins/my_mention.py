# coding: uft-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

# @listen_to('松のや')
# def listen_func(message):
#     message.reply('松のやは神')

@listen_to('hello')
def reply2hello(message):
    message.reply('hello')
