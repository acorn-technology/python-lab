# Network (HTTP)

In this lab we will work with data served over HTTP.

## 1 Client

The task here will be to build a very simple version of a board showing the coming departures at a train station.

The data will be fetched from [Tågtider API](http://tagtider.net/api/).

We are using the package `marshmallow_dataclass` that leverages the Python data classes (Python 3.7+). To parse a string containing a `Person` in JSON format we can do the following

```Python
from dataclasses import dataclass
import marshmallow_dataclass

@dataclass
class Person:
    name: str
    age: int

person_schema = marshmallow_dataclass.class_schema(Person)()

person = person_schema.loads('{ "name": "John", "age": 42 }')
```

There are many ways of performing HTTP requests in Python, a popular option is the `requests` package. Performing a GET request is rather straight forward

```Python
import requests

response = requests.get('https://google.se')
print(response.text[:500])
```

`requests` also provides a convenient way of dealing with authentication. Tågtider API is using Digest Auth

```Python
from requests.auth import HTTPDigestAuth
import requests

auth = HTTPDigestAuth('user', 'pwd')
response = requests.get('url', auth=auth)
```

### 1.1 

Using the API, fetch the station that is closest to `lat = 57.7056108, long = 11.9667294`.

### 1.2

Print information about the 10 upcoming departures from the closest station.