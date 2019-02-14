# KGbase library reference

To instantiate KGbase client, you will first need an API key. To get an API key for your project, open your project, click on "Collaborators" button in the upper right corner, and add an API user. Save the API key generated for this user.

##### Example code

```
import client
c = client.Client('API_KEY')
```

*** 
# Project
### List
Project list that user created and public project will be retrieved.
##### Example code
```
result = c.project_list()
```

##### Example response
```
{
    "user_projects": [
        {
            "id": 14,
            "is_public": False,
            "slug": "client-LWOM0kLMCNCMUJPK6Eh",
            "name": "client",
            "description": "client"
        },
    ],
    "public_projects": [
        {
            "id": 3,
            "is_public": True,
            "slug": "test2-LU7kokaeJ10BZKmtuvJ",
            "name": "test2",
            "description": "test2"
        },
        {
            "id": 4,
            "is_public": True,
            "slug": "test3-LU7l8JCT3SlKnQYLiu4",
            "name": "test3",
            "description": "test3"
        },
    ]
}
```

### Create
User can create public or private project.
##### Example code
```
result = c.project_create(
    name='client-9',
    description='client-9',
    is_public=True,
)
project_id = result['project']['slug']
```

##### Example response
```
{
    "project": {
        "id": 15,
        "is_public": True,
        "slug": "client-test1111111-LWS2AsRVWYkIaEr9Isq",
        "name": "client-test1111111",
        "description": "client-test1111111"
    },
    "message": "New project created"
}
```

***
# Table
### List
Table list of one particular project will be retrieved. Project `slug` should be passed.
##### Example code
```
result = c.table_list(
    project_id='client-1-LXKLEQaTfqx-PQhONGE'
)
```
##### Example response
```
{
    "tables": [
        {
            "repository_name": "test3-LWSJDcerl3f3ZSXECsC",
            "slug": "test3-LWSJDcerl3f3ZSXECsC",
            "description": "test3",
            "name": "test3"
        },
        {
            "repository_name": "test2-LWSInRQSfJkLcySckjN",
            "slug": "test2-LWSInRQSfJkLcySckjN",
            "description": "test2",
            "name": "test2"
        },
        {
            "repository_name": "test1-LWS2_M7GCM-Q2Xx7-kt",
            "slug": "test1-LWS2_M7GCM-Q2Xx7-kt",
            "description": "test1",
            "name": "test1"
        }
    ]
}
```

### Create
When creating table, project `slug` should be passed.
##### Example code
```
result = c.table_create(
    project_id='client-1-LXKLEQaTfqx-PQhONGE',
    name='test3',
    description='test3',
)
table_id = result['table']['slug']
```
##### Example response
```
{
    "project": {
        "repository_name": "test1-LWS2_M7GCM-Q2Xx7-kt",
        "slug": "test1-LWS2_M7GCM-Q2Xx7-kt",
        "description": "test1",
        "name": "test1"
    },
    "message": "New table created"
}
```

***
# Column
### Create
When creating column for table, project `slug` and table `slug` are necessary.
`type` should be one of `text`, `int`, `float`
##### Example code
```
result = c.changeset_create(
    project_id=project_id,
    summary='summary'
)
changeset_id = result['id']

result = c.column_create(
    table_id=table_id,
    name='Column1',
    column_type='text',
    is_unique=False,
    changeset_id=changeset_id,
)

result = c.column_create(
    table_id=table_id,
    name='Column2',
    column_type='text',
    is_unique=False,
    changeset_id=changeset_id,
)
```

##### Example response
```
{
    "message": "Column created",
    "changeset_id": 71
}
{
    "message": "Column created",
    "changeset_id": 72
}
```

***
# Record

### Create
When adding record, project `slug` and table `slug` are necessary.

##### Example code
```
result = c.changeset_create(
    project_id=project_id,
    summary='summary'
)
changeset_id = result['id']

result = c.record_create(
    table_id=table_id,
    record={'Column1': '1', 'Column2': '2'},
    changeset_id=changeset_id
)
print (result)

result = c.record_create(
    table_id=table_id,
    record={'Column1': '3', 'Column2': '4'},
    changeset_id=changeset_id
)
print (result)

result = c.record_create(
    table_id=table_id,
    record={'Column1': '5', 'Column2': '6'},
    changeset_id=changeset_id
)
print (result)

# Submit changeset
result = c.changeset_submit(
    changeset_id=changeset_id,
    summary='API Test'
)
print (result)

# Publish changeset
result = c.changeset_publish(
    changeset_id=changeset_id,
)
print (result)
```

##### Example response
```
{
    'id': 109, 
    'branch_name': 'raphaelseo@gmail.com-LXXjKzYnFXEw4TIafXV', 
    'summary': 'summary'
}
{'Column1': '1', 'Column2': '2', 'id': 'row-LXXjKhgZnysClIhLnsf'}
{'Column1': '3', 'Column2': '4', 'id': 'row-LXXjKkHqzLv6r6zw_N0'}
{'Column1': '5', 'Column2': '6', 'id': 'row-LXXjKms5_YEzKMYBkcY'}
```

### List
##### Example code
```
result = c.record_list(
    table_id=table_id,
)
print(result)

result = c.record_list(
    table_id=table_id,
    filter={'Column1': ['1', '3'], 'Column2': '2'}
)
print(result)

result = c.record_list(
    table_id=table_id,
    filter={'Column1': '1', 'Column2': '2'}
)
print(result)

result = c.record_list(
    changeset_id=changeset_id,
    table_id=table_id,
)
print(result)
```

##### Example response
```
[
    {'Column1': '1', 'Column2': '2', 'id': 'row-LXXjKhgZnysClIhLnsf'},
    {'Column1': '3', 'Column2': '4', 'id': 'row-LXXjKkHqzLv6r6zw_N0'},
    {'Column1': '5', 'Column2': '6', 'id': 'row-LXXjKms5_YEzKMYBkcY'}
]

[
    {'Column1': '1', 'Column2': '2', 'id': 'row-LYhGvbh4JtiW2fSZE4i'}, 
    {'Column1': '3', 'Column2': '4', 'id': 'row-LYhGveBDiBtyjd5hMcC'}
]

[
    {'Column1': '1', 'Column2': '2', 'id': 'row-LYhGvbh4JtiW2fSZE4i'}, 
]

[
    {'Column1': '1', 'Column2': '2', 'id': 'row-LXXjKhgZnysClIhLnsf'},
    {'Column1': '3', 'Column2': '4', 'id': 'row-LXXjKkHqzLv6r6zw_N0'},
    {'Column1': '5', 'Column2': '6', 'id': 'row-LXXjKms5_YEzKMYBkcY'}
]
```

### Update
##### Example code
```
# Create changeset
result = c.changeset_create(
    project_id=project_id,
    summary='summary'
)
changeset_id = result['id']

result = c.record_update(
    changeset_id=changeset_id,
    table_id=table_id,
    row_id=row2,
    record={'Column1': '7', 'Column2': '8'},
)
print(result)

# Submit changeset
result = c.changeset_submit(
    changeset_id=changeset_id,
    summary='API Test'
)
print (result)

# Publish changeset
result = c.changeset_publish(
    changeset_id=changeset_id,
)
print (result)
```

##### Example response
```
{'Column1': '7', 'Column2': '8', 'id': 'row-LXXoLJM-J0J2SCN-sma'}
```

### Delete
##### Example code
```
# Create changeset
result = c.changeset_create(
    project_id=project_id,
    summary='summary'
)
changeset_id = result['id']

result = c.record_destroy(
    changeset_id=changeset_id,
    table_id=table_id,
)

# Submit changeset
result = c.changeset_submit(
    changeset_id=changeset_id,
    summary='API Test'
)
print (result)

# Publish changeset
result = c.changeset_publish(
    changeset_id=changeset_id,
)
print (result)
```

##### Example response
```
{}
```

***
# Changeset
### Submit Changeset
You can submit changeset under the combination of project and table.

##### Example code
```
result = c.changeset_submit(
    table_id='test3-LXKLJd3BMnja_WbNeID',
    changeset_id=87,
    summary='API Test'
)
```
##### Example response
```
{
    "message": "Changeset submitted",
    "changeset_id": "74"
}
```

### Publish
You can submit changeset under the combination of project and table.
##### Example code
```
result = c.changeset_publish(
    table_id='test3-LXKLJd3BMnja_WbNeID',
    changeset_id=87,
)
```
##### Example response
```
{
    "message": "Changeset published",
    "changeset_id": "74"
}
```
