# QuoteBot

A basic Discord bot written in Python that posts random quotes from a local `quotes.txt` file. Server admins can add new quotes using slash commands.

## Features

- **Random quotes:** Use `/quote` to post a random quote.
- **Add quotes:** Use `/addquote` to append a quote to the local collection (admin only).

## Requirements

- Python 3.14 or newer
- `pyenv` and `pyenv-virtualenv` (recommended)

## Project Structure

```text
quotebot/
├── bot.py
├── quotes.txt
├── requirements.txt
├── .env
└── README.md
```

- `bot.py` — Bot implementation.
- `quotes.txt` — Quote collection, with one quote per line.
- `requirements.txt` — Python dependencies.
- `.env` — Local configuration and bot token. Do not commit this file.

## Installation

### 1. Clone this repository

Or if you already have the project, navigate to its directory instead.

### 2. Install Python with pyenv

Check your installed Python versions:

```bash
pyenv versions
```

Install Python 3.14 if needed:

```bash
pyenv install 3.14
```

Create a virtual environment:

```bash
pyenv virtualenv 3.14 quotebot-env
pyenv local quotebot-env
```

Verify the environment:

```bash
python --version
which python
```

### 3. Install dependencies from requirements.txt

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Discord Application Setup

### 1. Create the bot

1. Open the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application.
3. Open the **Bot** section and create or configure its bot user.
4. Copy the bot token and store it securely.

**Never publish your bot token or commit it to version control.**

### 2. Configure slash commands

In the Developer Portal, open **OAuth2 → URL Generator** and select these scopes:

- `bot`
- `applications.commands`

Select the bot permissions:

- View Channels
- Send Messages

Use the generated URL to invite the bot to your Discord server. You must have permission to manage the server.

## Configuration

Create a `.env` file in the project root:

```dotenv
QUOTEBOT_TOKEN=your_discord_bot_token
```

Make sure your Python code loads environment variables:

```python
from dotenv import load_dotenv

load_dotenv()
```

The bot should read its token with:

```python
token = os.getenv("QUOTEBOT_TOKEN")
```

## Quote Storage

An example `quotes.txt` file is provided, containing one quote per line. You can delete these and add your own.

The bot reads this file when `/quote` is invoked and randomly selects one non-empty line.

New quotes are appended to the file, so existing quotes are preserved.

## Usage

Start the bot:

```bash
python bot.py
```

When the bot is online, use the following commands in your Discord server.

| Command | Description | Access |
|---|---|---|
| `/quote` | Posts a random quote | All users |
| `/addquote quote:<text>` | Adds a quote to `quotes.txt` | Server admins |
