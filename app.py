from fastapi import FastAPI

app = FastAPI()

def exec1():
    """問題のある関数 - idが未定義でTypeError発生"""
    # line 9でエラー発生
    result = 2 + id  # TypeError: 'builtin_function_or_method' object does not support item assignment
    return result

@app.get("/test")
async def test_endpoint():
    """エラーを引き起こすエンドポイント"""
    return exec1()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)