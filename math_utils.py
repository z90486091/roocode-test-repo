import random

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

def create_markov_chain(text: str) -> dict:
    """
    Creates a Markov chain from a given text.
    """
    words = text.split()
    markov_chain = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i+1]
        if current_word in markov_chain:
            markov_chain[current_word].append(next_word)
        else:
            markov_chain[current_word] = [next_word]
    return markov_chain

if __name__ == "__main__":
    pi_approx = calculate_pi(100000)
    print(f"The approximate value of pi is: {pi_approx}")

    text = "a cat sat on a mat a cat sat on a mat"
    chain = create_markov_chain(text)
    print(f"Markov chain: {chain}")
