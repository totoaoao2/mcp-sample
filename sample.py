from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/")
def exec1(id: int = 0):
    print(id)
    # 安全性のため、Noneチェックも追加
    if id is None:
        raise HTTPException(status_code=400, detail="id parameter cannot be None")
    result = 2 + id
    return {"sts": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")