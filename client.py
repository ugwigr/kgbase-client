import requests

class Client(object):
    def __init__(self, api_key):
        self.base = "http://kgbase.com/api"
        self.api_key = api_key

    def create_url(self, path):
        return "%s/%s?api_key=%s" % (self.base, path, self.api_key,)

    def api_request(self, path, **kwargs):
        url = self.create_url(path)

        response = requests.post(url, **kwargs)
        if response.status_code == 200:
            return response.json()
        else:
            with open('error.html', 'w') as file:
                file.write(response.text)
            raise Exception("unexpected status code %s" % (response.status_code,))

    def create_changeset(self, table_id, summary):
        result = self.api_request("tables/%s/changesets/create" % (table_id,), json={'summary': summary})
        return result['id']

    def submit_changeset(self, table_id, changeset_id, summary):
        result = self.api_request("tables/%s/changesets/%s/submit" % (table_id, changeset_id,), json={'summary': summary})
        print "Result: %s" % (result,)

    def create_data(self, table_id, changeset_id, data):
        result = self.api_request("tables/%s/changesets/%s/data/create" % (table_id, changeset_id,), json=data)
        print "Result: %s" % (result,)
