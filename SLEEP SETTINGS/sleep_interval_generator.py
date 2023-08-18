def generate_active_times(sleep_time, active_time, total_time=2000):
    start_time = 0
    intervals = []

    while start_time + sleep_time + active_time <= total_time:
        intervals.append((start_time, start_time + active_time))
        start_time += sleep_time + active_time

    return intervals

def main():
    cycles = [
        (9, 1),
        (10, 2),
        (15, 5),
        (30, 10),
        (5, 2),
        (10, 5),
        (5, 5),
        (16, 24),
        (10, 30),
        (90, 10),
        (10, 90),
        (1000, 200),
        (300, 100),
        (500, 200),
        (100, 50),
        (500, 500),
        (160, 240),
        (100, 300),
    ]

    for sleep, active in cycles:
        intervals = generate_active_times(sleep, active)
        flattened_intervals = [str(val) for sublist in intervals for val in sublist]
        print(f"Sleep time: {sleep}, Active time: {active} => Group1.activeTimes = {', '.join(flattened_intervals)}")

if __name__ == "__main__":
    main()

