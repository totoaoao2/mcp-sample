from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def exec1():
    # エラー：idは文字列型の変数だが、数値と加算しようとしている
    result = 2 + id
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)