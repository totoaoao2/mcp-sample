from fastapi import FastAPI, HTTPException
import uvicorn
from typing import Optional

app = FastAPI()

@app.get("/")
def exec1(id: Optional[int] = None):
    print(f"Received id: {id}")
    
    # Handle None case gracefully
    if id is None:
        raise HTTPException(status_code=400, detail="id parameter is required")
    
    result = 2 + id
    return {"sts": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")