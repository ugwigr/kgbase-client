# Kgbase

## Installation
```
pip install kgbase
```

## Authentication

Import library.

```
from kgbase import Query
```

To authenticate, you must first signup from kgbase website. Your password must not be shared or exposed via publicly accessible resources (such as browser client-side scripting).

```python
q = Query()
q.login(
    username='Your username',
    password='Your password'
)
```

If you need to use a proxy, you can configure it with the proxies argument.

```python
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

q = Query(
    proxies=proxies
)
```

Requests can ignore verifying the SSL certficate if you set verify to False. By default, verify is set to True.

```python
q = Query(
    verify=False
)
```

To logout:
```python
q.logout()
```

## Projects

To get all public projects: 
```python
q.get_public_projects()
```

To get all team projects: 
```python
q.get_team_projects()
```

To get favorite projects: 
```python
q.get_favorite_projects()
```

To get my projects: 
```python
q.get_user_projects()
```

To create project:
```python
q.create_project(
    name='electronic devices', 
    is_public=True, 
)
```

You can see `projectId` from result.
```
{
    "data": {
        "createProject": {
            "ok": true,
            "project": {
                "uuid": "a0406c6d-122a-4ff2-af7f-976ba5cbca01",
                "graphqlId": "Project/1509",
                "projectId": "ctx-M53lgnjpCkc_plt0lqo",
                ...
            }
        }
    }
}
```

To see project state:
```python
q.get_project_state(
    project_id='ctx-M53lgnjpCkc_plt0lqo'
)
```

To update project:
```python
result = q.update_project(
    project_id='ctx-M53lgnjpCkc_plt0lqo', 
    name='electronic devices',
    is_public=False
)
```

To destroy project:
```python
q.destroy_project(
    project_id='ctx-M53lgnjpCkc_plt0lqo'
)
```

## Table

To create table:
```python
q.create_table(
    project_id='ctx-M53pLqASSUmxj5yU7LO',
    display_name='Product',
    description='Product Description'
)
```

The `tableId` is returned from the result.
```
{
    "data": {
        "createTable": {
            "ok": true,
            "tableId": "tab-M53nDu1y1SXMVA_ny97"
        }
    }
}
```

To update table:
```python
q.update_table(
    project_id='ctx-M53lgnjpCkc_plt0lqo',
    table_id='tab-M53nDu1y1SXMVA_ny97',
    display_name='Smartphones',
    description='Smartphones manufacurer and model name',
)
```

To delete table:
```python
q.delete_table(
    project_id='ctx-M53lgnjpCkc_plt0lqo',
    table_id='tab-M53nDu1y1SXMVA_ny97'
)
```

## Column
To create column:
```python
q.create_column(
    project_id='ctx-M53lgnjpCkc_plt0lqo',
    table_id='tab-M53nDu1y1SXMVA_ny97'
    display_name='company',
    data_type='text'
)
```

The `columnId` is returned from the result.
```python
{
    "data": {
        "createColumn": {
            "ok": true,
            "columnId": "col-1"
        }
    }
}
```

The `data_type` should be one of them. `text`, `number`, `boolean`, `url`, `date`, `date_added`, `link_one`, `link_many`.

To create column that data_type is `linke_one` or `link_many`:
```python
result = q.update_column(
    project_id='ctx-M53lgnjpCkc_plt0lqo',
    table_id='tab-M53nDu1y1SXMVA_ny97'
    column_id='col-1',
    display_name='company',
    data_type='link_one',
    linked_table='tab-dfj23eijSFdfewf'
)
```

To update column:
```python
q.update_column(
    project_id='ctx-M53pLqASSUmxj5yU7LO',
    table_id='tab-M53pRIARajeAYTwPIAN',
    column_id='col-1',
    display_name='company',
    data_type='text'
)
```

To delete column:
```python
q.delete_column(
    project_id='ctx-M53pLqASSUmxj5yU7LO',
    table_id='tab-M53pRIARajeAYTwPIAN',
    column_id='col-1',
)
```

## Vertex
To create vertex:
```
q.create_vertex(
    project_id='ctx-M53pLqASSUmxj5yU7LO',
    table_id='tab-M53pRIARajeAYTwPIAN',
    column_ids=['col-1', 'col-2'],
    values=['Google', 'Pixel 3A']
)
```

The `vertexId` is returned from the result.

```python
{
    "data": {
        "createVertex": {
            "ok": true,
            "vertex": {
                "id": "row-M53tT_jTviJ50qyzgsL",
                "label": "tab-M53pRIARajeAYTwPIAN",
                "values": [
                    {
                        "key": "col-1",
                        "value": "Google"
                    },
                    {
                        "key": "col-2",
                        "value": "Pixel 3A"
                    }
                ],
                "contextId": null
            }
        }
    }
}
```

Please note that `column_ids` and `values` should have same length of list in request. Value in list should match with data type of columns that you defined before.

To update vertex:
```python
q.update_vertex(
    project_id='ctx-M53pLqASSUmxj5yU7LO',
    table_id='tab-M53pRIARajeAYTwPIAN',
    vertex_id='row-M53tT_jTviJ50qyzgsL',
    column_ids=['col-1', 'col-2'],
    values=['Google', 'Pixel 3'] 
)
```

To delete vertex:
```python
q.delete_vertex(
    project_id='ctx-M53pLqASSUmxj5yU7LO',
    table_id='tab-M53pRIARajeAYTwPIAN',
    vertex_id='row-M53tT_jTviJ50qyzgsL',
)
```

## Schema

To see schema of project:
```python
q.get_schema(
    project_id='ctx-M53lgnjpCkc_plt0lqo'
)
```

You can see tables and columns belonging to the project.

```
{
    "data": {
        "getSchema": {
            "tables": [
                {
                    "tableId": "tab-M53lgnpTXtQhMqMBXHH",
                    "displayName": "Table 1",
                    "columns": [],
                    "config": null
                }
            ],
            "links": []
        }
    }
}
```

## Graph

To see vertex:
```python
q.get_graph(
    project_id='ctx-M53zulrvmCoNnP7PMEU',
    table_id='tab-M53zumOvT3xKmqkIB_X',
    filters=[],
    offset=1,
    limit=50
)
```

You can add filtering to vertex:

```python
q.get_graph(
    project_id='ctx-M53zulrvmCoNnP7PMEU',
    table_id='tab-M53zumOvT3xKmqkIB_X',
    filters=[
        {
            "property": "col-2",
            "predicate": "=",
            "value": "apple"
        }
    ],
    offset=1,
    limit=50
)
```

You can also add group by and aggregations:
```python
q.summarize_graph(
    project_id='ctx-M53zulrvmCoNnP7PMEU',
    table_id='tab-M53zumOvT3xKmqkIB_X',
    filters=[
        {
            "property": "col-2",
            "predicate": "=",
            "value": "apple"
        }
    ],
    groups=[
        {
            "property": "col-2"
        }
    ],
    aggregations=[
        {
            "property": "col-1",
            "function": "sum"
        }
    ],
    offset=1,
    limit=50
)
```

The `function` should be one of them. `count`, `sum`, `mean`, `max`, `min`.

## Bulk Upload

To upload csv file:
```python
q.bulk_upload(
    project_id='ctx-M57S8onUVXwdNMRgHPf',
    filepaths=[
        '/Users/sangwonseo/Downloads/company1.csv',
        '/Users/sangwonseo/Downloads/company2.csv',
    ]
)
```

Please note that csv files should follow Amazon neptune format. For more details, please refer to the documentation. https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html

## For more details about Kgbase
Please visit https://kgbase.com/pages/learn

## If you are interested in Kgbase demo
Please request demo at https://kgbase.com/pages/request-demo

## If you have any questions
Please email at customersuccess@thinknum.com

License
----

MIT
