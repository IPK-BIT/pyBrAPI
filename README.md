# pyBrAPI

## Project Overview
pyBrAPI is a Python package that provides convenient access to data from BrAPI servers. It simplifies interacting with BrAPI endpoints by handling REST requests and responses, and returns data typed into data models.

## Setup and Installation
Download the release from this Github repository. Then install the package using `pip`:

```
pip install dist/pybrapi-0.1.0-py3-none-any.whl
```

## Usage Instructions
### Connect to server
```py
from pybrapi import BrAPI

server = BrAPI('https://test-server.brapi.org/brapi/v2/')
```

### Request Germplasm
```py
response = server.get_germplasm(germplasmDbId="germplasm1")
```

Similar functions are provided for:
- trials
- studies
- observations
- observation units
- observation variables

### Request Observations Tables
Additionally for observations, users can receive the data in a pandas data frame.
```py
df = server.get_observations_as_dataframe(observationVariableDbId="variable1")
```


## Features
- Simplified interface for querying BrAPI endpoints
- Typed data models for returned data
- Handles authentication and connection management
- Supports various BrAPI operations like retrieving germplasm, observations, trials, etc.

## License
- The project is licensed under [MIT License](LICENSE)

## Additional Resources
- [BrAPI](https://brapi.org)
- [BrAPI Specification](https://brapi.org/specification)