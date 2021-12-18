

class HammingDistance(object):
    """
    This is the class for calculating the hamming string
    """
    __DISTANCE = 0

    def __init__(self, source_string: str, destination_string:str) -> None:
        """
        class initalizer
        """
        self.source_string = source_string
        self.destination_string = destination_string
        self.check_hamming_strings()

    def check_hamming_strings(self) -> None:
        """
        This is a helper validaator for strings
        as the hammstring algorithm only work with strings with the same length
        :param:source_string:str
        :param:destination_string
        :rtype:
        """
        if len(self.source_string) != len(self.destination_string):
            raise ValueError("Please check the length of your inputs")

    @property
    def __get_string_length(self) -> int:
        """
        This method to retrieve the length of each length
        """
        return len(self.source_string) or len(self.destination_string)

    def do_haming(self) -> int:
        """
        This is the main function that resonsible for creating the hamming job
        :rtype:int
        """
        return self.__get_distance(self.__get_string_length)

    def __get_distance(self, n: int) -> int:
        """
        This is the method that finds the distance for strings
        :param:n:int represents the length
        :rtype:int
        """
        if n == 0:
            return self.__DISTANCE
        if self.source_string[n-1] != self.destination_string[n-1]:
            self.__DISTANCE+=1

        return self.__get_distance(n - 1)



