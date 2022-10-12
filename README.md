# complice-api
Python wrapper for the [Complice](https://complice.co) API.

## Installation
```bash
pip install complice-api
```

## Usage
```python
from complice import CompliceAPI

# replace with your auth token, found at https://complice.co/apiclient/docs
complice = CompliceAPI('<AUTH_TOKEN>') 

complice.get_goals()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
