# metabase

## Installation
```
pip install kgbase
```

## Query

Import library.

```
from thinknum import Query
```

To authenticate, you must first obtain a client_id and client_secret from your assigned Thinknum account manager. Your client_secret must not be shared or exposed via publicly accessible resources (such as browser client-side scripting).

```python
q = Query(
    client_id='Your client id',
    client_secret='Your client secret'
)
```

If you need to use a proxy, you can configure it with the proxies argument.

```python
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

q = Query(
    client_id='Your client id',
    client_secret='Your client secret',
    proxies=proxies
)
```

Requests can ignore verifying the SSL certficate if you set verify to False. By default, verify is set to True.

```python
q = Query(
    client_id='Your client id',
    client_secret='Your client secret',
    verify=False
)
```

You will get a list of datasets, each of which has the dataset id and its display_name.
```python
q.get_dataset_list()
```

You will get dataset's metadata.
```python
q.get_dataset_metadata(dataset_id='job_listings')
```

It's possible to limit the dataset list to a specific ticker by specific a "ticker" query parameter. For example, getting all datasets available for Apple Inc:

```python
q.get_ticker_dataset_list(query='nasdaq:aapl')
```

You can search for tickers.
```python
q.get_ticker_list(query="tesla")
```

You can also search for tickers of particular dataset
```python
q.get_ticker_list(query="tesla", dataset_id='job_listings')
```

You can retrieve data for specific dataset and tickers with various filters. For example:

```python
q.add_ticker('nasdaq:lulu') # Add ticker
q.add_filter(
    column='as_of_date',
    type='>=',
    value=["2020-01-05"]
)  # Add filter
q.add_sort(
    column='as_of_date',
    order='asc'
)   # Add Sort
q.get_data(dataset_id='job_listings')    # Retrieve data
```

You can also specify `start` and `limit`. The default values are `1` and `100000`.
```
q.get_data(dataset_id='job_listings', start=1, limit=1000)
```

Sometimes you only need get aggregated results for a dataset. In such cases you can retrieve them through the `addGroup` and `addAggregation` functions.

```python
q.add_ticker('nasdaq:lulu') # Add ticker
q.add_group(column='as_of_date') # Add group
q.add_aggregation(
    column='dataset__entity__entity_ticker__ticker__ticker',
    type='count'
)   # Add aggregation
q.add_sort(
    column='as_of_date',
    order='asc'
)   # Add sort
q.get_data(dataset_id='job_listings')
```

There a few functions that you can apply to queries to gather even more insight into the data. You can retrieve a listing of the available functions in a dataset with the `getDatasetMetadata` function. For example, there is `nearby` function for `store` dataset.

```
q.add_ticker('nasdaq:lulu')
q.add_function(
    function='nearby',
    parameters={
        "dataset_type": "dataset",
        "dataset": "store",
        "tickers":["nyse:ua"],
        "entities": [],
        "distance": 5,
        "is_include_closed": False
    }
)
q.get_data(dataset_id='store')
```

Also, you can apply `nearest` function to `store` dataset like the following code.
```
q.add_ticker('nasdaq:lulu')
q.add_function(
    function='nearest',
    parameters={
        "dataset_type": "dataset",
        "dataset": "store",
        "tickers":["nyse:ua"],
        "entities": [],
        "ranks": [1],
        "is_include_closed": False
    }
)
q.get_data(dataset_id='store')
```

## History

Import library.

```
from thinknum import History
```

Like the `Query` library, you must authenticate to utilize `History` library.

```python
h = History(
    client_id='Your client id',
    client_secret='Your client secret'
)
```

If you need to use a proxy, you can configure it with the proxies argument.

```python
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

h = History(
    client_id='Your client id',
    client_secret='Your client secret',
    proxies=proxies
)
```

Requests can ignore verifying the SSL certficate if you set verify to False. By default, verify is set to True.

```python
h = History(
    client_id='Your client id',
    client_secret='Your client secret',
    verify=False
)
```

To retrieve a list of available history for a dataset:

```python
h.get_history_list(dataset_id='store')
```

You can view the metadata for the historical file:

```python
h.get_history_metadata(
    dataset_id='store',
    history_date='2020-03-09'
)
```

To download a CSV of the historical data:

```python
h.download(
    dataset_id='store',
    history_date='2020-03-09'
)
```

You can specify download path:

```python
h.download(
    dataset_id='store',
    history_date='2020-03-09', 
    download_path='/Users/sangwonseo/Downloads'
)
```

## For more details about Library or API
Please visit https://docs.thinknum.com/docs

## If you are interested in Thinknum
Please request demo at https://www.thinknum.com/demo/

## If you have any questions
Please email at customersuccess@thinknum.com

License
----

MIT
