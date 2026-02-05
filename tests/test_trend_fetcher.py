"""
Failing contract test for trend_fetcher Skill

Purpose:
Validate that returned structure matches specs/technical.md API contract.
This test MUST fail until the skill is implemented.
"""

import pytest

def test_trend_fetcher_contract():
    # Import run() from the folder-based skill package
    from skills.trend_fetcher.trend_fetcher import run

    # Call the run() placeholder with sample JSON input
    result = run({"region": "US", "limit": 5})

    # Assert the output structure matches the spec
    assert isinstance(result, dict), "Result must be a dictionary"
    assert "topics" in result, "Dictionary must contain 'topics' key"

    for topic in result["topics"]:
        assert isinstance(topic["name"], str), "'name' must be a string"
        assert isinstance(topic["score"], (int, float)), "'score' must be numeric"
