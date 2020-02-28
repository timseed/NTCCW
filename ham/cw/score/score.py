import Levenshtein

"""
Calculate simularaties between the files
"""


class Score:
    def __init__(self, f1, f2):
        """
        Get input files
        :param f1:
        :param f2:
        """
        self.str1 = ""
        self.str2 = ""

        with open(f1, "rt") as if1:
            self.str1 = if1.read()
        with open(f2, "rt") as if2:
            self.str2 = if2.read()

    def _setstr1(self,str1):
        self.str1=str1

    def _setstr2(self,str2):
        self.str2=str2

    def get_score(self):
        """
        Calculate Levenstein distance.
        All text is made lower-case.
        :return:
        """

        return Levenshtein.distance(self.str1.lower(), self.str2.lower())
