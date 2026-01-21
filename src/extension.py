from discord.ext import commands

async def extension(app: commands.Bot) -> None:
    from .modules.AntiFakeCryptoGiveAWay.eventListener import AntiFakeCryptoGiveAWay
    from .modules.AntiFakeCryptoGiveAWay.Hash import Hash

    await app.add_cog(AntiFakeCryptoGiveAWay(HashList=await Hash()))