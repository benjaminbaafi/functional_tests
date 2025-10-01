from typing import Tuple


def sequence(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    def loop(k: int, a: int, b: int) -> Tuple[int, int]:
        if k == 0:
            return (a, b)
        return loop(k - 1, b, a + b)

    return loop(n, 0, 1)[0]
