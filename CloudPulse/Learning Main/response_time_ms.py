
# Project: CloudPulse
# Experiment: Test performance classification

from performance import classify_performance

# Test different response-time values
test_times = [120, 750, 1500, None]

for response_time in test_times:
    performance = classify_performance(response_time)
    print(response_time, "ms:", performance)
