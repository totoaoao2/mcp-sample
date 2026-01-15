from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def exec1():
    # 修正：適切な数値変数を使用
    user_id = 123  # 例として数値を設定
    result = 2 + user_id
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)