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
        result = self.api_request("projects", method='GET')
        return result

    def project_create(self, **kwargs):
        result = self.api_request(path="projects/create", method='POST', json=kwargs)
        return result

    def create_changeset(self, table_id, summary):
        result = self.api_request("tables/%s/changesets/create" % (table_id,), json={'summary': summary})
        return result['id']

    def submit_changeset(self, table_id, changeset_id, summary):
        result = self.api_request("tables/%s/changesets/%s/submit" % (table_id, changeset_id,), json={'summary': summary})
        print "Result: %s" % (result,)

    def create_data(self, table_id, changeset_id, data):
        result = self.api_request("tables/%s/changesets/%s/data/create" % (table_id, changeset_id,), json=data)
        print "Result: %s" % (result,)

