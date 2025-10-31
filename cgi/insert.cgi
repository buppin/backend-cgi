#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
import cgi
import cgitb
import sqlite3
import os


form = cgi.FieldStorage()
id_val = form.getfirst("id", "").strip()
text_val = form.getfirst("text", "").strip()

DB_FILE = "database.db"

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

cur.execute(
    """
INSERT OR REPLACE INTO messages (id, text)
VALUES (?, ?)
""",
    (id_val, text_val),
)

conn.commit()
conn.close()

print("Content-Type: application/json")
print("Access-Control-Allow-Origin: *")
print()

response = {"status": "done"}
print(json.dumps(response))
