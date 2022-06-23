from hoshino import Service

sv = Service('operator_voice')


@sv.on_fullmatch('', only_to_me=True)
async def demo_fun_1(bot, ev):
    await bot.send(ev, '我在哦博士~')
