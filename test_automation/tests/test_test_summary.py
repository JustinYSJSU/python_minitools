import pytest
from test_summary import summarize_results

class TestTestSummary():

    def test_normal_input(self, generate_normal_data):
        results = summarize_results(results=generate_normal_data["data"])

        assert results == generate_normal_data["results"]

    def test_empty_input(self, generate_empty_data):
        results = summarize_results(results=generate_empty_data["data"])

        assert results == generate_empty_data["results"]

    def test_same_result_input(self, generate_same_result_data):
        results = summarize_results(results=generate_same_result_data["data"])

        assert results == generate_same_result_data["results"]
    
    def test_invalid_status(self, generate_invalid_status_data):
        with pytest.raises(ValueError, match="Unknown status"):
            summarize_results(results=generate_invalid_status_data["data"])
    
    @pytest.mark.parametrize("data", (
            [
                {
                    "name": "test_login",
                    "duration": 0.42,
                },
                {
                    "name": "test_logout",
                    "duration": 0.18,
                },
                {
                    "name": "test_signup",
                    "duration": 0.05,
                },
            ],
            [
                {
                    "name": "test_login",
                    "status": "passed",
                },
                {
                    "name": "test_logout",
                    "status": "failed",
                },
                {
                    "name": "test_signup",
                    "status": "passed",
                },
            ]
    ))
    def test_missing_key(self, data):
        with pytest.raises(KeyError):
            summarize_results(results=data)