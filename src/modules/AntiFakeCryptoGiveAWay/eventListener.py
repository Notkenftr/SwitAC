import re
import time
import aiohttp
import discord
import imagehash
from io import BytesIO
from PIL import Image
from discord.ext import commands


class AntiFakeCryptoGiveAWay(commands.Cog):
    def __init__(self, HashList: list) -> None:
        self.HashList = HashList
        self.cache = set()
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        image_urls = []

        for attachment in message.attachments:
            image_urls.append(attachment.url)

        for embed in message.embeds:
            if embed.image:
                image_urls.append(embed.image.url)
            if embed.thumbnail:
                image_urls.append(embed.thumbnail.url)

        pattern = re.compile(
            r'https?://[^\s<>()"]+(?:\.(?:png|jpe?g|webp|gif))(?:\?[^\s<>()"]*)?',
            re.IGNORECASE
        )
        image_urls.extend(pattern.findall(message.content.lower().strip()))

        if not image_urls:
            return

        async with aiohttp.ClientSession() as session:
            for image_url in image_urls:
                async with session.get(image_url) as response:
                    if response.status != 200:
                        continue
                    raw = await response.read()
                    with Image.open(BytesIO(raw)).convert("RGB") as img:
                        upload_image_hash = imagehash.phash(img)

                if upload_image_hash in self.HashList:
                    await message.delete()
                    return
                for h in self.HashList:
                    if abs(h - upload_image_hash) <= 5:
                        self.cache.add(upload_image_hash)
                        await message.delete()
                    return
