def main():
    import discord
    from discord.ext import commands
    from src.utils import Config
    app = commands.AutoShardedBot(command_prefix='!',
                                  intents=discord.Intents.all())

    @app.event
    async def on_ready():
        from src.importModule import importModule
        await importModule(app)
        print("Bot is ready.")
    app.run(Config().getToken())