from kgbase import Query

# TODO
# filter, group by
# csv upload
# raw import

if __name__ == "__main__":
    q = Query()
    result = q.login(
        username='sangwon.seo@thinknum.com',
        password='worldcup'
    )
    # print (result)
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
    #     project_id='ctx-M53lgnjpCkc_plt0lqo'
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
    #     project_id='ctx-M53lgnjpCkc_plt0lqo', 
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
    #     project_id='ctx-M53mQIDEperhJx4e7J0'
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

    # result = q.get_schema(
    #     project_id='ctx-M53lgnjpCkc_plt0lqo'
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

    

    # result = q.get_task(task_id="1867")
    # print (result)

    # result = q.create_table(
    #     project_id='ctx-M53pLqASSUmxj5yU7LO',
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
    #     project_id='ctx-M53lgnjpCkc_plt0lqo',
    #     table_id='tab-M53nDu1y1SXMVA_ny97',
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
    #     project_id='ctx-M53lgnjpCkc_plt0lqo',
    #     table_id='tab-M53nDu1y1SXMVA_ny97'
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

    # resut = q.get_task(task_id="1931")
    # print (result)

    # result = q.create_column(
    #     project_id='ctx-M53pLqASSUmxj5yU7LO',
    #     table_id='tab-M53pRIARajeAYTwPIAN',
    #     display_name='api_column',
    #     data_type='number'
    # )
    # result = q.update_column(
    #     project_id='ctx-M53pLqASSUmxj5yU7LO',
    #     table_id='tab-M53pRIARajeAYTwPIAN',
    #     column_id='col-10',
    #     display_name='api-column10',
    #     data_type='link_one',
    #     linked_table='tab-dfj23eijSFdfewf'
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
    #     project_id='ctx-M53pLqASSUmxj5yU7LO',
    #     table_id='tab-M53pRIARajeAYTwPIAN',
    #     column_id='col-1',
    #     display_name='api-column10',
    #     data_type='number'
    # )
    # result = q.update_column(
    #     project_id='ctx-M53pLqASSUmxj5yU7LO',
    #     table_id='tab-M53pRIARajeAYTwPIAN',
    #     column_id='col-10',
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
    #     project_id='ctx-M53pLqASSUmxj5yU7LO',
    #     table_id='tab-M53pRIARajeAYTwPIAN',
    #     column_id='col-0',
    # )
    # print (result)
    '''
    {
        "data": {
            "deleteColumn": {
                "ok": true
            }
        }
    }
    '''

    # result = q.create_vertex(
    #     project_id='ctx-M53pLqASSUmxj5yU7LO',
    #     table_id='tab-M53pRIARajeAYTwPIAN',
    #     column_ids=['col-1', 'col-3'],
    #     values=['test', 1]
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
    #     project_id='ctx-M53pLqASSUmxj5yU7LO',
    #     table_id='tab-M53pRIARajeAYTwPIAN',
    #     vertex_id='row-M53tT_jTviJ50qyzgsL',
    #     column_ids=['col-1', 'col-3'],
    #     values=['test', 7] 
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
    #     project_id='ctx-M53pLqASSUmxj5yU7LO',
    #     table_id='tab-M53pRIARajeAYTwPIAN',
    #     vertex_id='row-M53tiVvmOZ451AuBIUJ',
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
    #     project_id='ctx-M53pLqASSUmxj5yU7LO',
    #     table_id='tab-M53pRIARajeAYTwPIAN',
    #     vertex_ids=[
    #         "row-M53tmNvBRE-qf7_6nUC",
    #         "row-M53tphXYno5UGZgQZlS",
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

    # result = q.get_graph(
        # project_id='ctx-M53pLqASSUmxj5yU7LO',
        # table_id='tab-M53pRIARajeAYTwPIAN',
    #     offset=1,
    #     limit=50
    # )
    # print (result)


    # result = q.get_graph(
    #     project_id='ctx-M53zulrvmCoNnP7PMEU',
    #     table_id='tab-M53zumOvT3xKmqkIB_X',
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
    #     project_id='ctx-M53zulrvmCoNnP7PMEU',
    #     table_id='tab-M53zumOvT3xKmqkIB_X',
    #     filters=[
    #         {
    #             "property": "col-2",
    #             "predicate": "=",
    #             "value": "apple"
    #         }
    #     ],
    #     offset=1,
    #     limit=50
    # )
    # print (result)

    # Summarize Graph
    # count, sum, mean, max, min
    result = q.summarize_graph(
        project_id='ctx-M53zulrvmCoNnP7PMEU',
        table_id='tab-M53zumOvT3xKmqkIB_X',
        filters=[
            # {
            #     "property": "col-2",
            #     "predicate": "=",
            #     "value": "apple"
            # }
        ],
        groups=[{"property": "col-2"}],
        aggregations=[{"property": "col-1", "function": "sum"}],
        offset=1,
        limit=50
    )
    print (result)
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
