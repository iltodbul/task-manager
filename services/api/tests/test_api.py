import pytest
from unittest.mock import patch
from app import app, validate_task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('app.db.set')
def test_create_task_api(mock_set, client):
    payload = {
        "title": "Pipeline Test",
        "priority": "Low"
    }
    response = client.post('/tasks', json=payload)
    data = response.get_json()
    
    assert response.status_code == 201
    assert data['title'] == "Pipeline Test"
    assert mock_set.called

@patch('app.db.set')
def test_create_task_api_high(mock_set, client):
    payload = {
        "title": "Pipeline Test",
        "priority": "High"
    }
    response = client.post('/tasks', json=payload)
    data = response.get_json()
    
    assert response.status_code == 400
    assert mock_set.called is False

@patch('app.db.keys')
def test_get_tasks_api(mock_keys, client):
    mock_keys.return_value = []
    response = client.get('/tasks')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_delete_nonexistent_task(client):
    with patch('app.db.delete') as mock_del:
        mock_del.return_value = 0
        response = client.delete('/tasks/invalid-id')
        assert response.status_code == 404
        assert response.get_json()['error'] == "Task not found"
