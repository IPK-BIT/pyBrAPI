import pytest
from unittest.mock import MagicMock
from pybrapi import BrAPI
from pybrapi.models.core import Trial

@pytest.fixture
def mock_core():
    core_mock = MagicMock()
    core_mock.get_trials.return_value = [Trial(trialDbId='bridge', trialName='BRIDGE')]
    return core_mock

@pytest.fixture
def brapi_instance(mock_core, monkeypatch):
    monkeypatch.setattr("pybrapi.core.Core", lambda: mock_core)
    brapi = BrAPI(base_url="https://test-server.brapi.org/brapi/v2")
    brapi.get_trials = mock_core.get_trials
    return brapi

def test_get_trials(brapi_instance, mock_core):
    response: list[Trial] = brapi_instance.get_trials()
    mock_core.get_trials.assert_called_once_with()
    assert response[0].trialDbId == 'bridge'