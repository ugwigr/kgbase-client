from kgbase import Query

if __name__ == "__main__":
    q = Query()
    result = q.login(
        username='sangwon.seo@thinknum.com',
        password='worldcup'
    )
    # print (result)

    # result = q.get_user_state()
    # print (result)

    # result = q.get_public_projects()
    # print (result)

    # result = q.get_team_projects()
    # print (result)

    # result = q.get_favorite_projects()
    # print (result)

    # result = q.get_user_projects()
    # print (result)

    # print (q.create_project(name='test-api', is_public=True, color="gray"))

    # print (q.get_project_state(project_id='ctx-M4uWmlqujEeosYeci6C'))

    # print (q.update_project(project_id='ctx-M4uWmlqujEeosYeci6C', name='test-api-v2', is_public=False, color="gray"))

    # print (q.destroy_project(project_id='ctx-M4uWmlqujEeosYeci6C'))

    # print (q.get_schema(project_id='ctx-M4uaGyFSWy_VCFpwaBZ'))

    # print (q.get_graph(
    #     project_id='ctx-M4uaGyFSWy_VCFpwaBZ', 
    #     table_id='tab-M4ucjw_tyHUk-S6qayt',
    #     offset=1,
    #     limit=50
    # ))

    # print (q.get_task(task_id="1867"))

    # print (q.create_table(
    #     project_id='ctx-M4uaGyFSWy_VCFpwaBZ',
    #     display_name='api-test',
    #     description='Api test'
    # ))

    # print (q.update_table(
    #     project_id='ctx-M4uaGyFSWy_VCFpwaBZ',
    #     table_id='tab-M4z1HBWWbnAdC9AU6I-',
    #     display_name='api-table2',
    #     description='asdfsdfs',
    #     graph_shape='circle'
    # ))

    # print (q.delete_table(
    #     project_id='ctx-M4uaGyFSWy_VCFpwaBZ',
    #     table_id='tab-M4z1HBWWbnAdC9AU6I-'
    # ))
    # print (q.get_task(task_id="1867"))

    # print (q.create_column(
    #     project_id='ctx-M4uaGyFSWy_VCFpwaBZ',
    #     table_id='tab-M4z1HBWWbnAdC9AU6I-',
    #     display_name='api-column2',
    #     data_type='text'
    # ))

    # print (q.update_column(
    #     project_id='ctx-M4uaGyFSWy_VCFpwaBZ',
    #     table_id='tab-M4z1HBWWbnAdC9AU6I-',
    #     column_id='col-10',
    #     display_name='api-column10',
    #     data_type='number'
    # ))

    # print (q.delete_column(
    #     project_id='ctx-M4uaGyFSWy_VCFpwaBZ',
    #     table_id='tab-M4z1HBWWbnAdC9AU6I-',
    #     column_id='col-9',
    # ))

    print (q.create_vertex(
        project_id='ctx-M4uaGyFSWy_VCFpwaBZ',
        table_id='tab-M4z1HBWWbnAdC9AU6I-',
        column_ids=['col-1', 'col-10'],
        values=['a', '2']
    ))

    # print (q.update_vertex(
    #     project_id='ctx-M4uaGyFSWy_VCFpwaBZ',
    #     table_id='tab-M4z1HBWWbnAdC9AU6I-',
    #     vertex_id='row-M4zL8YmuPO_yiqBQebZ',
    #     column_ids=['col-1', 'col-10'],
    #     values=['api', '123123'] 
    # ))

    # print (q.delete_vertex(
    #     project_id='ctx-M4uaGyFSWy_VCFpwaBZ',
    #     table_id='tab-M4z1HBWWbnAdC9AU6I-',
    #     vertex_id='row-M4zL8YmuPO_yiqBQebZ',
    # ))

    # print (q.bulk_delete_vertices(
    #     project_id='ctx-M4uaGyFSWy_VCFpwaBZ',
    #     table_id='tab-M4z1HBWWbnAdC9AU6I-',
    #     vertex_ids=[
    #         "row-M4zKyJT1b-hf0g_UDEa",
    #         "row-M4zL3aqEQRR-cnxxttf",
    #         "row-M4zLGvIzooKOBwVCtjj",
    #         "row-M4zO9Ydz0V2R11xRTys",
    #     ]
    # ))
    # result = q.logout()
    # print (result)

    print (q.get_graph(
        project_id='ctx-M4uaGyFSWy_VCFpwaBZ', 
        table_id='tab-M4z1HBWWbnAdC9AU6I-',
        offset=1,
        limit=50
    ))
