def test_request_without_api_key(client):

    response = client.get("/products")

    assert response.status_code == 422


def test_request_with_invalid_api_key(client):

    response = client.get(
        "/products",
        headers={
            "x-api-key": "invalid-api-key"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid api key"


def test_request_with_valid_api_key(client, headers):

    response = client.get(
        "/products",
        headers=headers
    )

    assert response.status_code == 200


def test_create_product_with_invalid_api_key(client):

    payload = {
        "name": "MacBook Pro",
        "description": "Apple Laptop",
        "price": 2499.99,
        "quantity": 10
    }

    response = client.post(
        "/products",
        json=payload,
        headers={
            "x-api-key": "invalid-api-key"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid api key"


def test_delete_product_with_invalid_api_key(client):

    response = client.delete(
        "/products/1",
        headers={
            "x-api-key": "invalid-api-key"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid api key"