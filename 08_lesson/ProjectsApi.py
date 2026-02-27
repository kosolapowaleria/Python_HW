import requests


class ProjectsApi:

    def __init__(self, url):
        self.url = url
        self.headers = self.headers = {
            'Content-Type': 'application/json'
        }
        self._token = None

    def get_company_id(self, login, password):
        creds = {
            'login': login,
            'password': password
        }
        url = f'{self.url}/api-v2/auth/companies'
        resp = requests.post(url, json=creds, headers=self.headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return [company['id'] for company in data['content']]

    def get_token(self, login, password, company_id):
        creds = {
            'login': login,
            'password': password,
            'companyId': company_id
        }
        url = f'{self.url}/api-v2/auth/keys'
        resp = requests.post(url, json=creds, headers=self.headers, timeout=10)
        resp.raise_for_status()
        result = resp.json()
        self._token = result.get('key')
        self.headers['Authorization'] = f'Bearer {self._token}'
        return result

    def _make_request(self, method, endpoint, **kwargs):
        url = f'{self.url}{endpoint}'
        resp = requests.request(method, url, headers=self.headers, **kwargs)
        if resp.status_code >= 400:
            try:
                error_data = resp.json()
            except ValueError:
                error_data = {'error': resp.text}
            raise requests.exceptions.HTTPError(
                f"HTTP {resp.status_code}: {error_data}",
                response=resp
            )
        return resp.json()

    def create_project(self, title):
        creds = {'title': title}
        return self._make_request('POST', '/api-v2/projects', json=creds)

    def edit_project(self, project_id, new_title, mark_as_deleted=False):
        creds = {
            'title': new_title
        }
        endpoint = f'/api-v2/projects/{project_id}'
        if mark_as_deleted:
            creds['deleted'] = True
        return self._make_request('PUT', endpoint, json=creds)

    def get_project_by_id(self, project_id):
        endpoint = f'/api-v2/projects/{project_id}'
        return self._make_request('GET', endpoint)
