from dataclasses import dataclass
from pybrapi.authentication import AbstractAuth
from pybrapi.__utils__.__collector__ import __collect_results__

@dataclass
class Germplasm():
    
    def get_germplasm(self, base_url: str, auth: AbstractAuth|None , **kwargs):
        headers = {}
        if auth:
            headers["Authorization"] = auth.get_auth_string()
        return __collect_results__(f"{base_url}/germplasm", headers, kwargs)
