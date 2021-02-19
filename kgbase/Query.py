import requests
import json
import time
import sys
import os
import datetime
import platform
import csv


class Query(object):

    BASE_URL = 'https://www.kgbase.com/kgbase-query'
    BULK_UPLOAD_URL = "https://www.kgbase.com/bulk/upload"
    HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Python API 0.31 / {local_version}".format(local_version=platform.python_version())
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

    def _validate_response(self, response_text, operation_name):
        json_response = json.loads(response_text)
        if json_response.get("errors"):
            raise Exception(json_response["errors"][0]["message"])

        response = json_response.get("data").get(operation_name)
        if isinstance(response, dict) and response.get("error"):
            raise Exception(response["error"])

    def _parse_response(self, response_text, operation_name):
        return json.loads(response_text).get("data").get(operation_name)

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
        self._validate_response(response.text, 'loginUser')
        self._organization_id = json.loads(response.text).get("data", {}).get("loginUser", {}).get("user", {}).get("nickname")
        return self._parse_response(response.text, 'loginUser')

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
        self._validate_response(response.text, 'currentUser')
        return self._parse_response(response.text, 'currentUser')

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
        self._validate_response(response.text, 'logoutUser')
        return self._parse_response(response.text, 'logoutUser')

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
        return self._parse_response(response.text, 'getSchema')

    # GetGraph
    def get_graph(self, project_id, table_id=None, filters=[], offset=0, limit=50):
        if not project_id:
            raise Exception('Project ID required')
        operation_name = 'GetGraph'
        if table_id:
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
        else:
            response = self._requests(
                method='post',
                json={
                    "query": self._get_query(type='query', name=operation_name),
                    "variables": {
                        "context": {"contextId": project_id},
                        "query": {
                            "derivedColumns": [],
                            "filters": [],
                            "startingVertices": []
                        },
                        "limit": {"samplingMethod": "random"}
                    },
                    "operationName": operation_name
                }
            )
        return self._parse_response(response.text, 'getGraph')

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
        return self._parse_response(response.text, 'summarizeGraph')
    
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
        return self._parse_response(response.text, 'getTask')

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
        self._validate_response(response.text, 'publicProjects')
        return self._parse_response(response.text, 'publicProjects')

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
        self._validate_response(response.text, 'teamProjects')
        return self._parse_response(response.text, 'teamProjects')

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
        self._validate_response(response.text, 'favoriteProjects')
        return self._parse_response(response.text, 'favoriteProjects')

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
        self._validate_response(response.text, 'userProjects')
        return self._parse_response(response.text, 'userProjects')

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
        self._validate_response(response.text, 'createProject')
        return self._parse_response(response.text, 'createProject')

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
        self._validate_response(response.text, 'project')
        return self._parse_response(response.text, 'project')

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
        self._validate_response(response.text, 'updateProject')
        return self._parse_response(response.text, 'updateProject')

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
        self._validate_response(response.text, 'destroyProject')
        return self._parse_response(response.text, 'destroyProject')

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
        self._validate_response(response.text, 'createTable')
        return self._parse_response(response.text, 'createTable')

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
        self._validate_response(response.text, 'updateTable')
        return self._parse_response(response.text, 'updateTable')

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
        self._validate_response(response.text, 'deleteTable')
        return self._parse_response(response.text, 'deleteTable')

    # CreateColumn
    def create_column(self, project_id, table_id, display_name, data_type, linked_table=None, is_required=False):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        if not display_name:
            raise Exception('Display Name required')
        if not data_type:
            raise Exception('Data Type required')
        if data_type not in ['text', 'number', 'boolean', 'url', 'date', 'date_added', 'link_one', 'link_many', 'image', 'image_url']:
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
                        "linkedTable": linked_table,
                        "isRequired": is_required
                    } if data_type in ['link_one', 'link_many'] else {
                        "displayName": display_name, 
                        "dataType": data_type,
                        "isRequired": is_required
                    }
                },
                "operationName": operation_name
            }
        )
        self._validate_response(response.text, 'createColumn')
        return self._parse_response(response.text, 'createColumn')

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
        if data_type not in ['text', 'number', 'boolean', 'url', 'date', 'date_added', 'link_one', 'link_many', 'image', 'image_url']:
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
        self._validate_response(response.text, 'updateColumn')
        return self._parse_response(response.text, 'updateColumn')

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
        self._validate_response(response.text, 'deleteColumn')
        return self._parse_response(response.text, 'deleteColumn')

    # CreateVertex
    def create_vertex(self, project_id, table_id, values, edges):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        if not values:
            raise Exception('Values required')

        data_values = []
        for column_id, value in values.items():
            if isinstance(value, bool):
                value = str(value).lower()
            elif isinstance(value, (datetime.datetime, datetime.date)):
                value = value.strftime('%Y%m%dT%H%M%S')
            else:
                value = str(value)
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
        self._validate_response(response.text, 'createVertex')
        return self._parse_response(response.text, 'createVertex')

    # UpdateVertex
    def update_vertex(self, project_id, table_id, vertex_id, values, edges):
        if not project_id:
            raise Exception('Project ID required')
        if not table_id:
            raise Exception('Table ID required')
        if not vertex_id:
            raise Exception('Vertex ID required')
        if not values:
            raise Exception('Values required')

        data_values = []
        for column_id, value in values.items():
            if isinstance(value, bool):
                value = str(value).lower()
            elif isinstance(value, (datetime.datetime, datetime.date)):
                value = value.strftime('%Y%m%dT%H%M%S')
            else:
                value = str(value)
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
        self._validate_response(response.text, 'updateVertex')
        return self._parse_response(response.text, 'updateVertex')
    
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
        self._validate_response(response.text, 'deleteVertex')
        return self._parse_response(response.text, 'deleteVertex')

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
        self._validate_response(response.text, 'bulkDeleteVertices')
        return self._parse_response(response.text, 'bulkDeleteVertices')

    # Bulk Upload
    def bulk_upload(self, project_id, table_id, filepath, column_ids, configs={}):
        if not project_id:
            raise Exception('Project ID required')
        if not filepath:
            raise Exception('CSV Files required')

        csv_file = open(filepath)
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) != len(column_ids):
                raise Exception('Number of column ids not matched with csv file')
            break

        # Upload
        multipart_form_data = []
        multipart_form_data.append(('files', (filepath.split('/')[-1], open(filepath, 'rb'))))
        multipart_form_data = tuple(multipart_form_data)
        response = self._session.post(
            self.BULK_UPLOAD_URL,
            files=multipart_form_data,
            data={
                "organization_id": self._organization_id,
                "project_id": project_id,
                "file_type": "single_csv"
            }
        )
        if response.status_code != 200:
            raise Exception('Something went wrong in uploading csv file')
        bundle_id = json.loads(response.content)['bundle_id']
        if not bundle_id:
            raise Exception('Bundle id not found')

        operation_name = 'BulkStartImport'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "bundleId": bundle_id,
                    "context": {"contextId": project_id},
                    "sheetConfigs": [{
                        "columnMap": [{"csvColumnIndex": i, "mappedColumnId": column_id, "wantsCreate": False} for i, column_id in enumerate(column_ids) if column_id is not None],
                        "countSkipRows": configs.get("countSkipRows", 0),
                        "dropEmpty": configs.get("dropEmpty", False),
                        "hasHeader": configs.get("hasHeader", False),
                        "sheetName": "default",
                        "targetTable": table_id
                    }]
                },
                "operationName": operation_name
            }
        )
        self._validate_response(response.text, 'bulkStartImport')
        task_id = json.loads(response.text).get('data', {}).get('bulkStartImport', {}).get('taskId')
        if not task_id:
            raise Exception('Task id not found')

        status = 'queued'
        while status != 'finished' and status != 'failed':
            operation_name = 'GetTask'
            response = self._requests(
                method='post',
                json={
                    "query": self._get_query(type='query', name=operation_name),
                    "variables": {
                        "taskId": task_id,
                    },
                    "operationName": operation_name
                }
            )
            self._validate_response(response.text, 'getTask')
            status = json.loads(response.text).get('data', {}).get('getTask', {}).get('status')
            progress = json.loads(response.text).get('data', {}).get('getTask', {}).get('progress')
            print ("progress", progress)
            time.sleep(2)
        return self._parse_response(response.text, 'getTask')
