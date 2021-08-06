# Kgbase

## Installation
```
pip install kgbase
```

## Authentication

To import library.
```
from kgbase import Query
```

To authenticate:
```python
q = Query()
q.login(
    username='Your username',
    password='Your password'
)
```

You must first signup from kgbase website. Your password must not be shared or exposed via publicly accessible resources (such as browser client-side scripting).

To use a proxy:
```python
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

q = Query(
    proxies=proxies
)
```

To ignore verifying the SSL certficate:
```python
q = Query(
    verify=False
)
```

To get user state:
```python
q.get_user_state()
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

The `projectId` is returned from response. You need to know `projectId` when you update or detroy project.
```json
{
    "ok": true,
    "project": {
        "uuid": "a0406c6d-122a-4ff2-af7f-976ba5cbca01",
        "graphqlId": "Project/1509",
        "projectId": "ctx-M53lgnjpCkc_plt0lqo",
        "...": "..."
    }
}
```

To get project state:
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

The `tableId` is returned from the response. You need to know `tableId` when you update or delete table.
```json
{
    "ok": true,
    "tableId": "tab-M53nDu1y1SXMVA_ny97"
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
    table_id='tab-M53nDu1y1SXMVA_ny97',
    display_name='company',
    data_type='text'
)
```

The `data_type` should be one of `text`, `number`, `boolean`, `url`, `date`, `date_added`, `date_udated`, `auto_id`, `link_one`, `link_many`.

You can specify prefix for `auto_id` column using optional `data_format` property.

The `columnId` is returned from the response. You need to know `columnId` when you update or delete column.
```json
{
    "ok": true,
    "columnId": "col-1"
}
```

To create `link_one` or `link_many` column:
```python
result = q.create_column(
    project_id='ctx-M53lgnjpCkc_plt0lqo',
    table_id='tab-M53nDu1y1SXMVA_ny97'
    display_name='manufacturer',
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
    display_name='price',
    data_type='number',
)
```

To update column to link to table:
```python
q.update_column(
    project_id='ctx-M53pLqASSUmxj5yU7LO',
    table_id='tab-M53pRIARajeAYTwPIAN',
    column_id='col-2',
    display_name='product',
    data_type='link_many',
    linked_table='tab-dfj23eijSFdfewf'
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
```python
q.create_vertex(
    project_id='ctx-M53pLqASSUmxj5yU7LO',
    table_id='tab-M53pRIARajeAYTwPIAN',
    values={
        'col-0': 'Google',                  # text
        'col-1': 10.5,                      # number
        'col-2': False,                     # boolean
        'col-3': 'https://google.com',      # url
        'col-4': datetime.datetime.today()  # date
        # 'col-5'     # date_added
    },
    edges=[]
)
```

Note that you don't have to set `date_added`, `date_updated` and `auto_id` type columns when creating vertex since values are set automatically. Also `column_ids` and `values` lists should have same size, and each value in list should match with each data type of columns that you defined before.

The `vertexId` is returned from the result. You need to know `vertexId` when you update or delete vertex.

```json
{
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
```

To create vertex linking to another table's vertex:
```python
q.create_vertex(
    project_id='ctx-M57S8onUVXwdNMRgHPf',
    table_id='tab-M57wxxBqH0D7aKgYhhH',
    values={
        'col-0': 'Apple7',
        'col-1': True,
        'col-2': ''
    },
    edges=[
        ("column3", "row-M587jZETRpuCBIXUfw6"),
        ("column3", "row-M58Ac6n8CjPhqp8-u7M")
    ]
)
```

The `edges` is a list of tuples which includes `Column Label` and a `vertexId` that is linked to.


To update vertex:
```python
q.update_vertex(
    project_id='ctx-M53pLqASSUmxj5yU7LO',
    table_id='tab-M53pRIARajeAYTwPIAN',
    vertex_id='row-M53tT_jTviJ50qyzgsL',
    values={
        'col-1': 'Google', 
        'col-2': 'Pixel 3'
    },
    edges= []
)
```

To create edge to existing vertex:
```python
result = q.update_vertex(
    project_id='ctx-M57S8onUVXwdNMRgHPf',
    table_id='tab-M57wxxBqH0D7aKgYhhH',
    vertex_id='row-M588L2W5S9WZJ5t2Spn',
    values={
        'col-0': 'Google',
        'col-1': True,
        'col-2': ''
    },
    edges=[
        ("column3", "row-M587jZETRpuCBIXUfw6"),
        ("column3", "row-M58A84uaVMbCC16pSUA")
    ]
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

To get schema of project:
```python
q.get_schema(
    project_id='ctx-M53lgnjpCkc_plt0lqo'
)
```

You can see tables and columns belonging to the project.
```json
{
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
```

## Graph

To get vertices:
```python
q.get_graph(
    project_id='ctx-M53zulrvmCoNnP7PMEU',
    table_id='tab-M53zumOvT3xKmqkIB_X',
    filters=[],
    offset=0,
    limit=50
)
```

To add filtering:
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
    offset=0,
    limit=50
)
```

To add group by and aggregations:
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
    offset=0,
    limit=50
)
```

The `function` should be one of `count`, `sum`, `mean`, `max`, `min`.

## Bulk Upload

To upload csv file:
```python
q.bulk_upload(
    project_id='ctx-M57S8onUVXwdNMRgHPf',
    table_id='tab-MK09gSNWBtZ-g2iLW8-',
    filepath='/Users/sangwonseo/Downloads/company1.csv',
    column_ids=['col-0', 'col-1', 'col-2'],
    configs={
        'countSkipRows': 0,
        'hasHeader': False,
        'dropEmpty': False
    }
)
```

Note that csv files should follow Amazon neptune csv format. For more details, please refer to the documentation. https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html

## For more details about Kgbase
Please visit https://kgbase.com/pages/learn

## If you are interested in Kgbase demo
Please request demo at https://kgbase.com/pages/request-demo

## If you have any questions
Please email at customersuccess@thinknum.com

License
----

MIT
