from hoshino import Service, R
from random import choice

sv = Service('operator_voice')

nudge = ['问候', '闲置', '交谈1', '交谈2', '交谈3',
         '晋升后交谈1', '晋升后交谈2', '信赖提升后交谈1', '信赖提升后交谈2', '信赖提升后交谈3',
         '戳一下', '信赖触摸',
         '干员报到', '精英化晋升1',
         '编入队伍', '任命队长']


@sv.on_fullmatch('', only_to_me=True)
async def demo_fun_1(bot, ev):
    await bot.send(ev, '我在哦博士~')
    await bot.send(ev, R.rec(choice(nudge)).cqcode)
