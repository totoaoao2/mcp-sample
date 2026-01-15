from fastapi import FastAPI

app = FastAPI()

def exec1(item_id: int = 1):
    """修正済みの関数 - idパラメータを明示的に定義し型チェック追加"""
    try:
        # 型チェックを追加
        if not isinstance(item_id, int):
            raise ValueError(f"item_id must be an integer, got {type(item_id)}")
        
        # line 9 - 修正後: 適切なパラメータを使用
        result = 2 + item_id
        return {"result": result, "calculation": f"2 + {item_id}"}
    except Exception as e:
        return {"error": str(e), "type": type(e).__name__}

@app.get("/test")
async def test_endpoint(item_id: int = 1):
    """修正されたエンドポイント - パラメータ付きで動作"""
    return exec1(item_id)

@app.get("/")
async def root():
    """ルートエンドポイント"""
    return {"message": "FastAPI application is running", "test_endpoint": "/test?item_id=5"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)