import os
import random
from pathlib import Path

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

QUOTES_FILE = Path(__file__).resolve().parent / "quotes.txt"


def load_quotes() -> list[str]:
    if not QUOTES_FILE.exists():
        QUOTES_FILE.touch()

    with QUOTES_FILE.open("r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def add_quote(quote: str) -> None:
    quote = " ".join(quote.split())

    with QUOTES_FILE.open("a", encoding="utf-8") as file:
        file.write(quote + "\n")


class QuoteBot(commands.Bot):
    async def setup_hook(self):
        synced = await self.tree.sync()
        print("Synced commands:", [cmd.name for cmd in synced])


bot = QuoteBot(
    command_prefix=commands.when_mentioned,
    intents=None,
)


@bot.event
async def on_ready():
    print(f"{bot.user} is online!")


@bot.tree.command(
    name="quote",
    description="Post a random quote from the list",
)
async def quote_command(interaction: discord.Interaction):
    try:
        quotes = load_quotes()
        print(f"Loaded {len(quotes)} quotes")
        if not quotes:
            await interaction.response.send_message(
                "There are no quotes yet. An admin can add one with /addquote."
            )
            return
        await interaction.response.send_message(random.choice(quotes))
    except Exception as e:
        print(f"Error handling /quote: {e}")
        if not interaction.response.is_done():
            await interaction.response.send_message(
                "Bork bork",
                ephemeral=True,
            )


@bot.tree.command(
    name="addquote",
    description="Add a quote (admins only)",
)
@app_commands.guild_only()
@app_commands.default_permissions(administrator=True)
async def add_quote_command(
    interaction: discord.Interaction,
    quote: str,
):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(
            "Only admins can add quotes.",
            ephemeral=True,
        )
        return

    quote = " ".join(quote.split())
    if not quote:
        await interaction.response.send_message(
            "Please provide a quote.",
            ephemeral=True,
        )
        return

    add_quote(quote)

    await interaction.response.send_message(
        f"Quote added!",
        ephemeral=True,
    )


if __name__ == "__main__":
    token = os.getenv("QUOTEBOT_TOKEN")

    if not token:
        raise RuntimeError("Set QUOTEBOT_TOKEN in your .env file before starting.")

    bot.run(token)
