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

## 2 Server

Python generally have multiple ways of doing things. Setting up a web server is no exception. There are A LOT of choices when selecting sever, documentation generation, etc. In this lab we will use: flask, flask_restx and marshmallow_dataclass.

flask_restx simplifies creation of REST APIs. An API can be split into multiple namespaces

```Python
foo_api = Namespace('api/foo', description='Example namespace')
```

Models are created in the namespace for use with routes further on

```Python
foo_request = foo_api.model(
    'FooRequest',
    {
        'bar': fields.String(required=True, description="Who knows", help="Unhelpful"),
        'biz': fields.Integer(required=False)
    })
```

Resources are then added to the namespace with routes

```Python
from flask_restx import Namespace, Resource, fields

@foo_api.route('')
class Foo(Resource):
    @foo_api.expect(foo_request)
    @foo_api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Bad state'})
    def post(self):
        print(request.json)
        return 'baz', 200
```

This resource will process POST requests to /api/foo and expect a request body matching the model.

### 2.1

Copy the files `main.py` and `start.sh` pr `start.ps1`. Create a file called `count.py` that export a namespace `count_api`. Add two endpoints to this namespace, one that allows you to add/subtract to a number kept in memory, and one that returns that number.

The endpoint performing arithmetic should take the arguments in the request body and use marshmallow_dataclass to parse the data.