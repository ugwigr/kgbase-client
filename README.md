## Instantiate object
```
import client
c = client.Client('ab')
```

## List Project
```
result = c.project_list()
print result
```
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
## Create Project
```
result = c.project_create(**{
    'name': 'client-test1111111',
    'description': 'client-test1111111',
    'is_public': True
})
print result
```
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

## List Table
```
result = c.table_list('client-test1111111-LWS2AsRVWYkIaEr9Isq')
print result
```
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

## Create Table
```
result = c.table_create(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    **{
        'name': 'test3',
        'description': 'test3',
    }
)
print result
```
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

## Create Column
```
result = c.column_create(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    table_id='test3-LWSJDcerl3f3ZSXECsC',
    **{'type': u'text', 'is_unique': False, 'display_name': u'Sangwon Column1', 'id': u'sangwon-column1'}
)
print result
```
```
{
    "message": "Column created",
    "changeset_id": 71
}
```

## Create Column with  Changeset ID
```
result = c.column_create(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    table_id='test3-LWSJDcerl3f3ZSXECsC',
    **{'type': u'text', 'is_unique': False, 'display_name': u'Sangwon Column2', 'id': u'sangwon-column2', 'changeset_id': 72}
)
print result
```
```
{
    "message": "Column created",
    "changeset_id": 71
}
```

## Create Data
```
result = c.data_create(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    table_id='test3-LWSJDcerl3f3ZSXECsC',
    **{'sangwon-column1': '1', 'sangwon-column2': '2'}
)
print result
```
```
{
    "message": "Data created",
    "changeset_id": 74
}
```

## Create Data with Changeset ID
```
result = c.data_create(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    table_id='test3-LWSJDcerl3f3ZSXECsC',
    **{'sangwon-column1': '1', 'sangwon-column2': '2', 'changeset_id': 74}
)
print result
```
```
{
    "message": "Data created",
    "changeset_id": 74
}
```

## Submit Changeset
```
result = c.changeset_submit(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    table_id='test1-LWS2_M7GCM-Q2Xx7-kt',
    changeset_id=74,
    **{'summary': 'api test'}
)
print result
```
```
{
    "message": "Changeset submitted",
    "changeset_id": "74"
}
```
## Publish Changeset
```
result = c.changeset_publish(
    project_id='client-test1111111-LWS2AsRVWYkIaEr9Isq',
    table_id='test1-LWS2_M7GCM-Q2Xx7-kt',
    changeset_id=74,
)
print result
```
```
{
    "message": "Changeset published",
    "changeset_id": "74"
}
```