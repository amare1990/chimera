# skills/trend_fetcher/trend_fetcher.py

"""Simple trend_fetcher skill implementation used for tests and local development.

The real project would call an external trends API; this lightweight
implementation returns deterministic mock results matching
`specs/technical.md` and `tests/test_trend_fetcher.py` expectations.
"""

def run(input_json):
    """Fetch top trending topics for a region.

    Args:
        input_json (dict): expected keys: `region` (str), `limit` (int)

    Returns:
        dict: {"topics": [{"name": str, "score": number}, ...]}

    The output shape intentionally matches the test contract which
    expects a list of topic dicts with `name` and `score` keys.
    """
    if not isinstance(input_json, dict):
        raise TypeError("input_json must be a dict")

    region = input_json.get("region", "global")
    limit = input_json.get("limit", 3)

    try:
        limit = int(limit)
    except Exception:
        limit = 3

    if limit < 0:
        limit = 0

    topics = []
    # deterministic mock: topic names include region and incremental index,
    # scores decrease slightly so consumers can sort or filter if needed.
    for i in range(limit):
        name = f"{region}-topic-{i+1}"
        score = round(max(0.0, 1.0 - i * 0.05), 4)
        topics.append({"name": name, "score": score})

    return {"topics": topics}
