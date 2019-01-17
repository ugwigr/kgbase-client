import client


c = client.Client('ab')

# List Project
# result = c.project_list()
# print result

# Create Project
# result = c.project_create(**{
#     'name': 'client-test1111111',
#     'description': 'client-test1111111',
#     'is_public': True
# })
# print result
# {u'project': {u'id': 15, u'is_public': True, u'slug': u'client-test1111111-LWS2AsRVWYkIaEr9Isq', u'name': u'client-test1111111', u'description': u'client-test1111111'}, u'message': u'New project created'}

# List Table
result = c.table_list('client-test1111111-LWS2AsRVWYkIaEr9Isq')
print result

# Create Table
# result = c.table_create(
#     project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
#     **{
#         'name': 'test3',
#         'description': 'test3',
#     }
# )
# print result

# Create Column
# result = c.column_create(
#     project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
#     table_id='test3-LWSJDcerl3f3ZSXECsC',
#     **{'type': u'text', 'is_unique': False, 'display_name': u'Sangwon Column1', 'id': u'sangwon-column1'}
# )
# print result

# result = c.column_create(
#     project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
#     table_id='test3-LWSJDcerl3f3ZSXECsC',
#     **{'type': u'text', 'is_unique': False, 'display_name': u'Sangwon Column2', 'id': u'sangwon-column2', 'changeset_id': 72}
# )
# print result


# result = c.data_create(
#     project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
#     table_id='test3-LWSJDcerl3f3ZSXECsC',
#     **{'sangwon-column1': '1', 'sangwon-column2': '2'}
# )
# print result

# result = c.data_create(
#     project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
#     table_id='test3-LWSJDcerl3f3ZSXECsC',
#     **{'sangwon-column1': '1', 'sangwon-column2': '2', 'changeset_id': 74}
# )
# print result


# result = c.changeset_submit(
#     project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
#     table_id='test1-LWS2_M7GCM-Q2Xx7-kt',
#     changeset_id=74,
#     **{'summary': 'api test'}
# )
# print result


# result = c.changeset_publish(
#     project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
#     table_id='test1-LWS2_M7GCM-Q2Xx7-kt',
#     changeset_id=74,
# )
# print result