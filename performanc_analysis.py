import time
import random

# Deterministic Selection (Median of Medians)
# ------------------------------
def deterministic_select(arr, k):
    # Base case: small array, just sort and return k-th element
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Step 1: Divide array into groups of 5 elements each
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    # Step 2: Find medians of all groups
    medians = [sorted(group)[len(group)//2] for group in groups]

    # Step 3: Recursively find median of medians (pivot)
    pivot = deterministic_select(medians, len(medians) // 2)

    # Step 4: Partition the array based on pivot
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    # Step 5: Recurse into the appropriate partition
    if k < len(lows):
        return deterministic_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return deterministic_select(highs, k - len(lows) - len(pivots))

# Randomized Selection (Quickselect)
# ------------------------------
def randomized_select(arr, k):
    # Base case: only one element
    if len(arr) == 1:
        return arr[0]

    # Step 1: Choose a random pivot
    pivot = random.choice(arr)

    # Step 2: Partition the array
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    # Step 3: Recurse based on position of k
    if k < len(lows):
        return randomized_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return randomized_select(highs, k - len(lows) - len(pivots))

# Benchmarking function to measure average runtime
# ------------------------------
def benchmark(algorithm, size, k, runs=5):
    total_time = 0
    for _ in range(runs):
        # Generate a new random array for each run
        arr = [random.randint(1, size * 10) for _ in range(size)]

        # Measure execution time
        start = time.perf_counter()
        algorithm(arr, k)
        end = time.perf_counter()

        # Accumulate total time
        total_time += (end - start)

    # Return average time over all runs
    return total_time / runs

# Configuration for testing
# ------------------------------
sizes = [100, 500, 1000, 5000, 10000]  # Different array sizes to test
runs = 5  # Number of repetitions for averaging

# Print table header
print(f"{'Size':>6} | {'Rand Time (s)':>15} | {'Det Time (s)':>15}")
print("-" * 42)

# Run benchmark for each array size
for size in sizes:
    k = size // 2  # Median (k-th smallest element)
    
    # Run benchmarks
    rand_time = benchmark(randomized_select, size, k, runs)
    det_time = benchmark(deterministic_select, size, k, runs)

    # Print result in tabular format
    print(f"{size:>6} | {rand_time:>15.6f} | {det_time:>15.6f}")
