def test_create_product(client, headers):

    payload = {
        "name": "MacBook Pro",
        "description": "Apple Laptop",
        "price": 2499.99,
        "quantity": 5
    }

    response = client.post(
        "/products",
        json=payload,
        headers=headers
    )

    assert response.status_code == 201

    body = response.json()

    assert body["id"] == 1
    assert body["name"] == payload["name"]
    assert body["description"] == payload["description"]
    assert body["price"] == payload["price"]
    assert body["quantity"] == payload["quantity"]


def test_get_all_products(client, headers):

    payload = {
        "name": "iPhone 16",
        "description": "Apple Phone",
        "price": 999.99,
        "quantity": 10
    }

    client.post(
        "/products",
        json=payload,
        headers=headers
    )

    response = client.get(
        "/products",
        headers=headers
    )

    assert response.status_code == 200

    body = response.json()

    assert len(body) == 1
    assert body[0]["name"] == "iPhone 16"


def test_get_product(client, headers):

    payload = {
        "name": "AirPods Pro",
        "description": "Apple Earbuds",
        "price": 299.99,
        "quantity": 8
    }

    created = client.post(
        "/products",
        json=payload,
        headers=headers
    ).json()

    response = client.get(
        f"/products/{created['id']}",
        headers=headers
    )

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == created["id"]
    assert body["name"] == "AirPods Pro"


def test_get_product_not_found(client, headers):

    response = client.get(
        "/products/999",
        headers=headers
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "product not found"


def test_update_product(client, headers):

    payload = {
        "name": "MacBook Air",
        "description": "Laptop",
        "price": 1500,
        "quantity": 5
    }

    created = client.post(
        "/products",
        json=payload,
        headers=headers
    ).json()

    update_payload = {
        "name": "MacBook Air M4",
        "description": "Updated Laptop",
        "price": 1800,
        "quantity": 7
    }

    response = client.put(
        f"/products/{created['id']}",
        json=update_payload,
        headers=headers
    )

    assert response.status_code == 200

    body = response.json()

    assert body["name"] == "MacBook Air M4"
    assert body["description"] == "Updated Laptop"
    assert body["price"] == 1800
    assert body["quantity"] == 7


def test_update_product_not_found(client, headers):

    payload = {
        "name": "Test",
        "description": "Test",
        "price": 10,
        "quantity": 1
    }

    response = client.put(
        "/products/999",
        json=payload,
        headers=headers
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "product not found"


def test_delete_product(client, headers):

    payload = {
        "name": "Keyboard",
        "description": "Mechanical Keyboard",
        "price": 120,
        "quantity": 15
    }

    created = client.post(
        "/products",
        json=payload,
        headers=headers
    ).json()

    response = client.delete(
        f"/products/{created['id']}",
        headers=headers
    )

    assert response.status_code == 204

    response = client.get(
        f"/products/{created['id']}",
        headers=headers
    )

    assert response.status_code == 404


def test_delete_product_not_found(client, headers):

    response = client.delete(
        "/products/999",
        headers=headers
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "product not found"


def test_create_product_validation(client, headers):

    payload = {
        "name": "",
        "description": "",
        "price": -10,
        "quantity": -1
    }

    response = client.post(
        "/products",
        json=payload,
        headers=headers
    )

    assert response.status_code == 422