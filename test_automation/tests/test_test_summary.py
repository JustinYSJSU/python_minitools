import pytest
from test_summary import summarize_results

class TestTestSummary():

    def test_normal_input(self, generate_normal_data):
        results = summarize_results(results=generate_normal_data["data"])

        assert results == generate_normal_data["results"]

    def test_empty_input(self, generate_empty_data):
        results = summarize_results(results=generate_empty_data["data"])

        assert results == generate_empty_data["results"]