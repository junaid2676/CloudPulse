
from performance import classify_performance


def test_fast_response():
    assert classify_performance(120) == "FAST"


def test_slow_response():
    assert classify_performance(750) == "SLOW"


def test_very_slow_response():
    assert classify_performance(1500) == "VERY SLOW"


def test_missing_response_time():
    assert classify_performance(None) == "UNKNOWN"
