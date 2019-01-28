import client


c = client.Client('ab')

# List Project
result = c.project_list()
print(result)

# Create Project
# result = c.project_create(**{
#     'name': 'client-1',
#     'description': 'client-1',
#     'is_public': True
# })
# print(result)

# List Table
# result = c.table_list('client-1-LXKLEQaTfqx-PQhONGE')
# print(result)

# Create Table
# result = c.table_create(
#     project_id='client-1-LXKLEQaTfqx-PQhONGE',
#     **{
#         'name': 'test3',
#         'description': 'test3',
#     }
# )
# print(result)

# Create Column without changeset id
# result = c.column_create(
#     project_id='client-1-LXKLEQaTfqx-PQhONGE',
#     table_id='test3-LXKLJd3BMnja_WbNeID',
#     **{'type': u'text', 'is_unique': False, 'name': u'Column1'}
# )
# print(result)

# Create Column with changeset id
# result = c.column_create(
#     project_id='client-1-LXKLEQaTfqx-PQhONGE',
#     table_id='test3-LXKLJd3BMnja_WbNeID',
#     **{'type': u'text', 'is_unique': False, 'name': u'Column2', 'changeset_id': 79}
# )
# print(result)

# Submit changeset
# result = c.changeset_submit(
#     project_id='client-1-LXKLEQaTfqx-PQhONGE',
#     table_id='test3-LXKLJd3BMnja_WbNeID',
#     changeset_id=79,
#     **{'summary': 'api test'}
# )
# print(result)

# Publish changeset
# result = c.changeset_publish(
#     project_id='client-1-LXKLEQaTfqx-PQhONGE',
#     table_id='test3-LXKLJd3BMnja_WbNeID',
#     changeset_id=79,
# )
# print(result)

# Create data without changeset id
# result = c.data_create(
#     project_id='client-1-LXKLEQaTfqx-PQhONGE',
#     table_id='test3-LXKLJd3BMnja_WbNeID',
#     **{'Sangwon Column1': '1', 'Sangwon Column2': '2', 'Sangwon Column3': '3'}
# )

# Create data with changeset id
# result = c.data_create(
#     project_id='client-1-LXKLEQaTfqx-PQhONGE',
#     table_id='test3-LXKLJd3BMnja_WbNeID',
#     **{'Sangwon Column1': '1', 'Sangwon Column2': '2', 'Sangwon Column3': '3', 'changeset_id': 87}
# )

# Submit changeset
# result = c.changeset_submit(
#     project_id='client-1-LXKLEQaTfqx-PQhONGE',
#     table_id='test3-LXKLJd3BMnja_WbNeID',
#     changeset_id=87,
#     **{'summary': 'api test'}
# )
# print(result)

# Publish changeset
# result = c.changeset_publish(
#     project_id='client-1-LXKLEQaTfqx-PQhONGE',
#     table_id='test3-LXKLJd3BMnja_WbNeID',
#     changeset_id=87,
# )
# print(result)