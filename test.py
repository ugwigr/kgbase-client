import client


c = client.Client('ab')

# List Project
result = c.project_list()
print (result)

# Create Project
result = c.project_create(
    name='client-10',
    description='client-10',
    is_public=True,
)
print (result)

# List Table
result = c.table_list(
    project_id='client-10-LXQ35FoviVrTVAJ-lBD'
)
print (result)

# Create Table
result = c.table_create(
    project_id='client-10-LXQ35FoviVrTVAJ-lBD',
    name='test3',
    description='test3',
)
print (result)

# Create changeset
result = c.changeset_create(
    table_id='test3-LXQ3HYMDRjzTYMjY5Js',
)
changeset_id = result['changeset']['id']
print(changeset_id)

# Create Column
result = c.column_create(
    table_id='test3-LXQ3HYMDRjzTYMjY5Js',
    name='Column1',
    column_type='text',
    is_unique=False,
    changeset_id=changeset_id,
)
print (result)

result = c.column_create(
    table_id='test3-LXQ3HYMDRjzTYMjY5Js',
    name='Column2',
    column_type='text',
    is_unique=False,
    changeset_id=changeset_id,
)
print (result)

# Create data
result = c.data_create(
    table_id='test3-LXQ3HYMDRjzTYMjY5Js',
    data={'Column1': '1', 'Column2': '2'},
    changeset_id=90
)
print (result)

result = c.data_create(
    table_id='test3-LXQ3HYMDRjzTYMjY5Js',
    data={'Column1': '3', 'Column2': '4'},
    changeset_id=90
)
print (result)

result = c.data_create(
    table_id='test3-LXQ3HYMDRjzTYMjY5Js',
    data={'Column1': '5', 'Column2': '6'},
    changeset_id=90
)
print (result)

# Submit changeset
result = c.changeset_submit(
    table_id='test3-LXQ3HYMDRjzTYMjY5Js',
    changeset_id=90,
    summary='API Test'
)
print (result)

# Publish changeset
result = c.changeset_publish(
    table_id='test3-LXQ3HYMDRjzTYMjY5Js',
    changeset_id=90,
)
print (result)