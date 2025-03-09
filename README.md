# Sample ToDo Bot

This bot is working with the **aiogram** 3.x and **SQLAlchemy** 2.x frameworks

```
python -m venv .venv
```

## Install packages:

```
pip install -r requirements.txt
```

## copy .env.example from .env

```
cp .env.example .env
```

## Setting for bot

you have token telegram bot for example
```
TOKEN='31415926535:BAFrwstyGI1Vl4AD8mdSNqOKiNnDUO8IEcs'
```

setting sqlite3
```
DB_URL='sqlite+aiosqlite:///db.sqlite3'
```

or setting postgresql
```
DB_URL='postgresql+asyncpg://user:password@host:port/dbname'
```

## start bot

```
python run.py
```