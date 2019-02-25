import client

c = client.Client("ab", base="http://127.0.0.1:8000/api")

# 1. Project
# List Project
result = c.project_list()
print (result)

# Create Project
result = c.project_create(
    name='client-39',
    description='client-39',
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

# 4. Record
# 4.1. Record Create
result = c.changeset_create(project_id=project_id, summary='summary')
changeset_id = result['id']
result = c.record_create(
    table_id=table_id,
    record={'Column1': '1', 'Column2': '2'},
    changeset_id=changeset_id
)
print(result)
row1 = result['id']
result = c.record_create(
    table_id=table_id,
    record={'Column1': '3', 'Column2': '4'},
    changeset_id=changeset_id
)
print(result)
row2 = result['id']
result = c.record_create(
    table_id=table_id,
    record={'Column1': '5', 'Column2': '6'},
    changeset_id=changeset_id
)
print(result)
row3 = result['id']

# Submit changeset
result = c.changeset_submit(changeset_id=changeset_id, summary='API Test')
# Publish changeset
result = c.changeset_publish(changeset_id=changeset_id)

# 4.2. Record List (without Changeset ID)
result = c.record_list(
    table_id=table_id,
)
print(result)

result = c.record_list(
    table_id=table_id,
    filters={'Column1': ['1', '3'], 'Column2': ['2']}
)
print(result)
result = c.record_list(
    table_id=table_id,
    filters={'Column1': '1', 'Column2': ['2']}
)
print(result)

result = c.record_list(
    table_id=table_id,
    filters={'Column5': '1'}
)
print(result)

# 4.2. Record List (Create Changeset ID)
result = c.changeset_create(project_id=project_id, summary='summary')
changeset_id = result['id']
result = c.record_list(
    changeset_id=changeset_id,
    table_id=table_id,
)
print(result)

# 4.3. Record Update
result = c.changeset_create(project_id=project_id, summary='summary')
changeset_id = result['id']
result = c.record_update(
    changeset_id=changeset_id,
    table_id=table_id,
    row_id=row2,
    record={'Column1': '7', 'Column2': '8'},
)
print(result)
# Submit changeset
result = c.changeset_submit(changeset_id=changeset_id, summary='API Test')
# Publish changeset
result = c.changeset_publish(changeset_id=changeset_id)

# 4.5. Record Destroy
result = c.changeset_create(project_id=project_id, summary='summary')
changeset_id = result['id']
result = c.record_destroy(
    changeset_id=changeset_id,
    table_id=table_id,
)
print(result)
# Submit changeset
result = c.changeset_submit(changeset_id=changeset_id, summary='API Test')
# Publish changeset
result = c.changeset_publish(changeset_id=changeset_id)
