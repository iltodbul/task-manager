import pytest
from app import validate_task

def test_validate_task_missing_title_high():
    data = {"priority": "High"}
    is_valid, error = validate_task(data)
    assert is_valid is False
    assert error == "Title is required"

def test_validate_task_missing_title_low():
    data = {"priority": "Low"}
    is_valid, error = validate_task(data)
    assert is_valid is False
    assert error == "Title is required"

def test_validate_task_high_priority_no_date():
    data = {"title": "Critical Bug", "priority": "High"}
    is_valid, error = validate_task(data)
    assert is_valid is False
    assert error == "High priority tasks need a due date"

def test_validate_task_valid_low():
    data = {"title": "Read the news", "priority": "Low"}
    is_valid, error = validate_task(data)
    assert is_valid is True
    assert error is None

def test_validate_task_valid_high():
    data = {"title": "Update Jenkins", "priority": "High", "due_date": "2026-02-10"}
    is_valid, error = validate_task(data)
    assert is_valid is True
    assert error is None
