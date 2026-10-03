import pytest
from config_validator import validate_config

class TestConfigValidator():

    def test_valid_config(self):
        valid_config = {
            "host": "localhost",
            "port": 8080,
            "timeout": 5
        }
        assert validate_config(valid_config) == True

    @pytest.mark.parametrize("config", [
        {"port": 8080, "timeout": 5},
        {"host": "localhost", "timeout": 5},
        {"host": "localhost", "port": 8080}
    ])
    def test_missing_field(self, config):
        assert validate_config(config) == False

    @pytest.mark.parametrize("config", [
        {"host": ["localhost"], "port": 8080, "timeout": 5},
        {"host": "localhost", "port": "8080", "timeout": 5},
        {"host": "localhsot", "port": 8080, "timeout": "5"}
    ])
    def test_invalid_types(self, config):
        assert validate_config(config) == False

    @pytest.mark.parametrize("config, result", [
        ({"host": "localhost", "port": 8080, "timeout": 5}, True),
        ({"host": "localhost", "port": -1000, "timeout": 5}, False),
        ({"host": "localhost", "port": 90000, "timeout": 5}, False)
    ])
    def test_port_range(self, config, result):
        assert validate_config(config) == result

    @pytest.mark.parametrize("config", [
        {"host": "localhost", "port": 8080, "timeout": -1},
        {"host": "localhost", "port": 8080, "timeout": 0}
    ])
    def test_timeout_range(self, config):
        assert validate_config(config) == False