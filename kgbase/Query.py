import requests
import json
import time
import sys
import os
import datetime


class Query(object):

    BASE_URL = 'https://kgbase.com/graphql'
    BULK_UPLOAD_URL = "https://kgbase.com/bulk/upload"
    HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Python API/1.0"
    }

    def __init__(self, proxies={}, verify=True):
        self._session = requests.session()
        self._proxies = proxies
        self._verify = verify

    def _requests(self, method, data={}, json={}, params={}):
        if method not in ['post', 'get']:
            raise Exception('Not allowed method')
        return getattr(self._session, method)(
            self.BASE_URL,
            headers=self.HEADERS,
            data=data,
            json=json,
            params=params,
            proxies=self._proxies,
            verify=self._verify
        )

    def _get_query(self, type, name):
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'graphql',
            type,
            "{name}.graphql".format(name=name)
        )
        f = open(file_path, 'r')
        return f.read()

    # User & Authentication
    # LoginUser
    def login(self, username, password):
        if not username:
            raise Exception('Username required')
        if not password:
            raise Exception('Password required')
        operation_name = 'LoginUser'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "data": {
                        "username": username, 
                        "password": password
                    }
                },
                "operationName": operation_name
            }
        )
        self._organization_id = json.loads(response.text).get("data", {}).get("loginUser", {}).get("user", {}).get("nickname")
        return response.text

    # GetUserState
    def get_user_state(self):
        operation_name = 'GetUserState'
        response = self._requests(
            method='get',
            json={
                "query": self._get_query(type='query', name=operation_name),
                "variables": None,
                "operationName": operation_name
            }
        )
        return response.text

    # LogoutUser
    def logout(self):
        operation_name = 'LogoutUser'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": None,
                "operationName": operation_name
            }
        )
        return response.text

    # GetSchema
    def get_schema(self, project_id):
        if not project_id:
            raise Exception('Project ID required')
        operation_name = 'GetSchema'
        response = self._requests(
            method='get',
            json={
                "query": self._get_query(type='query', name=operation_name),
                "variables": {"context": {"contextId": project_id}},
                "operationName": operation_name
            }
        )
        return response.text

    # GetGraph
    def get_graph(self, project_id, table_id, filters=[], offset=0, limit=50):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        operation_name = 'GetGraph'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='query', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id},
                    "contextId": project_id,
                    "query": {
                        "startingVertices": [], 
                        "labels": [table_id], 
                        "pagination": {
                            "label": table_id, 
                            "offset": offset, 
                            "limit": limit
                        }, 
                        "filters": [dict({"label": table_id}, **filter) for filter in filters],
                    }
                },
                "operationName": operation_name
            }
        )
        return response.text

    # SummarizeGraph
    def summarize_graph(self, project_id, table_id, filters=[], groups=[], aggregations=[], offset=0, limit=50):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        operation_name = 'SummarizeGraph'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='query', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id},
                    "contextId": project_id,
                    "query": {
                        "startingVertices": [],
                        "labels": [table_id],
                        "pagination": {
                            "label": table_id,
                            "offset": offset,
                            "limit": limit
                        },
                        "filters": [dict({"label": table_id}, **filter) for filter in filters],
                        "summary": {
                            "label": table_id,
                            "groups": groups,
                            "aggregations": aggregations
                        }
                    }
                },
                "operationName": operation_name
            }
        )
        return response.text
    
    # GetTask
    def get_task(self, task_id):
        if not task_id:
            raise Exception('Task ID required')
        operation_name = 'GetTask'
        response = self._requests(
            method='get',
            json={
                "query": self._get_query(type='query', name=operation_name),
                "variables": {"taskId": task_id},
                "operationName": operation_name
            }
        )
        return response.text

    # Projects
    # GetPublicProjects
    def get_public_projects(self):
        operation_name = "GetPublicProjects"
        response = self._requests(
            method='get',
            json={
                "query": self._get_query(type='query', name=operation_name),
                "variables": None,
                "operationName": operation_name
            }
        )
        return response.text

    # GetTeamProjects
    def get_team_projects(self):
        operation_name = "GetTeamProjects"
        response = self._requests(
            method='get',
            json={
                "query": self._get_query(type='query', name=operation_name),
                "variables": None,
                "operationName": operation_name
            }
        )
        return response.text

    # GetFavoriteProjects
    def get_favorite_projects(self):
        operation_name = "GetFavoriteProjects"
        response = self._requests(
            method='get',
            json={
                "query": self._get_query(type='query', name=operation_name),
                "variables": None,
                "operationName": operation_name
            }
        )
        return response.text

    # GetUserProjects
    def get_user_projects(self):
        operation_name = "GetUserProjects"
        response = self._requests(
            method='get',
            json={
                "query": self._get_query(type='query', name=operation_name),
                "variables": None,
                "operationName": operation_name
            }
        )
        return response.text

    # CreateProject
    def create_project(self, name, is_public=False, color="gray"):
        if not name:
            raise Exception('Name required')
        operation_name = 'CreateProject'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "data": {
                        "name": name,
                        "isPublic": is_public,
                        "color": color
                    }
                },
                "operationName": operation_name
            }
        )
        return response.text

    # GetProjectState
    def get_project_state(self, project_id):
        if not project_id:
            raise Exception('Project ID required')
        operation_name = "GetProjectState"
        response = self._requests(
            method='get',
            json={
                "query": self._get_query(type='query', name=operation_name),
                "variables": {"projectId": project_id},
                "operationName": operation_name
            }
        )
        return response.text

    # UpdateProject
    def update_project(self, project_id, name, is_public=False, color="gray"):
        if not project_id:
            raise Exception('Project ID required')
        if not name:
            raise Exception('Name required')
        operation_name = 'UpdateProject'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "projectId": project_id,
                    "data": {"name": name, "isPublic": is_public, "color": color}
                },
                "operationName": operation_name
            }
        )
        return response.text

    # DestroyProject
    def destroy_project(self, project_id):
        if not project_id:
            raise Exception('Project ID required')
        operation_name = 'DestroyProject'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {"projectId": project_id},
                "operationName": operation_name
            }
        )
        return response.text

    # Table
    # CreateTable
    def create_table(self, project_id, display_name, description='', graph_shape="circle"):
        if not project_id:
            raise Exception('Project ID required')
        if not display_name:
            raise Exception('Display Name required')
        operation_name = 'CreateTable'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id}, 
                    "data": {
                        "displayName": display_name,
                        "config": {
                            "graphShape": graph_shape,
                            "description": description
                        }
                    }},
                "operationName": operation_name
            }
        )
        return response.text

    # UpdateTable
    def update_table(self, project_id, table_id, display_name, description='', graph_shape="circle"):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        if not display_name:
            raise Exception('Display Name required')
        operation_name = 'UpdateTable'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id}, 
                    "tableId": table_id,
                    "data": {
                        "displayName": display_name,
                        "config": {
                            "graphShape": graph_shape,
                            "description": description
                        }
                    }
                },
                "operationName": operation_name
            }
        )
        return response.text

    # DeleteTable
    def delete_table(self, project_id, table_id, preserve_relationships_data=False):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        operation_name = 'DeleteTable'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id}, 
                    "tableId": table_id,
                    "preserveRelationshipsData": preserve_relationships_data
                },
                "operationName": operation_name
            }
        )
        return response.text

    # CreateColumn
    def create_column(self, project_id, table_id, display_name, data_type, linked_table=None):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        if not display_name:
            raise Exception('Display Name required')
        if not data_type:
            raise Exception('Data Type required')
        if data_type not in ['text', 'number', 'boolean', 'url', 'date', 'date_added', 'link_one', 'link_many']:
            raise Exception('Invalid Data Type')
        operation_name = 'CreateColumn'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id}, 
                    "tableId": table_id,
                    "data": {
                        "displayName": display_name, 
                        "dataType": data_type, 
                        "linkedTable": linked_table
                    } if data_type in ['link_one', 'link_many'] else {
                        "displayName": display_name, 
                        "dataType": data_type
                    }
                },
                "operationName": operation_name
            }
        )
        return response.text

    # UpdateColumn
    def update_column(self, project_id, table_id, column_id, display_name, data_type, linked_table=None, restore_relationships_data=False):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        if not column_id:
            raise Exception('Column ID required')
        if not display_name:
            raise Exception('Display Name required')
        if not data_type:
            raise Exception('Data Type required')
        if data_type not in ['text', 'number', 'boolean', 'url', 'date', 'date_added', 'link_one', 'link_many']:
            raise Exception('Invalid Data Type')
        operation_name = 'UpdateColumn'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id}, 
                    "tableId": table_id,
                    "columnId": column_id,
                    "data": {
                        "displayName": display_name,
                        "dataType": data_type
                    },
                    "restoreRelationshipsData": False
                },
                "operationName": operation_name
            }
        )
        return response.text

    # DeleteColumn
    def delete_column(self, project_id, table_id, column_id):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        if not column_id:
            raise Exception('Column ID required')
        operation_name = 'DeleteColumn'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id}, 
                    "tableId": table_id,
                    "columnId": column_id,                
                },
                "operationName": operation_name
            }
        )
        return response.text

    # CreateVertex
    def create_vertex(self, project_id, table_id, column_ids, values, edges):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        if not column_ids:
            raise Exception('Column IDs required')
        if not values:
            raise Exception('Values required')

        data_values = []
        for index, column_id in enumerate(column_ids):
            if isinstance(values[index], bool):
                value = str(values[index]).lower()
            elif isinstance(values[index], (datetime.datetime, datetime.date)):
                value = values[index].strftime('%Y%m%dT%H%M%S')
            else:
                value = str(values[index])
            data_values.append({
                "key": column_id,
                "value": value
            })

        data_edges = []
        for label, to_id in edges:
            data_edges.append({
                "label": label,
                "toId": to_id
            })

        operation_name = 'CreateVertex'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id}, 
                    "label": table_id,
                    "data": {
                        "values": data_values,
                        "edges": data_edges,
                    }
                },
                "operationName": operation_name
            }
        )
        return response.text

    # UpdateVertex
    def update_vertex(self, project_id, table_id, vertex_id, column_ids, values, edges):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        if not vertex_id:
            raise Exception('Vertex ID required')
        if not column_ids:
            raise Exception('Column IDs required')
        if not values:
            raise Exception('Values required')

        data_values = []
        for index, column_id in enumerate(column_ids):
            if isinstance(values[index], bool):
                value = str(values[index]).lower()
            elif isinstance(values[index], (datetime.datetime, datetime.date)):
                value = values[index].strftime('%Y%m%dT%H%M%S')
            else:
                value = str(values[index])
            data_values.append({
                "key": column_id,
                "value": value
            })

        data_edges = []
        for label, to_id in edges:
            data_edges.append({
                "label": label,
                "toId": to_id
            })

        operation_name = 'UpdateVertex'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id}, 
                    "label": table_id,
                    "vertexId": vertex_id,
                    "data": {
                        "values": data_values,
                        "edges": data_edges
                    }
                },
                "operationName": operation_name
            }
        )
        return response.text
    
    # DeleteVertex
    def delete_vertex(self, project_id, table_id, vertex_id):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        if not vertex_id:
            raise Exception('Vertex ID required')
        operation_name = 'DeleteVertex'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id}, 
                    "label": table_id,
                    "vertexId": vertex_id
                },
                "operationName": operation_name
            }
        )
        return response.text

    # BulkDeleteVertices
    def bulk_delete_vertices(self, project_id, table_id, vertex_ids):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        if not vertex_ids:
            raise Exception('Vertex IDs required')
        operation_name = 'BulkDeleteVertices'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id}, 
                    "label": table_id,
                    "vertexIds": vertex_ids,
                    "deleteAll": False
                },
                "operationName": operation_name
            }
        )
        return response.text

    # Bulk Upload
    def bulk_upload(self, project_id, filepaths):
        if not project_id:
            raise Exception('Project ID required')
        if not filepaths:
            raise Exception('CSV Files required')
        
        # Upload
        multipart_form_data = []
        for filepath in filepaths:
            multipart_form_data.append(
                ('files', (filepath.split('/')[-1], open(filepath, 'rb'))))
        multipart_form_data = tuple(multipart_form_data)

        response = self._session.post(
            self.BULK_UPLOAD_URL,
            files=multipart_form_data,
            data={
                "organization_id": self._organization_id,
                "project_id": project_id,
                "file_type": "csv"
            }
        )
        if response.status_code != 200:
            raise Exception('Something went wrong')
        bundle_id = json.loads(response.content)['bundle_id']

        operation_name = 'BulkStartProcessing'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "bundleId": bundle_id,
                },
                "operationName": operation_name
            }
        )
        if response.status_code != 200:
            raise Exception('Something went wrong')

        status = 'running'
        while status != 'finished' and status != 'failed':
            operation_name = 'GetBulkBundle'
            response = self._requests(
                method='post',
                json={
                    "query": self._get_query(type='query', name=operation_name),
                    "variables": {
                        "bundleId": bundle_id,
                    },
                    "operationName": operation_name
                }
            )
            status = json.loads(response.text).get('data', {}).get('getBulkBundle', {}).get('status')
            time.sleep(5)
        return response.text
