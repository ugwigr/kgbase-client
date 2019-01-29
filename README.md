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
c.project_list()
```

##### Example response
```
{
    "user_projects": [
        {
            "id": 14,
            "is_public": False,
            "slug": "sangwon-LWOM0kLMCNCMUJPK6Eh",
            "name": "sangwon",
            "description": "sangwon"
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
c.project_create(**{
    'name': 'client-test1111111',
    'description': 'client-test1111111',
    'is_public': True
})
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
c.table_list('client-test1111111-LWS2AsRVWYkIaEr9Isq')
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
c.table_create(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    **{
        'name': 'test3',
        'description': 'test3',
    }
)
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
c.column_create(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    table_id='test3-LWSJDcerl3f3ZSXECsC',
    **{'type': u'text', 'is_unique': False, 'name': u'Column1'}
)
```

##### Example response
```
{
    "message": "Column created",
    "changeset_id": 71
}
```

### Create Column with Changeset ID
If you know changeset id, then you can create a column multiple times under same changeset id. And then you can submit changeset for all created columns at once.

##### Example code
```
c.column_create(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    table_id='test3-LWSJDcerl3f3ZSXECsC',
    **{'type': u'text', 'is_unique': False, 'name': u'Column2', 'changeset_id': 72}
)
```

##### Example response
```
{
    "message": "Column created",
    "changeset_id": 71
}
```

***
# Data
### Create
When adding data, project `slug` and table `slug` are necessary.

##### Example code
```
c.data_create(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    table_id='test3-LWSJDcerl3f3ZSXECsC',
    **{'Column1': '1', 'Column2': '2'}
)
```

##### Example response
```
{
    "message": "Data created",
    "changeset_id": 74
}
```

### Create Data with Changeset ID
If you know changeset id, then you can add data multiple times under same changeset id. And then you can submit changeset for all added data at once.

##### Example code
```
c.data_create(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    table_id='test3-LWSJDcerl3f3ZSXECsC',
    **{'Column1': '1', 'Column2': '2', 'changeset_id': 74}
)
```
##### Example response
```
{
    "message": "Data created",
    "changeset_id": 74
}
```

***
# Changeset
### Submit Changeset
You can submit changeset under the combination of project and table.

##### Example code
```
c.changeset_submit(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    table_id='test1-LWS2_M7GCM-Q2Xx7-kt',
    changeset_id=74,
    **{'summary': 'api test'}
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
c.changeset_publish(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    table_id='test1-LWS2_M7GCM-Q2Xx7-kt',
    changeset_id=74,
)
```
##### Example response
```
{
    "message": "Changeset published",
    "changeset_id": "74"
}
```
