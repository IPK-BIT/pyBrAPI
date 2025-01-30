from dataclasses import dataclass
from base64 import b64encode
import requests

@dataclass
class AbstractAuth:
    def get_auth_string(self):
        raise NotImplementedError("get_auth_string not implemented")
    
@dataclass
class BasicAuth(AbstractAuth):
    username: str
    password: str
    
    def get_auth_string(self):
        return f"Basic {b64encode(f'{self.username}:{self.password}'.encode()).decode()}"
    
@dataclass
class OIDCAuth(AbstractAuth):
    oidc_url: str
    oidc_details: dict
    __token__: str = None
    __refresh_token__: str = None
    
    def __init__(self, oidc_url: str, oidc_details: dict):
        self.oidc_url = oidc_url
        self.oidc_details = oidc_details
        self.__token__ = self.get_token()
    
    def get_token(self):
        response = requests.post(f"{self.oidc_url}/token", data=self.oidc_details)
        response.raise_for_status()
        self.__refresh_token__ = response.json()["refresh_token"]
        return response.json()["access_token"]
    
    def get_auth_string(self):
        return f"Bearer {self.__token__}"
    
    def refresh(self):
        self.__token__ = self.get_token()