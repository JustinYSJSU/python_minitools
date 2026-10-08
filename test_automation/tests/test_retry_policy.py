import pytest
from retry_policy import should_retry

class TestRetryPolicy:

    @pytest.mark.parametrize("test_data, result", [
        ({"status": "passed", "attempts": 1, "failure_type": None}, False),
        ({"status": "failed", "attempts": 1, "failure_type": "network"}, True),
        ({"status": "failed", "attempts": 1, "failure_type": "timeout"}, True),
        ({"status": "failed", "attempts": 1, "failure_type": "assertion"}, False),
        ({"status": "failed", "attempts": 1, "failure_type": "unknown"}, False),
        ({"status": "failed", "attempts": 2, "failure_type": "network"}, False)
    ])
    def test_retry(self, test_data, result):
        res = should_retry(job=test_data)
        assert res == result
