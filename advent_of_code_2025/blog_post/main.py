import timeit

from aoc import solve

if __name__ == "__main__":
    with open("large_case.txt") as f:
        page = f.read()

    assert solve(page) == 4135

    runs = 600
    print(f"Python:\t\t{timeit.timeit(lambda: solve(page), number=runs):.4f}")

