import sys
from helpers import levenshtein_distance
from helpers.hamming_distance import HammingDistance
from helpers.levenshtein_distance import LevenshteinDistance

def init_algos() -> tuple:
    """
    This method to init and start the algorithms based on the user choices
    """
    print("Please chose your algorithm: \n 1-Hamming Distance \n 2-Levenshtein Distance")
    algo = input("Enter your choice: ")

    if int(algo) not in [1,2]:
        raise ValueError("Enter a valid value!")

    source_string = input("enter your first string: ")
    destination_string = input("enter your second string: ")
    return algo, source_string, destination_string


if __name__ == "__main__":
    algo, source_string, destination_string = init_algos()

    if int(algo) == 1:
        """
        Check for hamming algo
        """
        hamming = HammingDistance(source_string, destination_string)
        print("hamming distance operation => ", hamming.do_haming())
    if int(algo) == 2:
        levenshtein = LevenshteinDistance(source_string, destination_string)
        print("levenshtein distance operation => ", levenshtein.do_levenshtein())