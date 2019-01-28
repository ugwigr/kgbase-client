import requests


class Client(object):
    def __init__(self, api_key):
        # self.base = "http://kgbase.com/api"
        self.base = "http://0.0.0.0:8080/api"
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
            with open('error.html', 'w') as file:
                file.write(response.text)
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
    
    def column_create(self, project_id, table_id, **kwargs):
        result = self.api_request(
            path="projects/%s/tables/%s/columns/create" % (project_id, table_id,),
            method='POST',
            json=kwargs
        )
        return result
    
    def data_create(self, project_id, table_id, **kwargs):
        result = self.api_request(
            path="projects/%s/tables/%s/data/create" % (project_id, table_id,),
            method='POST',
            json=kwargs
        )
        return result
    
    def changeset_submit(self, project_id, table_id, changeset_id, **kwargs):
        result = self.api_request(
            path="projects/%s/tables/%s/changesets/%s/submit" % (project_id, table_id, changeset_id,),
            method='POST',
            json=kwargs
        )
        return result
    
    def changeset_publish(self, project_id, table_id, changeset_id, **kwargs):
        result = self.api_request(
            path="projects/%s/tables/%s/changesets/%s/publish" % (project_id, table_id, changeset_id,),
            method='POST',
            json=kwargs
        )
        return result
