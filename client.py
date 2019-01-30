import requests


class Client(object):
    def __init__(self, api_key, base=None):
        if base:
            self.base = base
        else:
            self.base = "https://kgbase.com/api"
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
            # print(response.text)
            raise Exception("unexpected status code %s" % (response.status_code,))

    def project_list(self):
        result = self.api_request(
            path="projects",
            method='GET'
        )
        return result

    def project_create(self, **kwargs):
        result = self.api_request(
            path="projects/create",
            method='POST',
            json=kwargs
        )
        return result

    def table_list(self, project_id, **kwargs):
        result = self.api_request(
            path="projects/%s/tables" % (project_id,),
            method='GET',
            json=kwargs
        )
        return result

    def table_create(self, project_id, **kwargs):
        result = self.api_request(
            path="projects/%s/tables/create" % (project_id,),
            method='POST',
            json=kwargs
        )
        return result

    def column_create(self, table_id, **kwargs):
        result = self.api_request(
            path="tables/%s/columns/create" % (table_id,),
            method='POST',
            json=kwargs
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

    def data_create(self, table_id, changeset_id, data):
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

    def changeset_create(self, project_id, summary=None):
        result = self.api_request(
            path="projects/%s/changesets/create" % (project_id),
            method='POST',
            json={
                'summary': summary,
            },
        )

        return result['id']

    def changeset_submit(self, changeset_id, summary=None):
        result = self.api_request(
            path="changesets/%s/submit" % (changeset_id,),
            method='POST',
            json={
                'summary': summary,
            }
        )
        return result

    def changeset_publish(self, changeset_id):
        result = self.api_request(
            path="changesets/%s/publish" % (changeset_id,),
            method='POST',
        )
        return result
