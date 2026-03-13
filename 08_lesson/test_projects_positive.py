import pytest


@pytest.mark.positive_test
def test_create_project_success(api_client):
    """Позитивный тест: создание проекта с валидным названием"""
    title = 'Новый проект'
    resp = api_client.create_project(title)
    assert resp['id'] is not None, 'ID проекта не должен быть пустым'
    assert isinstance(resp['id'], str), 'ID должен быть строкой'
    assert len(resp['id']) > 0, 'Длина ID должна быть больше 0'


@pytest.mark.positive_test
def test_edit_project_success(api_client, test_project):
    """Позитивный тест: обновление названия проекта"""
    new_title = 'Обновлённый проект'
    resp = api_client.edit_project(test_project, new_title)
    assert 'id' in resp, 'Ответ должен содержать поле "id"'
    assert resp['id'] == test_project, 'ID должны совпадать '


@pytest.mark.positive_test
def test_get_project_success(api_client, test_project):
    """Позитивный тест: получение проекта по ID"""
    response = api_client.get_project_by_id(test_project)
    assert 'id' in response, 'Ответ должен содержать поле "id"'
    assert 'title' in response, 'Ответ должен содержать поле "title"'
    assert response['id'] == test_project, 'ID должен совпадать с запрошенным'


@pytest.mark.positive_test
def test_mark_project_as_deleted(api_client, test_project):
    """Позитивный тест: помечаем проект как удалённый"""
    response = api_client.edit_project(
        test_project, 'Удаляемый проект', mark_as_deleted=True
    )
    assert 'id' in response, "Ответ должен содержать ID"
    project_data = api_client.get_project_by_id(test_project)
    if 'deleted' in project_data:
        assert project_data['deleted'] is True, \
            'Проект должен быть помечен как удалённый'
