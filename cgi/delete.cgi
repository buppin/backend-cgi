#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
import cgi
import cgitb
import sqlite3

cgitb.enable()

form = cgi.FieldStorage()
id_val = form.getfirst("id", "").strip()

DB_FILE = "database.db"

print("Content-Type: application/json")
print("Access-Control-Allow-Origin: *")
print()

if not id_val:
    response = {"status": "error", "message": "Missing id"}
    print(json.dumps(response, ensure_ascii=False))
    exit()

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

cur.execute("DELETE FROM messages WHERE id = ?", (id_val,))
conn.commit()
deleted_rows = cur.rowcount
conn.close()

if deleted_rows > 0:
    response = {"status": "done", "deleted_id": id_val}
else:
    response = {"status": "not_found", "id": id_val}

print(json.dumps(response, ensure_ascii=False))

