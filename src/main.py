import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,  # Allows cookies/authorization headers
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/nl2code")
def nl2code():
    data = json.dumps({"code": "print(\"hello world\")"})
    return data
 
if __name__ == "__main__":

    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)