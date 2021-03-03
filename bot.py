import discord
import asyncio

from secret import TOKEN


class PhilosophyBot(discord.Client):
    """DiscordBot"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Example :
        # create the background task and run it in the background
        #self.bg_task = self.loop.create_task(self.job())

    async def job(self):
        """Job to run indefinitely"""
        await self.wait_until_ready()

        while not self.is_closed():
            pass

    async def on_ready(self):
        print('Bot logged as {0.user}'.format(client))
        
        
    def documentation(self):
        """Return documentations"""
        doc = " ".join((
            "Bonjour, je suis la doc !\n\n",
            "Je tiens sur plusieurs lignes\n\n",
            f"<@!{client.user.id}> ping\n",
            f"<@!{client.user.id}> help\n",
        ))

        return(doc)
    
    async def on_message(self, message):
        """Handle messages"""
        if message.author == client.user:
            return
        
        if message.content.startswith(f"<@!{client.user.id}> "): 
            if "ping" in message.content:
                emoji = "🏓"
                await message.add_reaction(emoji)
                await message.channel.send("pong")
                
            if "help" in message.content:
                await message.channel.send(self.documentation())

client = PhilosophyBot()
client.run(TOKEN)
