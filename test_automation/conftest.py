import pytest

@pytest.fixture
def generate_normal_data():
    return(
        {
            "data": [
                {
                    "name": "test_login",
                    "status": "passed",
                    "duration": 0.42,
                },
                {
                    "name": "test_logout",
                    "status": "failed",
                    "duration": 0.18,
                },
                {
                    "name": "test_signup",
                    "status": "skipped",
                    "duration": 0.05,
                },
            ],
            "results":{
                "passed": 1,
                "failed": 1,
                "skipped": 1,
                "total_duration": 0.65
            }
        }
    )

@pytest.fixture
def generate_empty_data():
    return(
        {
            "data": [],
            "results":{
                "passed": 0,
                "failed": 0,
                "skipped": 0,
                "total_duration": 0.0
            }
        }
    )