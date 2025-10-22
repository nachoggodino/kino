from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.chat_controller import router as chat_router

app = FastAPI(title="Kino Backend")

app.include_router(chat_router, prefix="/kino")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get( "/" )
def health_check():
    return {"status": "ok", "message": "Kino backend is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
