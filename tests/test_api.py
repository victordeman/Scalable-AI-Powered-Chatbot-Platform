import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post("/api/chat", json={"message": "Hello"})
    assert response.status_code == 200
    assert "response" in response.json()
