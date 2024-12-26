from fastapi import FastAPI , HTTPException


app = FastAPI()

@app.get("/")
async def welcome():
    return ("Welcome to my first deployed API. Provide a number and get its square")
 
@app.get("/square")
async def square_number(number : float):
    try:
        result = number *number
        return {"number": number, "square": result }
    except Exception as e:
        raise HTTPException(status_code=400, detail= "invalid input. please input a valid number")
    