import requests


class Client(object):
    def __init__(self, api_key, base=None):
        if base:
            self.base = base
        else:
            self.base = "http://0.0.0.0:8181/api"
        self.api_key = api_key

    def create_url(self, path):
        return "%s/%s?api_key=%s" % (self.base, path, self.api_key,)

    def api_request(self, path, method='POST', **kwargs):
        url = self.create_url(path)
        if method == 'POST':
            response = requests.post(url, **kwargs)
        elif method == 'GET':
            response = requests.get(url, **kwargs)

        if response.status_code == 200:
            return response.json()
        else:
            return {
                'status_code': response.status_code,
                'message': response.json().get('message')
            }

    def project_list(self):
        result = self.api_request(
            path="projects",
            method='GET'
        )
        return result

    def project_create(self, name, description, is_public):
        result = self.api_request(
            path="projects/create",
            method='POST',
            json={
                'name': name,
                'description': description,
                'is_public': is_public,
            }
        )
        return result

    def table_list(self, project_id):
        result = self.api_request(
            path="projects/%s/tables" % (project_id,),
            method='GET',
        )
        return result

    def table_create(self, project_id, name, description):
        result = self.api_request(
            path="projects/%s/tables/create" % (project_id,),
            method='POST',
            json={
                'name': name,
                'description': description,
            }
        )
        return result

    def column_create(self, table_id, name, column_type, is_unique, changeset_id):
        result = self.api_request(
            path="tables/%s/changesets/%s/columns/create" % (table_id, changeset_id),
            method='POST',
            json={
                'name': name,
                'type': column_type,
                'is_unique': is_unique,
            }
        )
        return result

    def data_list(self, table_id, filters=None):
        result = self.api_request(
            path="tables/%s/data/list" % (table_id,),
            method='POST',
            json={
                'filters': filters,
            }
        )
        return result['rows']

    def data_create(self, table_id, data, changeset_id):
        result = self.api_request(
            path="tables/%s/changesets/%s/data/create" % (table_id, changeset_id,),
            method='POST',
            json=data
        )
        return result

    def data_destroy(self, table_id, changeset_id, filters=None):
        result = self.api_request(
            path="tables/%s/changesets/%s/data/destroy" % (table_id, changeset_id,),
            method='POST',
            json={
                'filters': filters,
            }
        )

        return result

    def changeset_create(self, table_id, **kwargs):
        result = self.api_request(
            path="tables/%s/changesets/create" % (table_id),
            method='POST',
            json=kwargs,
        )
        return result

    def changeset_submit(self, table_id, changeset_id, summary=None):
        result = self.api_request(
            path="tables/%s/changesets/%s/submit" % (table_id, changeset_id,),
            method='POST',
            json={
                'summary': summary,
            }
        )
        return result

    def changeset_publish(self, table_id, changeset_id):
        result = self.api_request(
            path="tables/%s/changesets/%s/publish" % (table_id, changeset_id,),
            method='POST',
        )
        return result
