from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from v1.routes.classifications import controller as classifications
from v1.routes.users import controller as users
from v1.routes.suppliers import controller as suppliers
import os
from dotenv import load_dotenv

load_dotenv()
class ClassiAPI:
    def __init__(self):
        self.app = FastAPI()
        self.setup_middleware()
        self.setup_routers()
        
    def setup_middleware(self):
        origins = ["*"]
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def setup_routers(self):
        self.app.include_router(classifications.router)
        self.app.include_router(users.router)
        self.app.include_router(suppliers.router)

    def run(self):
        uvicorn.run("main:server.app", host="localhost", port=int(os.environ.get("PORT")), reload=True)

server = ClassiAPI()

if __name__ == "__main__":
    server.run()

