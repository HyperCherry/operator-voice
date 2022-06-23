from hoshino import Service

sv = Service('operator_voice')


@sv.on_fullmatch('粉毛', '澄闪')
async def hello(bot, ev):
    await bot.send(ev, '博士我在哦~')
