from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def exec1():
    # 修正：適切な変数名を使用し、正しい型で計算を行う
    user_id = 3  # 例として数値の ID を使用
    result = 2 + user_id
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)