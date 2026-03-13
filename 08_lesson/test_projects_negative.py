import pytest
import requests


@pytest.mark.negative_test
def test_create_project_empty_title(api_client):
    """Негативный тест: попытка создать проект с пустым названием"""
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        api_client.create_project("")
    assert excinfo.value.response.status_code in [400], \
        'Должен быть код 400 (Bad Request)'


@pytest.mark.negative_test
def test_create_project_none_title(api_client):
    """Негативный тест: попытка создать проект с None в названии"""
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        api_client.create_project(None)
    assert excinfo.value.response.status_code in [400, 422], \
        'Должен быть код 400 или 422'


@pytest.mark.negative_test
def test_edit_project_invalid_id(api_client):
    """Негативный тест: попытка обновить проект с некорректным ID"""
    invalid_id = 'invalid-format'
    new_title = 'Новое название'
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        api_client.edit_project(invalid_id, new_title)
    assert excinfo.value.response.status_code in [400, 404], \
        'Должен быть код 400 (некорректный формат) или 404 (не найден)'


@pytest.mark.negative_test
def test_edit_project_nonexistent_id(api_client):
    """Негативный тест: попытка обновить несуществующий проект"""
    nonexistent_id = '00000000-0000-0000-0000-000000000000'
    new_title = 'Новое название'
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        api_client.edit_project(nonexistent_id, new_title)
    assert excinfo.value.response.status_code == 404, \
        'Должен быть код 404 (Not Found)'


@pytest.mark.negative_test
def test_get_project_invalid_id(api_client):
    """Негативный тест: попытка получить проект с некорректным ID"""
    invalid_id = "not-a-uuid"
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        api_client.get_project_by_id(invalid_id)
    assert excinfo.value.response.status_code in [400, 404], \
        'Должен быть код 400 или 404'


@pytest.mark.negative_test
def test_get_project_nonexistent_id(api_client):
    """Негативный тест: попытка получить несуществующий проект"""
    nonexistent_id = "11111111-1111-1111-1111-111111111111"
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        api_client.get_project_by_id(nonexistent_id)
    assert excinfo.value.response.status_code == 404, \
        'Должен быть код 404 (Not Found)'
