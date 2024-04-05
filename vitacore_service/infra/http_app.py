import uvicorn
from fastapi import FastAPI

from vitacore_service.presentation.http.routers import router


app = FastAPI()

app.include_router(router, prefix="/forTis")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
