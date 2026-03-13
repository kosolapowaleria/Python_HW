import pytest
from ProjectsApi import ProjectsApi


@pytest.fixture(scope="session")
def auth_data():
    """Внести данные для авторизации из приложенного файла"""
    return {
        'login': '',
        'password': ''
    }


@pytest.fixture(scope="session")
def api_client(auth_data):
    api = ProjectsApi('https://ru.yougile.com')
    company_ids = api.get_company_id(auth_data['login'], auth_data['password'])
    company_id = company_ids[0]
    api.get_token(auth_data['login'], auth_data['password'], company_id)
    return api


@pytest.fixture
def test_project(api_client):
    resp = api_client.create_project('Тестовый проект для теста')
    project_id = resp['id']
    yield project_id
    try:
        api_client.edit_project(
            project_id, 'Проект для удаления', mark_as_deleted=True
        )
    except Exception as e:
        print(f'Предупреждение:'
              f' не удалось пометить проект {project_id} как удалённый: {e}')
