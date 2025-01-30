from dataclasses import dataclass
from pybrapi.authentication import AbstractAuth
from pybrapi.__utils__.__collector__ import __collect_results__
from pybrapi.models.core import Study, Trial

@dataclass
class Core():
    
    def get_trials(self, base_url: str, auth: AbstractAuth|None, **kwargs) -> list[Trial]:
        headers = {}
        if auth:
            headers["Authorization"] = auth.get_auth_string()
        return [Trial(**trial) for trial in __collect_results__(f"{base_url}/trials", headers, kwargs)]

    def get_studies(self, base_url: str, auth: AbstractAuth|None, **kwargs) -> list[Study]:
        headers = {}
        if auth:
            headers["Authorization"] = auth.get_auth_string()
        return [Study(**study) for study in __collect_results__(f"{base_url}/studies", headers, kwargs)]