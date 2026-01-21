from discord.ext import commands
from src.modules.AntiFakeCryptoGiveAWay.Hash import Hash

async def importModule(app: commands.Bot):
    from src.modules.AntiFakeCryptoGiveAWay.eventListener import AntiFakeCryptoGiveAWay

    await app.add_cog(AntiFakeCryptoGiveAWay(HashList= await Hash()))

    await app.tree.sync()
