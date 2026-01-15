from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/")
def exec1(id: int = 0):
    """
    Calculate result by adding 2 to the provided id.
    
    Args:
        id (int): Integer value to add to 2. Defaults to 0.
        
    Returns:
        dict: Dictionary containing the calculation result.
        
    Raises:
        HTTPException: If id is not a valid integer.
    """
    try:
        print(f"Received id: {id}")
        result = 2 + id
        return {"sts": result}
    except TypeError as e:
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid input: {str(e)}. Please provide a valid integer for 'id' parameter."
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")