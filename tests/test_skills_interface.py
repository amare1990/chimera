"""
Failing tests that enforce Skill interfaces.

Defines the 'Empty Slot' for the agent.
"""

import inspect

def test_all_skills_have_run_function():
    import skills

    expected = [
        "trend_fetcher.trend_fetcher",
        "content_generator.content_generator",
        "publisher.publisher"
    ]

    for name in expected:
        # Import the module dynamically
        module = __import__(f"skills.{name}", fromlist=["run"])

        # Ensure run() exists
        assert hasattr(module, "run"), f"{name} must expose run()"

        # Ensure run() accepts exactly 1 JSON input
        sig = inspect.signature(module.run)
        assert len(sig.parameters) == 1, "run() must accept single JSON input"
