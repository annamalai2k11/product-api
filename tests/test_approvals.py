def test_create_approval(client):
    payload = {
        "request_type": "CREATE_PRODUCT",
        "requested_by": "alice",
        "payload": {
            "name": "Laptop",
            "description": "Gaming laptop",
            "price": 1499.99,
            "quantity": 2,
        },
    }

    response = client.post("/approvals", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["requested_by"] == "alice"
    assert body["status"] == "PENDING"
    assert body["request_type"] == "CREATE_PRODUCT"
    assert body["payload"]["name"] == "Laptop"


def test_get_pending_approvals(client):
    payload = {
        "request_type": "CREATE_PRODUCT",
        "requested_by": "bob",
        "payload": {"name": "Mouse"},
    }

    client.post("/approvals", json=payload)

    response = client.get("/approvals")

    assert response.status_code == 200
    body = response.json()
    assert len(body) >= 1
    assert any(item["requested_by"] == "bob" for item in body)


def test_approve_approval(client):
    created = client.post(
        "/approvals",
        json={
            "request_type": "CREATE_PRODUCT",
            "requested_by": "carol",
            "payload": {"name": "Keyboard"},
        },
    ).json()

    response = client.post(
        f"/approvals/{created['approval_id']}/approve",
        json={"comments": "Looks good"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "APPROVED"
    assert body["approval_id"] == created["approval_id"]


def test_reject_approval(client):
    created = client.post(
        "/approvals",
        json={
            "request_type": "REJECT_PRODUCT",
            "requested_by": "dave",
            "payload": {"name": "Rejected item"},
        },
    ).json()

    response = client.post(
        f"/approvals/{created['approval_id']}/reject",
        json={"comments": "Not approved"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "REJECTED"
    assert body["approval_id"] == created["approval_id"]


def test_get_missing_approval_returns_404(client):
    response = client.get("/approvals/unknown-approval-id")

    assert response.status_code == 404
    assert response.json()["detail"] == "Approval not found"
