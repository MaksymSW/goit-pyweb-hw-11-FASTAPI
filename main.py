import time
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy import text
from src.routes import search

from src.database.db import get_db
from src.routes import contacts

app = FastAPI()



@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    try:
        # Make request
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")


app.include_router(contacts.router)
app.include_router(search.search)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=9000, reload=True)