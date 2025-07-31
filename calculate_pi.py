def calculate_pi(n_terms: int) -> float:
    """
    Calculates an approximation of pi using the Leibniz formula.
    """
    numerator = 4.0
    denominator = 1.0
    operator = 1.0
    pi = 0.0
    for _ in range(n_terms):
        pi += operator * (numerator / denominator)
        denominator += 2.0
        operator *= -1.0
    return pi

if __name__ == "__main__":
    pi_approx = calculate_pi(100000)
    print(f"The approximate value of pi is: {pi_approx}")
