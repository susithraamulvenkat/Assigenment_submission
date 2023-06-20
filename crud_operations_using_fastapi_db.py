from pymongo import MongoClient
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

# communicate with the Mongo db we are connecting with database
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
db = client.interns_b2_23
collection = db.susithra


class Emp(BaseModel):
    emp_id: str
    emp_user_name: str
    emp_password: str
    emp_position: str
    emp_gender: str
#  insert the employee_details in the database


@app.post("/insert_employee")
async def insert_employee(emp: Emp):
    collection.insert_one(emp.dict())
    return {"note": "employee details are stored successfully"}


@app.get("/get_employee")
async def get_employee(emp_id: str):
    find_emp_id = collection.find_one({"emp_id": emp_id})
    if find_emp_id:
        return{
            "emp_id": find_emp_id["emp_id"],
            "emp_user_name": find_emp_id["emp_user_name"],
            "emp_password": find_emp_id["emp_password"],
            "emp_position": find_emp_id["emp_position"],
            "emp_gender": find_emp_id["emp_gender"]
             }
    else:
        return {"we cant able to find this employee!I think this employee id not exist"}


@app.put("/update_employee")
async def update_employee(emp_id: str, emp: Emp):
    emp_up = collection.find_one({"emp_id": emp_id})
    if emp_up:
        collection.update_one({"emp_id": emp_id}, {"$set": emp.dict()})
        return{"note": "Employee details are successfully in the updated in the database "}
    else:
        return{"This employee details are not there "}


@app.delete("/delete_employee")
async def delete_employee(emp_id: str):
    emp_del = collection.find_one({"emp_id": emp_id})
    if emp_del:
        collection.delete_one({"emp_id": emp_id})
        return {"note": "employee details are removed successfully"}
    else:
        return {"employee details are not found"}
