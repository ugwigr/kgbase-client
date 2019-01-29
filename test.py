import client


c = client.Client('ab')

# List Project
result = c.project_list()

# Create Project
result = c.project_create(
    name='client-9',
    description='client-9',
    is_public=True,
)

# List Table
result = c.table_list(
    project_id='client-1-LXKLEQaTfqx-PQhONGE'
)

# Create Table
result = c.table_create(
    project_id='client-1-LXKLEQaTfqx-PQhONGE',
    name='test3',
    description='test3',
)

# Create Column
result = c.column_create(
    table_id='test3-LXKLJd3BMnja_WbNeID',
    name='Column1',
    column_type='text',
    is_unique=False,
    changeset_id=79,
)

# Create data
result = c.data_create(
    table_id='test3-LXKLJd3BMnja_WbNeID',
    data={'Column1': '1', 'Column2': '2'},
    changeset_id=87
)

# Submit changeset
result = c.changeset_submit(
    table_id='test3-LXKLJd3BMnja_WbNeID',
    changeset_id=87,
    summary='API Test'
)

# Publish changeset
result = c.changeset_publish(
    table_id='test3-LXKLJd3BMnja_WbNeID',
    changeset_id=87,
)