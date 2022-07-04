from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import Customer, Type

# create instance of application
app = FastAPI()

# define database db
db: List[Customer] = [
    Customer(
        id=UUID("bfe3cf93-bd9a-41be-b2ad-1ae552097d11"),
        type_=Type.type_2D,
        grid_file="s3 URL",
        pole_file="s4 URL",
        critical_distances=[23, 34, 44]
    ),
    Customer(
        id=UUID("54b7ac91-66be-4217-b8ab-edc47258c6f8"),
        type_=Type.type_3D,
        grid_file="s3 URL",
        pole_file="s4 URL",
        critical_distances=[43, 4, 39]
    )
]


# Route for GET request
@app.get("/")
async def root():
    return {"Hello": "World"}


# Retrieve an existing geospatial-job
@app.get("/api/v1/customers")
async def retrieve_geospatial_job():
    return db;


# add new geospatial-job
@app.post("/api/v1/customers")
async def add_geospatial_job(customer: Customer):
    db.append(customer)
    return {"id": customer.id}


# Delete data from the database
@app.delete("/api/v1/customers/{customer_id}")
async def delete_geospatial_job(customer_id: UUID):
    for customer in db:
        if customer.id == customer_id:
            db.remove(customer)
            return
        raise HTTPException(
            status_code=404,
            detail=f"customer with id: {customer_id} does not exists"
        )





