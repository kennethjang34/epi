from test_framework import generic_test


def compute_binomial_coefficient(n: int, k: int) -> int:
    if (n - k) % n == 0:
        return 1
    if n % k == 0:
        return compute_binomial_coefficient(n - 1, k - 1) * (n / k)
    else:
        return (compute_binomial_coefficient(n - 1, k - 1) / k) * n


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "binomial_coefficients.py",
            "binomial_coefficients.tsv",
            compute_binomial_coefficient,
        )
    )
