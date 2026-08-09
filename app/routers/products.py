from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.security import verify_api_key
from app.schemas import ProductUpdate, ProductCreate, ProductResponse
from app.crud import (get_product_by_id as get_product_by_id_db,
                      get_all_products as get_all_products_db,
                      create_product as create_product_db,
                      update_product as update_product_db,
                      delete_product as delete_product_db)
from app.database import get_db

router = APIRouter(
    prefix="/products",
    tags=["products"],
    dependencies=[Depends(verify_api_key)]
)

@router.post(
    "",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_product(request:ProductCreate, db:Session = Depends(get_db)):
    return create_product_db(request,db)

@router.put(
    "/{product_id}",
    response_model=ProductResponse,
)
def update_product(product_id:int, request:ProductUpdate, db:Session = Depends(get_db)):
    product = update_product_db(product_id,request,db)
    if not product:
        raise HTTPException(404, "product not found")
    return product

@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_product(product_id:int, db:Session=Depends(get_db)):
    deleted = delete_product_db(product_id,db)
    if not deleted:
        raise HTTPException(404,"product not found")


@router.get(
    "",
    response_model = list[ProductResponse]
)
def get_all_products(db: Session = Depends(get_db)):
    return get_all_products_db(db)

@router.get(
    "/{product_id}",
    response_model = ProductResponse
)
def get_product(product_id:int, db: Session = Depends(get_db)):
    product = get_product_by_id_db(product_id,db)
    if not product:
        raise HTTPException(404, "product not found")
    return product
