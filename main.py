from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from v1.routes.classifications import controller as classifications
from v1.routes.users import controller as users
from v1.routes.suppliers import controller as suppliers

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(classifications.router)
app.include_router(users.router)
app.include_router(suppliers.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Pine Seeds Classifier API!"}


if __name__== "__main__":
    uvicorn.run(app, host='localhost', port=8000)
