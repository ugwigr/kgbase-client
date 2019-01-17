import client


c = client.Client('ab')

# print c.project_list()

# print c.project_create(**{
#     'name': 'client-test-name23',
#     'description': 'client-test-description1',
#     'is_public': 1
# })


# print c.table_list('client-test-name22-LWMyg-z7rY87CEye0vl')

# print c.table_create(
#     project_id='client-test-name22-LWMyg-z7rY87CEye0vl',
#     **{
#         'name': 'test1',
#         'description': 'test1',
#     }
# )

print c.column_create(
    project_id='sangwon-LWOM0kLMCNCMUJPK6Eh',
    table_id='sangwon-table-LWOM3p6GInEy1dK1ZFS',
    **{'type': u'text', 'is_unique': False, 'display_name': u'Sangwon Column35', 'id': u'sangwon-column35'}
)
