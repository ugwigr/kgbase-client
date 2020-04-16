import requests
import json
import time
import sys
import os


class Query(object):

    BASE_URL = 'http://127.0.0.1:8000/graphql'
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
        if method not in ['post', 'get', 'head']:
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
                "variables": {"data": {"username": username, "password": password}},
                "operationName": operation_name
            }
        )
        return response.text

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

    def function_name(self):
        operation_name = "operation_name"
        response = self._requests(
            method='method',
            json={
                "query": self._get_query(type='type', name=operation_name),
                "variables": None,
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

    # CreateProject - {data: {name: "Test2", isPublic: true, color: "gray"}, templateId: null}
    def create_project(self, name, is_public=False, color="gray"):
        if not name:
            raise Exception('Name required')

        operation_name = 'CreateProject'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {"data": {"name": name, "isPublic": is_public, "color": color}},
                "operationName": operation_name
            }
        )
        return response.text

    # GetProjectState - {projectId: "ctx-M4uQHCKS5WuDm0eeNDt"}
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

    # UpdateProject - {projectId: "ctx-M4uQHCKS5WuDm0eeNDt", data: {name: "Test2323", description: "12322", isPublic: false, color: "yellow"}, name: "Test2323", description: "12322", isPublic: false, color: "yellow"}
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

    # DestroyProject - {projectId: "ctx-M4uQHCKS5WuDm0eeNDt"}
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

    # GetSchema - {context: {contextId: "ctx-M4uQHCKS5WuDm0eeNDt"}}
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

    # GetGraph - variables: {
    #     context: {contextId: "ctx-M4uaGyFSWy_VCFpwaBZ"}
    #     contextId: "ctx-M4uaGyFSWy_VCFpwaBZ"
    #     query: {
    #         startingVertices: [], 
    #         labels: ["tab-M4ucjw_tyHUk-S6qayt"], 
    #         pagination: {
    #             label: "tab-M4ucjw_tyHUk-S6qayt", 
    #             offset: 0, 
    #             limit: 50
    #         }, 
    #         filters: []
    #     }
    def get_graph(self, project_id, table_id, offset=0, limit=50):
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
                        "filters": []
                    }
                },
                "operationName": operation_name
            }
        )
        return response.text
    
    # GetTask - variables: {taskId: "1856"}
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

    # CreateTable - variables: {context: {contextId: "ctx-M4uaGyFSWy_VCFpwaBZ"}, data: {displayName: "test1"}}
    def create_table(self, project_id, display_name, description, graph_shape="circle"):
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

    # UpdateTable - variables: {context: {contextId: "ctx-M4uaGyFSWy_VCFpwaBZ"}, tableId: "tab-M4ub7KPXs6hP4A1SUjL", data: {displayName: "test12", config: {graphShape: "circle", labelColumn: "col-0"}}, displayName: "test12", config: {graphShape: "circle", labelColumn: "col-0"}, graphShape: "circle", labelColumn: "col-0"}
    def update_table(self, project_id, table_id, display_name, description, graph_shape="circle"):
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

    # DeleteTable - variables: {context: {contextId: "ctx-M4uaGyFSWy_VCFpwaBZ"}, tableId: "tab-M4ub7KPXs6hP4A1SUjL", preserveRelationshipsData: false}
    def delete_table(self, project_id, table_id, preserve_relationships_data=False):
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

    # CreateColumn - variables: {
    #   context: {contextId: "ctx-M4uaGyFSWy_VCFpwaBZ"}, 
    #   tableId: "tab-M4ub7KPXs6hP4A1SUjL", 
    #   data: {displayName: "column1", dataType: "text"}, 
    #   displayName: "column1", 
    #   dataType: "text"
    # }
    # dataType: "link_one", linkedTable: "tab-M4ucjw_tyHUk-S6qayt"
    # data_type
    # text, number, boolean, url, date, date_added
    def create_column(self, project_id, table_id, display_name, data_type):
        operation_name = 'CreateColumn'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id}, 
                    "tableId": table_id,
                    "data": {"displayName": display_name, "dataType": data_type}
                },
                "operationName": operation_name
            }
        )
        return response.text

    # UpdateColumn - variables: {context: {contextId: "ctx-M4uaGyFSWy_VCFpwaBZ"}, tableId: "tab-M4ub7KPXs6hP4A1SUjL", columnId: "col-0", data: {displayName: "column12", dataType: "text"}, displayName: "column12", dataType: "text", restoreRelationshipsData: false}
    def update_column(self, project_id, table_id, column_id, display_name, data_type, restore_relationships_data=False):
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

    # DeleteColumn - variables: {context: {contextId: "ctx-M4uaGyFSWy_VCFpwaBZ"}, tableId: "tab-M4ub7KPXs6hP4A1SUjL", columnId: "col-0"}
    def delete_column(self, project_id, table_id, column_id):
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

    # CreateVertex - varaiables: {
    # context: {contextId: "ctx-M4uaGyFSWy_VCFpwaBZ"}, 
    # contextId: "ctx-M4uaGyFSWy_VCFpwaBZ", 
    # label: "tab-M4ucjw_tyHUk-S6qayt", 
    # data: {
    # values: [
    # {key: "col-0", value: "sdfsd"}, 
    # {key: "col-1", value: "123123"}
    # ], 
    # edges: []
    # }}
    def create_vertex(self, project_id, table_id, column_ids, values):
        operation_name = 'CreateVertex'
        response = self._requests(
            method='post',
            json={
                "query": self._get_query(type='mutation', name=operation_name),
                "variables": {
                    "context": {"contextId": project_id}, 
                    "label": table_id,
                    "data": {
                        "values": [
                            {
                                "key": column_id, "value": values[index]
                            } for index, column_id in enumerate(column_ids)
                        ],
                        "edges": []
                    }
                },
                "operationName": operation_name
            }
        )
        return response.text

    # UpdateVertex - varialbes: {
    # context: {contextId: "ctx-M4uaGyFSWy_VCFpwaBZ"}
    #     label: "tab-M4ucjw_tyHUk-S6qayt"
    #     vertexId: "row-M4udjwvBn25FvmYGcsL"
    #     data: {
    #       values: [{key: "col-0", value: "sdsdsdfs"}, 
    #       {key: "col-1", value: "1231231313123123"}], edges: []}
    # }
    def update_vertex(self, project_id, table_id, vertex_id, column_ids, values):
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
                        "values": [
                            {
                                "key": column_id, "value": values[index]
                            } for index, column_id in enumerate(column_ids)
                        ],
                        "edges": []
                    }
                },
                "operationName": operation_name
            }
        )
        return response.text
    
    # DeleteVertex
    def delete_vertex(self, project_id, table_id, vertex_id):
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

    # BulkDeleteVertices - variables: {
    #     context: {contextId: "ctx-M4uaGyFSWy_VCFpwaBZ"}
    #     label: "tab-M4ucjw_tyHUk-S6qayt"
    #     vertexIds: ["row-M4udjwvBn25FvmYGcsL"]
    #     deleteAll: false
    # }
    def bulk_delete_vertices(self, project_id, table_id, vertex_ids):
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

    # Upload
    # Raw Import - Upload -> BulkStartProcessing
