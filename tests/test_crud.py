from app.crud import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product
)

from app.schemas import (
    ProductCreate,
    ProductUpdate
)


def test_create_product(db):

    request = ProductCreate(
        name="iPhone 16",
        description="Apple iPhone",
        price=999.99,
        quantity=5
    )

    product = create_product(request,db)

    assert product.id is not None
    assert product.name == "iPhone 16"
    assert product.description == "Apple iPhone"
    assert product.price == 999.99
    assert product.quantity == 5


def test_get_product(db):

    request = ProductCreate(
        name="MacBook Pro",
        description="Apple Laptop",
        price=2499.99,
        quantity=3
    )

    created = create_product(request,db)

    product = get_product_by_id(created.id,db)

    assert product is not None
    assert product.id == created.id
    assert product.name == "MacBook Pro"


def test_get_product_not_found(db):

    product = get_product_by_id(999,db)

    assert product is None


def test_get_all_products(db):

    create_product(
        ProductCreate(
            name="Product 1",
            description="Description 1",
            price=10,
            quantity=2
        ),
        db
    )

    create_product(
        ProductCreate(
            name="Product 2",
            description="Description 2",
            price=20,
            quantity=5
        ),
        db
    )

    products = get_all_products(db)

    assert len(products) == 2


def test_update_product(db):

    created = create_product(
        ProductCreate(
            name="Old Product",
            description="Old Description",
            price=100,
            quantity=10
        ),
        db
    )

    updated = update_product(
        created.id,
        ProductUpdate(
            name="New Product",
            description="New Description",
            price=200,
            quantity=25
        ),
        db
    )

    assert updated.name == "New Product"
    assert updated.description == "New Description"
    assert updated.price == 200
    assert updated.quantity == 25


def test_update_product_not_found(db):

    updated = update_product(
        999,
        ProductUpdate(
            name="Test",
            description="Test",
            price=10,
            quantity=1
        ),
        db
    )

    assert updated is None


def test_delete_product(db):

    created = create_product(
        ProductCreate(
            name="Delete Me",
            description="Delete Description",
            price=50,
            quantity=4
        ),
        db
    )

    deleted = delete_product(created.id,db)

    assert deleted is True

    product = get_product_by_id(created.id,db)

    assert product is None


def test_delete_product_not_found(db):

    deleted = delete_product(999,db)

    assert deleted is False