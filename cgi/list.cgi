#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
import sqlite3
import cgitb


DB_FILE = "database.db"

print("Content-Type: application/json")
print("Access-Control-Allow-Origin: *")
print()

conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS messages (
        id TEXT PRIMARY KEY,
        text TEXT
    )
    """
)

cur.execute("SELECT id, text FROM messages")
rows = cur.fetchall()
conn.close()

data = {"output": [{"id": row[0], "text": row[1]} for row in rows]}
print(json.dumps(data, ensure_ascii=False))
