from pip._vendor.distlib.compat import raw_input
from rivescript import RiveScript


bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()

while True:
    msg = raw_input('You> ')
    if msg == '/quit':
        quit()

    reply = bot.reply("localuser", msg)
    print('Bot>', reply)
