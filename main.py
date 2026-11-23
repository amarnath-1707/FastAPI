from fastapi import FastAPI
from models import product
from database import engine,SessionLocal
import database_models




app = FastAPI()


database_models.Base.metadata.create_all(bind=engine)




@app.get("/")
def greet():
    return "Hello from Fastapi"


products = [
    product(id= 1, description = "smart phone", price = 99, name = "phone",quantity = 10),
    product(id=2,description ="gaming laptop",price = 999,name ="laptop",quantity = 10)
]


def db_init():
    db = SessionLocal()
    count = db.query(database_models.Product).count
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))    
        db.commit()

db_init()    


@app.get("/products") 
def get_all_products():
    return products


@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
        else:
            return "product not found"


@app.post("/product")
def add_Products(product:product):
    products.append(product)
    return products


@app.put("/product")
def update_products(id:int,product: product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = products
            return "products added successfully"
    return "no product found"


@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted successfully"
    return "product not found"      