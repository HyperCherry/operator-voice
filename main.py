import os

from hoshino import Service, R
from random import choice
from hoshino.typing import MessageSegment, NoticeSession, CQEvent

sv = Service('operator_voice')

lang = "CHN"


@sv.on_fullmatch('', only_to_me=True)
async def greet(bot, ev):
    await bot.send(ev, '我在哦博士~')
    await bot.send(ev, R.rec(random_voice()).cqcode)


def random_voice():
    voice = choice(file_name_listdir(R.rec(lang).path))  # 获取到文件名
    return lang + "/" + voice


def random_expression():
    expression = choice(file_name_listdir(R.img('operator').path))
    return "operator/" + expression


def file_name_listdir(file_dir):
    targets = []
    for files in os.listdir(file_dir):
        targets.append(files)
    return targets


@sv.on_notice('notify.poke')
async def poke_back(session: NoticeSession):
    if session.ctx['target_id'] == session.ctx['self_id']:
        await session.send(R.img(random_expression()).cqcode)
