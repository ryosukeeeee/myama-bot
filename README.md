# myama-bot

研究室のSlackで大人気のmyama-botです．
特定のキーワードを含むメンションに対して反応します．
myama-botが参加しているチャンネルに投稿されたメッセージにキーワードが含まれると反応します．
pluginsディレクトリ内の[my_mention.py](/plugins/my_mention.py)に振る舞いが定義されています．

## Built with
[slackbot](https://github.com/lins05/slackbot) - pythonのslackbot用ライブラリ

## Usage example
例：botが参加しているチャンネルに「とんかつ」を含むメッセージが投稿されたときに，「I love とんかつ」とメンションするようにしたい．
```python
@listen_to('とんかつ')
def reply2matsunoya(message):
	message.reply('I love とんかつ')
```

例：botに「名言」を含むメンションをすると，そのチャンネルにランダムに名言を投稿するようにしたい．
```python
@respond_to('名言')
def reply2phrase(message):
	message.send(random.choice([
		'空間こそがメディア',
		'余裕が停滞を生む',
		'終わりが見えると作業がだるい',
		'罰を与えなければいけない',
		'蓄えてるわけでしょ？爆発力がすごいね多分',
		'できてたね〜',
		'いっぱい酒飲むと死んだ脳細胞が生き返るって聞いたことある',
		'固くなってうまい',
		'おれたちも訴えかけるべき。蝉のように。',
		'臆病者は、勝つと分かっている戦いしかできない。'
		'フォーエバー・ラヴ',
		'30億人いるっしょ，女って',
		'悲報過ぎて秘宝館になった',
		'俺のやることじゃねえ',
		'止まない雨はないでしょ',
		'Appleすらも動かす男か']))
 ```
 
 ## References 
[PythonのslackbotライブラリでSlackボットを作る](https://qiita.com/sukesuke/items/1ac92251def87357fdf6)
