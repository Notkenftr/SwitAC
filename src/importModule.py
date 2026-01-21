from discord.ext import commands
from .modules.AntiFakeCryptoGiveAWay.Hash import Hash

async def importModule(app: commands.Bot):
    from .modules.AntiFakeCryptoGiveAWay.eventListener import AntiFakeCryptoGiveAWay

    await app.add_cog(AntiFakeCryptoGiveAWay(HashList= await Hash()))

    await app.tree.sync()
