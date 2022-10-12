# Complice API

This is a Python wrapper for the [Complice](https://complice.co) API.

## Installation

```bash
pip install complice-api
```

## Usage

```python
from complice import CompliceAPI


complice = CompliceAPI('your_auth_token') # replace with your auth token, found at https://complice.co/apiclient/docs
complice.print_goals()
```
