from dataclasses import dataclass
from pybrapi.authentication import AbstractAuth
from pybrapi.modules import core, phenotyping, germplasm

@dataclass
class BrAPI:
    base_url: str = "https://test-server.brapi.org/brapi/v2"
    auth: AbstractAuth|None = None
    
    __core__: core.Core = core.Core()
    __germplasm__: germplasm.Germplasm = germplasm.Germplasm()
    __phenotyping__: phenotyping.Phenotyping = phenotyping.Phenotyping()
    
    def get_germplasm(self, **kwargs):
        return self.__germplasm__.get_germplasm(self.base_url, self.auth, **kwargs)
    
    def get_observations(self, **kwargs):
        return self.__phenotyping__.get_observations(self.base_url, self.auth, **kwargs)
    
    def get_observations_as_dataframe(self, **kwargs):
        return self.__phenotyping__.get_observations_as_dataframe(self.base_url, self.auth, **kwargs)
    
    def get_observation_units(self, **kwargs):
        return self.__phenotyping__.get_observation_units(self.base_url, self.auth, **kwargs)
    
    def get_observation_variables(self, **kwargs):
        return self.__phenotyping__.get_observation_variables(self.base_url, self.auth, **kwargs)
    
    def get_studies(self, **kwargs):
        return self.__core__.get_studies(self.base_url, self.auth, **kwargs)
    
    def get_trials(self, **kwargs):
        return self.__core__.get_trials(self.base_url, self.auth, **kwargs)
    