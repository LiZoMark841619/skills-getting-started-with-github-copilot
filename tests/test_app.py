import pytest
from fastapi.testclient import TestClient
from src.app import app

# Arrange-Act-Assert (AAA) pattern

def test_root_endpoint():
    # Arrange
    client = TestClient(app)
    expected_status = 200
    # Act
    response = client.get("/")
    # Assert
    assert response.status_code == expected_status
    # (További assert-ek, ha van válasz tartalom)
