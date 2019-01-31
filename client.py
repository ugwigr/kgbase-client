import requests


class Client(object):
    def __init__(self, api_key, base='https://kgbase.com/api'):
        '''
        Args:
            api_key - User API Key
            base - https://kgbase.com/api (default)
        '''
        self.base = base
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
        '''
        Args:
            NA

        Returns:
            user_projects
                id
                is_public
                slug
                name
                description

            public_projects
                id
                is_public
                slug
                name
                description
        '''
        result = self.api_request(
            path="projects",
            method='GET'
        )
        return result

    def project_create(self, name, description, is_public):
        '''
        Args:
            name
            description
            is_public

        Returns:
            id
            is_public
            slug
            name
            description
        '''
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
        '''
        Args:
            project_id

        Returns:
            respository_name
            slug
            description
            name
        '''
        result = self.api_request(
            path="projects/%s/tables" % (project_id,),
            method='GET',
        )
        return result

    def table_create(self, project_id, name, description):
        '''
        Args:
            project_id
            name
            description

        Returns:
            table
                name
                repository_name
                slug
                description
        '''
        result = self.api_request(
            path="projects/%s/tables/create" % (project_id,),
            method='POST',
            json={
                'name': name,
                'description': description,
            }
        )
        return result

    def column_create(self, table_id, name, column_type, is_unique, changeset_id, target_table=None):
        '''
        Args:
            table_id
            name
            column_type
            is_unique
            changeset_id
            target_table (optional)
        
        Returns:
            changeset_id
        '''
        result = self.api_request(
            path="tables/%s/changesets/%s/columns/create" % (table_id, changeset_id),
            method='POST',
            json={
                'name': name,
                'type': column_type,
                'is_unique': is_unique,
            } if column_type != 'foreign_key' else {
                'name': name,
                'type': column_type,
                'is_unique': is_unique,
                'target_table': target_table,
            }
        )
        return result

    def data_list(self, changeset_id, table_id, filters=None):
        '''
        Args:
            changeset_id
            table_id
            filters (Optional)
        
        Returns:
            rows
        '''
        result = self.api_request(
            path="changesets/%s/tables/%s/data/list" % (changeset_id, table_id,),
            method='POST',
            json={
                'filters': filters,
            }
        )
        return result

    def data_create(self, changeset_id, table_id, data):
        '''
        Args:
            changeset_id
            table_id
            data
        
        Return
            data
            id
        '''
        result = self.api_request(
            path="changesets/%s/tables/%s/data/create" % (changeset_id, table_id,),
            method='POST',
            json=data
        )
        return result

    def data_update(self, changeset_id, table_id, row_id, data):
        '''
        Args:
            changeset_id
            table_id
            row_id
            data
        Return
            data
            id
        '''
        result = self.api_request(
            path="changesets/%s/tables/%s/data/%s/update" % (changeset_id, table_id, row_id,),
            method='POST',
            json=data
        )
        return result

    def data_destroy(self, changeset_id, table_id, filters=None):
        '''
        Args:
            changeset_id
            table_id

        Returns:
            NA
        '''

        result = self.api_request(
            path="changesets/%s/tables/%s/data/destroy" % (changeset_id, table_id,),
            method='POST',
            json={
                'filters': filters,
            }
        )
        return result

    def changeset_create(self, project_id, summary):
        '''
        Args:
            project_id
            summary

        Returns:
            id
            branch_name
            summary
        '''
        result = self.api_request(
            path="projects/%s/changesets/create" % (project_id),
            method='POST',
            json={
                'summary': summary,
            },
        )
        return result

    def changeset_submit(self, changeset_id, summary=None):
        '''
        Args:
            changeset_id
            summary

        Returns:
            changeset_id
        '''
        result = self.api_request(
            path="changesets/%s/submit" % (changeset_id,),
            method='POST',
            json={
                'summary': summary,
            }
        )
        return result

    def changeset_publish(self, changeset_id):
        '''
        Args:
            changeset_id
        Returns:
            changeset_id
        '''
        result = self.api_request(
            path="changesets/%s/publish" % (changeset_id,),
            method='POST',
        )
        return result
