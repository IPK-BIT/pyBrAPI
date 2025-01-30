import pandas as pd
from dataclasses import dataclass
from pybrapi.authentication import AbstractAuth
from pybrapi.__utils__.__collector__ import __collect_results__
from pybrapi.models.phenotyping import Observation, ObservationUnit, ObservationVariable

@dataclass
class Phenotyping():
    
    def get_observations(self, base_url: str, auth: AbstractAuth|None , **kwargs) -> list[Observation]:
        headers = {}
        if auth:
            headers["Authorization"] = auth.get_auth_string()
        return [Observation(**observation) for observation in __collect_results__(f"{base_url}/observations", headers, kwargs)]
    
    def get_observation_units(self, base_url: str, auth: AbstractAuth, **kwargs) -> list[ObservationUnit]:
        headers = {}
        if auth:
            headers["Authorization"] = auth.get_auth_string()
        return [ObservationUnit(**observationUnit) for observationUnit in __collect_results__(f"{base_url}/observationunits", headers, kwargs)]
    
    def get_observation_variables(self, base_url: str, auth: AbstractAuth, **kwargs) -> list[ObservationVariable]:
        headers = {}
        if auth:
            headers["Authorization"] = auth.get_auth_string()
        return [ObservationVariable(**observationVariable) for observationVariable in __collect_results__(f"{base_url}/variables", headers, kwargs)]
    
    def get_observations_as_dataframe(self, base_url: str, auth: AbstractAuth, **kwargs) -> pd.DataFrame:
        if not "pageSize" in kwargs:
            kwargs["pageSize"] = 50
        headers = {}
        if auth:
            headers["Authorization"] = auth.get_auth_string()
        results = __collect_results__(f"{base_url}/observations/table", headers, kwargs)
        headerRow: list[str] = results["headerRow"]
        for var in results["observationVariables"]:
            headerRow.append(var["observationVariableDbId"])
        df = pd.DataFrame(results["data"], columns=headerRow)
        return df
