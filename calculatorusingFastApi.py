from fastapi import FastAPI
app = FastAPI()#creating obj for FastApi


@app.get("/addition/{a}/{b}")#it is the path operation decorator
async def addition(a:float, b:float):
    return{"The addition of these two number is ": a+b}


@app.get("/subtraction/{a}/{b}")
async def subtraction(a:float,b:float):
    return {"The subtraction of these two number is ": a-b}

@app.get("/multiplication/{a}/{b}")
async def multiplication(a:float, b:float):
    return {"The multiplication of these two number is ": a*b}

@app.get("/division/{a}/{b}")
async def division(a:float, b:float):
    try:
        return {"The division of these two number is ": a/b}
    except:
        return{"invalid input for the division"}

@app.get("/modulus/{a}/{b}")
async def modulus(a:float, b:float):
    return {"The modulus of these two number is ": a%b}
