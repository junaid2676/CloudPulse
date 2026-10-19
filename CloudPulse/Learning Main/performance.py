def classify_performance(response_time_ms):
    if response_time_ms is None:
        return "UNKNOWN"

    elif response_time_ms < 500:
        return "FAST"

    elif response_time_ms <= 1000:
        return "SLOW"

    else:
        return "VERY SLOW"
