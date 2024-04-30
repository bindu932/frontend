

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

# Fake database
database = {
    "products": [
        {"id": 1, "name": "Product 1", "price": 10.99},
        {"id": 2, "name": "Product 2", "price": 9.99},
        {"id": 3, "name": "Product 3", "price": 12.99}
    ],
    "orders": []
}

class Product(BaseModel):
    id: int
    name: str
    price: float

class Order(BaseModel):
    id: int
    product_id: int
    quantity: int

@app.get("/api/products")
async def get_products():
    return JSONResponse(content=jsonable_encoder(database["products"]), media_type="application/json")

@app.get("/api/orders")
async def get_orders():
    return JSONResponse(content=jsonable_encoder(database["orders"]), media_type="application/json")

@app.post("/api/orders")
async def create_order(order: Order):
    database["orders"].append(order)
    return JSONResponse(content=jsonable_encoder(order), media_type="application/json")

@app.get("/api/products/{product_id}")
async def get_product(product_id: int):
    for product in database["products"]:
        if product["id"] == product_id:
            return JSONResponse(content=jsonable_encoder(product), media_type="application/json")
    return JSONResponse(content={"error": "Product not found"}, media_type="application/json", status_code=404)

@app.put("/api/products/{product_id}")
async def update_product(product_id: int, product: Product):
    for p in database["products"]:
        if p["id"] == product_id:
            p["name"] = product.name
            p["price"] = product.price
            return JSONResponse(content=jsonable_encoder(product), media_type="application/json")
    return JSONResponse(content={"error": "Product not found"}, media_type="application/json", status_code=404)

@app.delete("/api/products/{product_id}")
async def delete_product(product_id: int):
    for product in database["products"]:
        if product["id"] == product_id:
            database["products"].remove(product)
            return JSONResponse(content={"message": "Product deleted"}, media_type="application/json")
    return JSONResponse(content={"error": "Product not found"}, media_type="application/json", status_code=404)
