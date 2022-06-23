from pathlib import Path

from hoshino import Service, R

import wiki

sv = Service('operator_voice')

wiki = wiki.Wiki()
wiki.download_pallas_voices()


def get_voice(name: str):
    oper = '帕拉斯'
    file = wiki.voice_exists(oper, name)
    if not file:
        file = wiki.download_operator_voices(oper, name)
        if not file:
            return False
    return file


@sv.on_fullmatch('', only_to_me=True)
async def demo_fun_1(bot, ev):
    await bot.send(ev, '我在哦博士~')
    await bot.send(ev, R.rec(Path(get_voice('任命助理'))))

# msg: Message = MessageSegment.record(file=Path(get_voice('任命助理')))

# xxx = R.rec(xxx/xxx.mp3).cqcode
#
# @sv.on_fullmatch(["发送语音"])
# async def xxx(bot, ev):
#   await bot.send(ev, xxx)
