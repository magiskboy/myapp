from databases import Database

__all__ = ["connect", "disconnect", "get"]

_db: Database = None

async def connect(uri: str):
    global _db
    _db = Database(uri)
    await _db.connect()

async def disconnect():
    global _db
    await _db.disconnect()

def get() -> Database:
    global _db
    return _db