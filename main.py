import uvicorn
from fastapi import FastAPI
from scripts.core.services.movie_services import movie_router as apps
app = FastAPI()
app.include_router(apps)
if __name__ == "__main__":
    uvicorn.run("main:app")
