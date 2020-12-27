# Ecocode

Monitoring system to gather information about how your models / algorithms run


## How to use it ?

### Monitor a function

To monitor a function, you just need to do the following:
```python
from ecocode import ecocode_decorator

@ecocode_decorator(
    country="FR",
    name="My Super function",
    api_key="your-api-key"
)
def function(*arg, **kwargs):
    ...
```

And it will monitor your process and send the results at the end of the process.

### Monitor a Flask app

Not yet available

