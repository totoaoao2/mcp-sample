from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def exec1(id: int = None):
    print(id)
    result = 2 + id
    return {"sts": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
