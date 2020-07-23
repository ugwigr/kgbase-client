from kgbase import Query
import datetime
import json


# TODO
# csv upload
# raw import

if __name__ == "__main__":
    # q = Query()
    # result = q.login(
    #     username='sangwon.seo@thinknum.com',
    #     password='1'
    # )

    q = Query()
    result = q.login(
        username='sangwon.seo@thinknum.com',
        password='10Worldcup!'
    )
    print (result)
    '''
    {
        "data": {
            "loginUser": {
                "ok": true,
                "user": {
                    "uuid": null,
                    "graphqlId": "User/1",
                    "username": "sangwon.seo@thinknum.com",
                    "name": "Sangwon Seo",
                    "avatarUrl": "https://kgbase.s3.amazonaws.com/profile_pictures/2019/12/KakaoTalk_Photo_2019-12-23-08-51-51.jpeg",
                    "nickname": "sangwonseo",
                    "apiKey": "w2gJRyzNwB",
                    "isStaff": true,
                    "lastActivityAt": "2020-04-16T20: 41: 12.897637+00: 00"
                },
                "error": null
            }
        }
    }
    '''

    # result = q.get_user_state()
    # print (result)
    '''
    {
        "data": {
            "currentUser": {
                "uuid": null,
                "graphqlId": "User/1",
                "username": "sangwon.seo@thinknum.com",
                "name": "Sangwon Seo",
                "avatarUrl": "https://kgbase.s3.amazonaws.com/profile_pictures/2019/12/KakaoTalk_Photo_2019-12-23-08-51-51.jpeg",
                "nickname": "sangwonseo",
                "apiKey": "w2gJRyzNwB",
                "isStaff": true,
                "lastActivityAt": "2020-04-16T20: 41: 12.897637+00: 00"
            }
        }
    }
    '''

    # result = q.logout()
    # print (result)
    '''
    {
        "data": {
            "logoutUser": {
                "ok": true
            }
        }
    }
    '''

    # result = q.get_public_projects()
    # print (result)

    # result = q.get_team_projects()
    # print (result)

    # result = q.get_favorite_projects()
    # print (result)

    # result = q.get_user_projects()
    # print (result)
    '''
    {
        "data": {
            "publicProjects": [
                {
                    "uuid": "f08d0007-0908-4edb-beeb-87ee5e41344b",
                    "graphqlId": "Project/266",
                    "projectId": "cz05qj1k5zo4puif",
                    "name": "clinicaltrials",
                    "description": "",
                    "updatedAt": "2019-12-13T06:27:42.614425+00:00",
                    "dataChangedAt": null,
                    "color": "gray",
                    "slug": "clinicaltrials",
                    "owner": {
                        "ownerType": "USER",
                        "name": "Health Knowledge",
                        "slug": "healthknow",
                        "avatarUrl": null
                    },
                    "isPublic": true,
                    "collaborators": [
                        {
                            "uuid": "1349191d-4cf2-4db7-8f1b-30d4535fd915",
                            "graphqlId": "User/36",
                            "username": "stella.weng@thinknum.com",
                            "name": "StellaWeng",
                            "avatarUrl": "https: //kgbase.s3.amazonaws.com/profile_pictures/2019/12/WX20191107-100351.png",
                            "nickname": "stellaweng",
                            "apiKey": null,
                            "isStaff": true,
                            "lastActivityAt": "2020-04-16T19:26:04.589058+00:00"
                        }
                    ],
                    "apiUsers": [],
                    "favoritesCount": 1,
                    "canManage": false
                }
            ]
        }
    }
    '''

    # result = q.create_project(
    #     name='test-api', 
    #     is_public=True, 
    # )
    # print (result)
    '''
    {
        "data": {
            "createProject": {
                "ok": true,
                "project": {
                    "uuid": "a0406c6d-122a-4ff2-af7f-976ba5cbca01",
                    "graphqlId": "Project/1509",
                    "projectId": "ctx-M53lgnjpCkc_plt0lqo",
                    "name": "test-api",
                    "description": null,
                    "updatedAt": "2020-04-16T20:55:53.329530+00:00",
                    "dataChangedAt": "2020-04-16T20:55:53.329296",
                    "color": "gray",
                    "slug": "test-api-lw",
                    "owner": {
                        "ownerType": "USER",
                        "name": "Sangwon Seo",
                        "slug": "sangwonseo",
                        "avatarUrl": "https: //kgbase.s3.amazonaws.com/profile_pictures/2019/12/KakaoTalk_Photo_2019-12-23-08-51-51.jpeg"
                    },
                    "isPublic": true,
                    "collaborators": [],
                    "apiUsers": [],
                    "favoritesCount": 0,
                    "canManage": true
                }
            }
        }
    }
    '''

    # result = q.get_project_state(
    #     project_id='ctx-MCxWvNH-NPIaFmE6OQH'
    # )
    # print (result)
    '''
    {
        "data": {
            "project": {
                "uuid": "a0406c6d-122a-4ff2-af7f-976ba5cbca01",
                "graphqlId": "Project/1509",
                "projectId": "ctx-M53lgnjpCkc_plt0lqo",
                "name": "test-api",
                "description": null,
                "updatedAt": "2020-04-16T20:55:53.329530+00:00",
                "dataChangedAt": "2020-04-16T20:55:53.329296+00:00",
                "color": "gray",
                "slug": "test-api-lw",
                "owner": {
                    "ownerType": "USER",
                    "name": "Sangwon Seo",
                    "slug": "sangwonseo",
                    "avatarUrl": "https: //kgbase.s3.amazonaws.com/profile_pictures/2019/12/KakaoTalk_Photo_2019-12-23-08-51-51.jpeg"
                },
                "isPublic": true,
                "collaborators": [],
                "apiUsers": [],
                "favoritesCount": 0,
                "canManage": true
            },
            "isOwnerOrMember": true,
            "canManageProject": true,
            "canRead": true,
            "canWrite": true,
            "hasRequestedAccess": false,
            "isProjectFavorited": false,
            "wantsNotifications": null
        }
    }
    '''

    # result = q.update_project(
    #     project_id='ctx-MCxWvNH-NPIaFmE6OQH', 
    #     name='test-api-v2', 
    #     is_public=False
    # )
    # print (result)
    '''
    {
        "data": {
            "updateProject": {
                "ok": true,
                "project": {
                    "uuid": "a0406c6d-122a-4ff2-af7f-976ba5cbca01",
                    "graphqlId": "Project/1509",
                    "projectId": "ctx-M53lgnjpCkc_plt0lqo",
                    "name": "test-api-v2",
                    "description": null,
                    "updatedAt": "2020-04-16T20:58:12.252444+00:00",
                    "dataChangedAt": "2020-04-16T20:58:12.252324",
                    "color": "gray",
                    "slug": "test-api-v2",
                    "owner": {
                        "ownerType": "USER",
                        "name": "Sangwon Seo",
                        "slug": "sangwonseo",
                        "avatarUrl": "https://kgbase.s3.amazonaws.com/profile_pictures/2019/12/KakaoTalk_Photo_2019-12-23-08-51-51.jpeg"
                    },
                    "isPublic": false,
                    "collaborators": [],
                    "apiUsers": [],
                    "favoritesCount": 0,
                    "canManage": true
                }
            }
        }
    }
    '''

    # result = q.destroy_project(
    #     project_id='ctx-MCxWvNH-NPIaFmE6OQH'
    # )
    # print (result)
    '''
    {
        "data": {
            "destroyProject": {
                "ok": true
            }
        }
    }
    '''

    # result = q.create_table(
    #     project_id='ctx-MCxXEVZjyndWiHH7VPY',
    #     display_name='api-test',
    #     description='Api test'
    # )
    # print (result)
    '''
    {
        "data": {
            "createTable": {
                "ok": true,
                "tableId": "tab-M53nDu1y1SXMVA_ny97"
            }
        }
    }
    '''

    # result = q.update_table(
    #     project_id='ctx-MCxXEVZjyndWiHH7VPY',
    #     table_id='tab-MCxXOmTENzVaAZUdDGR',
    #     display_name='api-table2',
    #     description='asdfsdfs',
    # )
    # print (result)
    '''
    {
        "data": {
            "updateTable": {
                "ok": true
            }
        }
    }
    '''

    # result = q.delete_table(
    #     project_id='ctx-MCxXEVZjyndWiHH7VPY',
    #     table_id='tab-MCxWDQtyYHrv12o3-id',
    # )
    # print (result)
    '''
    {
        "data": {
            "deleteTable": {
                "ok": true,
                "taskId": "1931"
            }
        }
    }
    '''

    # result = q.create_column(
    #     project_id='ctx-MCxXEVZjyndWiHH7VPY',
    #     table_id='tab-MCxXOmTENzVaAZUdDGR',
    #     display_name='api_column',
    #     data_type='text'
    # )
    # print (result)

    # result = q.update_column(
    #     project_id='ctx-MCxXEVZjyndWiHH7VPY',
    #     table_id='tab-MCxXOmTENzVaAZUdDGR',
    #     column_id='col-0',
    #     display_name='api-column0',
    #     data_type='text'
    #     # data_type='link_one',
    #     # linked_table='tab-dfj23eijSFdfewf'
    # )
    # print (result)
    '''
    {
        "data": {
            "createColumn": {
                "ok": true,
                "columnId": "col-1"
            }
        }
    }
    '''

    # text, number, boolean, url, date, date_added, link_one, link_many
    # result = q.update_column(
    #     project_id='ctx-MCxXEVZjyndWiHH7VPY',
    #     table_id='tab-MCxXOmTENzVaAZUdDGR',
    #     column_id='col-0',
    #     display_name='api-column10',
    #     data_type='number'
    # )
    # result = q.update_column(
    #     project_id='ctx-MCxWvNH-NPIaFmE6OQH',
    #     table_id='tab-M5NlqLNJdGIrk5uFI4m',
    #     column_id='col-0',
    #     display_name='api-column10',
    #     data_type='link_one',
    #     linked_table='tab-dfj23eijSFdfewf'
    # )
    # print (result)
    '''
    {
        "data": {
            "updateColumn": {
                "ok": true,
                "taskId": null
            }
        }
    }
    '''
    
    # result = q.delete_column(
    #     project_id='ctx-M5Na8A_zgK3m455pp-r',
    #     table_id='tab-M5Nb1-JqUtsb-SwpnH3',
    #     column_id='col-0',
    # )
    # print (result)
    # '''
    # {
    #     "data": {
    #         "deleteColumn": {
    #             "ok": true
    #         }
    #     }
    # }
    # '''

    # result = q.create_vertex(
    #     project_id='ctx-MCxXEVZjyndWiHH7VPY',
    #     table_id='tab-MCxXOmTENzVaAZUdDGR',
    #     values={
    #         'col-0': 'Palantir',                  # text
    #         # 'col-1': 1,                      # number
    #         # 'col-2': False,                     # boolean
    #         # 'col-3': 'https://google.com',      # url
    #         # 'col-4': datetime.datetime.today()  # date
    #         # 'col-5'     # date_added
    #     },
    #     edges=[]
    # )
    # print (result)

    # result = q.create_vertex(
    #     project_id='ctx-MCxWvNH-NPIaFmE6OQH',
    #     table_id='tab-M5Nm23_krbcQHdBqWh-',
    #     values={
    #         # 'col-0': 'Google',                  # text
    #         'col-0': 'Shopify',                      # number
    #         # 'col-2': False,                     # boolean
    #         # 'col-3': 'https://google.com',      # url
    #         # 'col-4': datetime.datetime.today()  # date
    #         # 'col-5'     # date_added
    #     },
    #     edges=[]
    # )
    # print (result)

    # result = q.create_vertex(
    #     project_id='ctx-M5Na8A_zgK3m455pp-r',
    #     table_id='tab-M5Nb1-JqUtsb-SwpnH3',
    #     values={
    #         # 'col-0': 'Google',                  # text
    #         'col-1': 'Tesla',                      # number
    #         # 'col-2': False,                     # boolean
    #         # 'col-3': 'https://google.com',      # url
    #         # 'col-4': datetime.datetime.today()  # date
    #         # 'col-5'     # date_added
    #     },
    #     edges=[]
    # )
    # print (result)
    # result = q.get_graph(
    #     project_id='ctx-MCxXEVZjyndWiHH7VPY',
    #     table_id='tab-MCxXOmTENzVaAZUdDGR',
    #     filters=[],
    #     offset=1,
    #     limit=50
    # )
    # print (result)

    # result = q.create_vertex(
    #     project_id='ctx-M57S8onUVXwdNMRgHPf',
    #     table_id='tab-M57wxxBqH0D7aKgYhhH',
    #     values={
    #         'col-0': 'Apple7',
    #         'col-1': True,
    #         'col-2': ''
    #     },
    #     edges=[
    #         ("column3", "row-M587jZETRpuCBIXUfw6"),
    #         ("column3", "row-M58Ac6n8CjPhqp8-u7M")
    #     ]
    # )
    # print (result)

    # result = q.update_vertex(
    #     project_id='ctx-MCxXEVZjyndWiHH7VPY',
    #     table_id='tab-MCxXOmTENzVaAZUdDGR',
    #     vertex_id='row-MCxYO25MsG10qTdrSPQ',
    #     values={
    #         'col-0': 'SW',
    #     },
    #     edges=[
    #     ]
    # )
    # print (result)

    # result = q.get_graph(
    #     project_id='ctx-MCxWvNH-NPIaFmE6OQH',
    #     table_id='tab-M5Nm23_krbcQHdBqWh-',
    #     filters=[],
    #     offset=1,
    #     limit=50
    # )
    # print (result)
    '''
    {
        "data": {
            "createVertex": {
                "ok": true,
                "vertex": {
                    "id": "row-M53tT_jTviJ50qyzgsL",
                    "label": "tab-M53pRIARajeAYTwPIAN",
                    "values": [
                        {
                            "key": "col-1",
                            "value": "test"
                        },
                        {
                            "key": "col-3",
                            "value": "1.0"
                        }
                    ],
                    "contextId": null
                }
            }
        }
    }
    '''

    # result = q.update_vertex(
    #     project_id='ctx-MCxWvNH-NPIaFmE6OQH',
    #     table_id='tab-M5Nm23_krbcQHdBqWh-',
    #     vertex_id='row-M5NnwDXIN6tZVOWOCuR',
    #     values={
    #         'col-0': 'Samsung',
    #     },
    #     edges=[]
    # )
    # print (result)
    '''
    {
        "data": {
            "updateVertex": {
                "ok": true
            }
        }
    }
    '''

    # result = q.delete_vertex(
    #     project_id='ctx-MCxXEVZjyndWiHH7VPY',
    #     table_id='tab-MCxXOmTENzVaAZUdDGR',
    #     vertex_id='row-MCxYO25MsG10qTdrSPQ',
    # )
    # print (result)
    '''
    {
        "data": {
            "deleteVertex": {
                "ok": true
            }
        }
    }
    '''

    # result = q.bulk_delete_vertices(
    #     project_id='ctx-MCxXEVZjyndWiHH7VPY',
    #     table_id='tab-MCxXOmTENzVaAZUdDGR',
    #     vertex_ids=[
    #         "row-MCxYexMyxDjAJ6oTmlh",
    #         "row-MCxYhXtaOKSnyADwYXa"
    #     ]
    # )
    # print (result)
    '''
    {
        "data": {
            "bulkDeleteVertices": {
                "ok": true
            }
        }
    }
    '''


    # result = q.get_schema(
    #     project_id='ctx-M5Na8A_zgK3m455pp-r'
    # )
    # print (result)
    '''
    {
        "data": {
            "getSchema": {
                "tables": [
                    {
                        "tableId": "tab-M53lgnpTXtQhMqMBXHH",
                        "displayName": "Table 1",
                        "columns": [],
                        "config": null
                    }
                ],
                "links": []
            }
        }
    }
    '''

    # result = q.get_graph(
    #     project_id='ctx-MCxWvNH-NPIaFmE6OQH',
    #     table_id='tab-M5Nm23_krbcQHdBqWh-',
    #     offset=1,
    #     limit=50
    # )
    # print (result)

    # result = q.get_graph(
    #     project_id='ctx-M5Na8A_zgK3m455pp-r',
    #     table_id='tab-M5Nb1-JqUtsb-SwpnH3',
    #     filters=[],
    #     offset=1,
    #     limit=50
    # )
    # print (result)
    '''
    {
        "data": {
            "getGraph": {
                "vertices": [
                    {
                        "id": "row-M54-YHKSk3i_9rXO7cl",
                        "label": "tab-M53zumOvT3xKmqkIB_X",
                        "values": [
                            {
                                "key": "col-0",
                                "value": "ipod"
                            },
                            {
                                "key": "col-1",
                                "value": "10.0"
                            },
                            {
                                "key": "col-2",
                                "value": "apple"
                            }
                        ],
                        "contextId": null
                    },
                    {
                        "id": "row-M54-akM_ctW_QMTAmd5",
                        "label": "tab-M53zumOvT3xKmqkIB_X",
                        "values": [
                            {
                                "key": "col-0",
                                "value": "galaxy s"
                            },
                            {
                                "key": "col-1",
                                "value": "20.0"
                            },
                            {
                                "key": "col-2",
                                "value": "samsung"
                            }
                        ],
                        "contextId": null
                    },
                    {
                        "id": "row-M54-e4d-BIwZywV9Qoq",
                        "label": "tab-M53zumOvT3xKmqkIB_X",
                        "values": [
                            {
                                "key": "col-0",
                                "value": "galaxy tab"
                            },
                            {
                                "key": "col-1",
                                "value": "20.0"
                            },
                            {
                                "key": "col-2",
                                "value": "samusng"
                            }
                        ],
                        "contextId": null
                    },
                    {
                        "id": "row-M54-fbtdB4FLEO_R2xy",
                        "label": "tab-M53zumOvT3xKmqkIB_X",
                        "values": [
                            {
                                "key": "col-0",
                                "value": "mac"
                            },
                            {
                                "key": "col-1",
                                "value": "20.0"
                            },
                            {
                                "key": "col-2",
                                "value": "apple"
                            }
                        ],
                        "contextId": null
                    }
                ],
                "edges": [],
                "total": 5
            }
        }
    }
    '''

    # result = q.get_graph(
    #     project_id='ctx-MCxWvNH-NPIaFmE6OQH',
    #     table_id='tab-M5Nm23_krbcQHdBqWh-',
    #     filters=[
    #         {
    #             "property": "col-0",
    #             "predicate": "=",
    #             "value": "Samsung"
    #         }
    #     ],
    #     offset=1,
    #     limit=50
    # )
    # print (result)

    # # Summarize Graph
    # # count, sum, mean, max, min
    # result = q.summarize_graph(
    #     project_id='ctx-MCxWvNH-NPIaFmE6OQH',
    #     table_id='tab-M5Nm23_krbcQHdBqWh-',
    #     filters=[
    #         {
    #             "property": "col-0",
    #             "predicate": "=",
    #             "value": "Samsung"
    #         }
    #     ],
    #     groups=[{"property": "col-0"}],
    #     aggregations=[{"property": "col-0", "function": "count"}],
    #     offset=1,
    #     limit=50
    # )
    # print (result)
    '''
    {
        "data": {
            "getGraph": {
                "vertices": [],
                "edges": [],
                "total": 0
            }
        }
    }
    '''

    # result = q.bulk_upload(
    #     project_id='ctx-M5Na8A_zgK3m455pp-r',
    #     filepaths=[
    #         '/Users/sangwonseo/Downloads/company1.csv',
    #         '/Users/sangwonseo/Downloads/company2.csv',
    #     ]
    # )
    # print (result)
    '''
    {
        "data": {
            "getBulkBundle": {
                "bundleId": "1976ac21-45b6-4e02-8f6c-36456cf70b1d",
                "status": "finished"
            }
        }
    }
    '''
