import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_octocat_gists(client):
    response = client.get("/octocat")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)  # GitHub gists are returned as a list
    # Each gist should have an 'id' key at minimum
    if data:  # only check if there are gists
        assert "id" in data[0]

