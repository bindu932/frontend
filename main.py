from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from routes import router as api_routes

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float

class Order(BaseModel):
    id: int
    product_id: int
    quantity: int

@app.get("/")
async def root():
    return {"message": "Welcome to the E-commerce API"}

app.include_router(api_routes)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)

