import client

c = client.Client("API_KEY", base="http://127.0.0.1:8000/api")

# 1. Project
# List Project
result = c.project_list()
print (result)

# Create Project
result = c.project_create(
    name='client-26',
    description='client-26',
    is_public=True,
)
print(result)
project_id = result['project']['slug']

# 2. Table
# List Table
result = c.table_list(
    project_id=project_id
)
print (result)

# Create Table
result = c.table_create(
    project_id=project_id,
    name='test1',
    description='test1',
)
print(result)
table_id = result['table']['slug']

# 3. Column
# Create changeset
result = c.changeset_create(project_id=project_id, summary='summary')
changeset_id = result['id']

# Create Column
result = c.column_create(
    table_id=table_id,
    name='Column1',
    column_type='text',
    is_unique=False,
    changeset_id=changeset_id,
)
print (result)
result = c.column_create(
    table_id=table_id,
    name='Column2',
    column_type='text',
    is_unique=False,
    changeset_id=changeset_id,
)
print (result)
# Submit changeset
result = c.changeset_submit(changeset_id=changeset_id, summary='API Test')
# Publish changeset
result = c.changeset_publish(changeset_id=changeset_id)

# 4. Data
# 4.1. Data Create
result = c.changeset_create(project_id=project_id, summary='summary')
changeset_id = result['id']
result = c.data_create(
    table_id=table_id,
    data={'Column1': '1', 'Column2': '2'},
    changeset_id=changeset_id
)
print(result)
row1 = result['id']
result = c.data_create(
    table_id=table_id,
    data={'Column1': '3', 'Column2': '4'},
    changeset_id=changeset_id
)
print(result)
row2 = result['id']
result = c.data_create(
    table_id=table_id,
    data={'Column1': '5', 'Column2': '6'},
    changeset_id=changeset_id
)
print(result)
row3 = result['id']

# Submit changeset
result = c.changeset_submit(changeset_id=changeset_id, summary='API Test')
# Publish changeset
result = c.changeset_publish(changeset_id=changeset_id)

# 4.2. Data List
result = c.changeset_create(project_id=project_id, summary='summary')
changeset_id = result['id']
result = c.data_list(
    changeset_id=changeset_id,
    table_id=table_id,
)
print(result)

# 4.3. Data Update
result = c.changeset_create(project_id=project_id, summary='summary')
changeset_id = result['id']
result = c.data_update(
    changeset_id=changeset_id,
    table_id=table_id,
    row_id=row2,
    data={'Column1': '7', 'Column2': '8'},
)
print(result)
# Submit changeset
result = c.changeset_submit(changeset_id=changeset_id, summary='API Test')
# Publish changeset
result = c.changeset_publish(changeset_id=changeset_id)

# 4.5. Data Destroy
result = c.changeset_create(project_id=project_id, summary='summary')
changeset_id = result['id']
result = c.data_destroy(
    changeset_id=changeset_id,
    table_id=table_id,
)
print(result)
# Submit changeset
result = c.changeset_submit(changeset_id=changeset_id, summary='API Test')
# Publish changeset
result = c.changeset_publish(changeset_id=changeset_id)
