from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get('/')
def health_check():
    return 'ok'