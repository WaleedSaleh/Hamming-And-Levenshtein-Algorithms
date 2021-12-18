class LevenshteinDistance(object):
    """
    This is the class for calculating the Levenshtein Distance Operations
    """

    def __init__(self, source_string: str, destination_string:str) -> None:
        """
        class initalizer
        """
        self.source_string = source_string
        self.destination_string = destination_string
        self.check_levenshtein_strings()


    def check_levenshtein_strings(self) -> None:
        """
        This is a helper validaator for strings
        as the hammstring algorithm only work with strings with the same length
        :param:source_string:str
        :param:destination_string
        :rtype:
        """
        if self.source_string.isdigit() or self.destination_string.isdigit():
            raise ValueError("Please make sure your inputs are strings only!")


    @property
    def __get_source_string_length(self) -> int:
        """
        This method to retrieve the length of each string
        here we are adding 1 to the length for the white space
        in order to follow the algorithm rules.
        """
        return len(self.source_string) + 1


    @property
    def __get_destination_string_length(self) -> int:
        """
        This method to retrieve the length of each string
        here we are adding 1 to the length for the white space
        in order to follow the algorithm rules.
        """
        return len(self.destination_string) + 1

    def do_levenshtein(self) -> int:
        """
        This is the main function that resonsible for creating the levenshtein job
        :rtype:int
        """
        return self.__get_distance()


    def __get_distance(self) -> int:
        """
        This is the method that finds the distance for strings
        :param:n:int represents the length
        :rtype:int
        """
        rows = self.__get_source_string_length
        cols = self.__get_destination_string_length
        matrix = [[0 for x in range(cols)] for x in range(rows)]

        for i in range(1, rows):
            matrix[i][0] = i

        for i in range(1, cols):
            matrix[0][i] = i

        for col in range(1, cols):
            for row in range(1, rows):
                if self.source_string[row-1] == self.destination_string[col-1]:
                    cost = 0
                else:
                    cost = 1

                matrix[row][col] = min(matrix[row-1][col] + 1, matrix[row][col-1] + 1, matrix[row-1][col-1] + cost)

        return matrix[row][col]
