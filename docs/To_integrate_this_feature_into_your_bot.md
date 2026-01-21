## 📦 Installation
Install the required dependencies:
```bash
pip install discord.py pyyaml imagehash pillow
```

## 🔌 Integrating SwitAC into Your Bot
### Import the extension
```python
from src import extension
```

### Load the extension when the bot is ready
```python
import discord
from discord.ext import commands
from src import extension

intents = discord.Intents.default()
intents.message_content = True

app = commands.Bot(command_prefix="!", intents=intents)

@app.event
async def on_ready():
    await extension(app) # <- Add this to your on_ready event
    print(f"Logged in as {app.user}")

app.run("YOUR_BOT_TOKEN")

```