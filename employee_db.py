from pymongo import MongoClient
from pydantic import BaseModel
from fastapi import FastAPI, Request

app = FastAPI()

# communicate with the Mongo db we are connecting with database
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
db = client.interns_b2_23
collection = db.susithra


class Emp(BaseModel):
    employee_username: str
    password: str
    confirm_password: str
    mobile_number: str


@app.post("/employee_signup")
async def employee_signup(request: Request):
    form_data = await request.form()  # response of form data
    employee = Emp(
        employee_username=form_data["employee_username"],
        password=form_data["password"],
        confirm_password=form_data["confirm_password"],
        mobile_number=form_data["mobile_number"]
    )
    collection.insert_one(employee.dict())  # store the details in collection db
    return {"note": "employee sign up successfully"}


@app.post("/employee_login")
async def employee_login(request: Request):
    form_data = await request.form()
    employee_username = form_data["employee_username"]
    password = form_data["password"]
    employee = collection.find_one({"employee_username": employee_username, "password": password})
    if employee:
        return {"note": "login successful"}
    else:
        return {"error": "sorry, invalid input try with valid username and password"}




@app.post("/emp_update")
async def emp_update(request: Request):
   form_data = await request.form()
   employee_username = form_data["employee_username"]
   mobile_number = form_data["mobile_number"]
   new_number = form_data["new_number"]
   employee = collection.find_one({"employee_username": employee_username})
   if employee:
       employee["mobile_number"] = new_number
       collection.update_one({"employee_username": employee_username}, {"$set": employee})
       return {"note": "Employee details updated successfully"}
   else:
       return {"error": "Employee username not found"}



@app.post("/employee_delete")
async def employee_delete(request: Request):
    form_data = await request.form()
    employee_username = form_data["employee_username"]
    employee = collection.find_one({"employee_username": employee_username})
    if employee:
        collection.delete_one({"employee_username": employee_username})
        return {"note": "employee details deleted successful"}
    else:
        return {"error": "sorry, invalid input try with valid username and password"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
