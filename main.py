from fastapi import FastAPI
from models import Products
from database import session , engine
import database_model

app = FastAPI()          #created an app object for my FASTAPI class 

products = [
    Products(id=1,name = 'phone',description='budget phone',price = 99,quantity=10),
    Products(id=2,name = 'laptop',description='gaming laptop ',price = 599,quantity=18),
    Products(id=3,name = 'xbox',description='microsoft',price = 599,quantity=10),
    Products(id=4,name = 'psp',description='sony',price = 699,quantity=10)
]

'''
# adding products from the list 


@app.get("/")  #URL1
def greet():
    return "welcome to my server"

    
# to view all products
@app.get('/products') #URL2
def get_all_products():
    return products

#to get product using ID
@app.get('/product/{id}')  #URL3
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
    return "product not found"

#to add a new product 
@app.post('/addedproducts') #URL4 
def add_product(product:Products):   #tells the FASTAPI the format of the request(json)
    products.append(product)
    return product

#to update an existing product
@app.put('/updateproduct')
def update_product(id:int , product:Products):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product has been updated"
    return "product not found"

#to delete a product
@app.delete('/delproduct')
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return"product deleted"
        return "product not found"
    
'''

#using the database

import database_model
from sqlalchemy.orm import Session
database_model.Base.metadata.create_all(bind=engine)   #this creates the table with the columns in the sql database
from fastapi import Depends
from database_model import Item
# making use of dependency injection in order to open and close a connection

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

# now we add the data in the table 
# we use model.dump to get key value pairs and then we unpack it



def init_db():
    db =session()

    count = db.query(database_model.Item).count
    
    if count == 0:
        for i in products:
            db.add(database_model.Item(**i.model_dump()))

        db.commit()

init_db()


# to get all the products from the table on the Uvicorn server

@app.get('/products')
def get_all_products(db:Session = Depends(get_db)):
    
    db_products = db.query(database_model.Item).all()

    return db_products

# getting the product using ID from the database

@app.get('/products/{id}')
def get_product_by_id(id:int , db:Session = Depends(get_db)):
    db_product = db.query(database_model.Item).filter(database_model.Item.id == id).first()
    if db_product:
        return db_product
    else:
        return "product not found"

# to add the new product to the database
@app.post('/product')
def add_products(product:Item, db:Session=Depends(get_db)):
    db.add(database_model.Item(**product.model_dump()))
    db.commit()
    return product

#to update any product in the database
@app.put('/product')
def update_product(id:int,product :Item, db:Session =Depends(get_db)):
    db_product = db.query(database_model.Item).filter(database_model.Item.id == id).first() # to check if the product exists
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product has been updated"
    else:
        return "product not found"

# to delete a product from the database
@app.delete('/products')
def delete_entry(id:int,db:Session=Depends(get_db)):
    db_product = db.query(database_model.Item).filter(database_model.Item.id == id).first()
    if db_product:
        del db_product
        db.commit() 
        return "product has been successfully deleted from the database"
    else:
        return "product not found"
