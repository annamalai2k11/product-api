from .models import Product
from .schemas import ProductCreate,ProductUpdate
from sqlalchemy.orm import Session


def get_all_products(db:Session):
    return db.query(Product).all()

def get_product_by_id(product_id: int, db:Session):
    return db.query(Product).filter(Product.id==product_id).first()

def create_product(request: ProductCreate, db:Session):
    obj = Product(**request.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_product(product_id:int,request: ProductUpdate, db:Session):
    product = get_product_by_id(product_id,db)

    if not product:
        return None

    for key, value in request.model_dump().items():
        setattr(product,key,value)

    db.commit()
    db.refresh(product)
    return product

def delete_product(product_id: int, db:Session):
    product = get_product_by_id(product_id,db)

    if not product:
        return False

    db.delete(product)
    db.commit()
    return True






