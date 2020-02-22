from unittest import TestCase
from ham.cw import Cw


class TestCw(TestCase):
    def setUp(self) -> None:
        self.morse = Cw()
        self.dot = self.morse.dit
        self.dash = self.morse.dah
        self.gap = self.morse.gap
        self.endletter = self.morse.endletter
        self.endword = self.morse.endword

    def test_Cw_Exists(self):
        self.assertIsInstance(self.morse, Cw)

    def test_letter_to_dot_dash(self):
        self.assertEqual(self.morse.letter_to_dot_dash("a"), ".-")
        self.assertEqual(self.morse.letter_to_dot_dash("b"), "-...")
        self.assertEqual(self.morse.letter_to_dot_dash("c"), "-.-.")
        self.assertEqual(self.morse.letter_to_dot_dash("d"), "-..")
        self.assertEqual(self.morse.letter_to_dot_dash("e"), ".")
        self.assertEqual(self.morse.letter_to_dot_dash("f"), "..-.")
        self.assertEqual(self.morse.letter_to_dot_dash("g"), "--.")
        self.assertEqual(self.morse.letter_to_dot_dash("h"), "....")
        self.assertEqual(self.morse.letter_to_dot_dash("i"), "..")
        self.assertEqual(self.morse.letter_to_dot_dash("j"), ".---")
        self.assertEqual(self.morse.letter_to_dot_dash("k"), "-.-")
        self.assertEqual(self.morse.letter_to_dot_dash("l"), ".-..")
        self.assertEqual(self.morse.letter_to_dot_dash("m"), "--")
        self.assertEqual(self.morse.letter_to_dot_dash("n"), "-.")
        self.assertEqual(self.morse.letter_to_dot_dash("o"), "---")
        self.assertEqual(self.morse.letter_to_dot_dash("p"), ".--.")
        self.assertEqual(self.morse.letter_to_dot_dash("q"), "--.-")
        self.assertEqual(self.morse.letter_to_dot_dash("r"), ".-.")
        self.assertEqual(self.morse.letter_to_dot_dash("s"), "...")
        self.assertEqual(self.morse.letter_to_dot_dash("t"), "-")
        self.assertEqual(self.morse.letter_to_dot_dash("u"), "..-")
        self.assertEqual(self.morse.letter_to_dot_dash("v"), "...-")
        self.assertEqual(self.morse.letter_to_dot_dash("w"), ".--")
        self.assertEqual(self.morse.letter_to_dot_dash("x"), "-..-")
        self.assertEqual(self.morse.letter_to_dot_dash("y"), "-.--")
        self.assertEqual(self.morse.letter_to_dot_dash("z"), "--..")
        self.assertEqual(self.morse.letter_to_dot_dash("A"), ".-")
        self.assertEqual(self.morse.letter_to_dot_dash("B"), "-...")
        self.assertEqual(self.morse.letter_to_dot_dash("C"), "-.-.")
        self.assertEqual(self.morse.letter_to_dot_dash("D"), "-..")
        self.assertEqual(self.morse.letter_to_dot_dash("E"), ".")
        self.assertEqual(self.morse.letter_to_dot_dash("F"), "..-.")
        self.assertEqual(self.morse.letter_to_dot_dash("G"), "--.")
        self.assertEqual(self.morse.letter_to_dot_dash("H"), "....")
        self.assertEqual(self.morse.letter_to_dot_dash("I"), "..")
        self.assertEqual(self.morse.letter_to_dot_dash("J"), ".---")
        self.assertEqual(self.morse.letter_to_dot_dash("K"), "-.-")
        self.assertEqual(self.morse.letter_to_dot_dash("L"), ".-..")
        self.assertEqual(self.morse.letter_to_dot_dash("M"), "--")
        self.assertEqual(self.morse.letter_to_dot_dash("N"), "-.")
        self.assertEqual(self.morse.letter_to_dot_dash("O"), "---")
        self.assertEqual(self.morse.letter_to_dot_dash("P"), ".--.")
        self.assertEqual(self.morse.letter_to_dot_dash("Q"), "--.-")
        self.assertEqual(self.morse.letter_to_dot_dash("R"), ".-.")
        self.assertEqual(self.morse.letter_to_dot_dash("S"), "...")
        self.assertEqual(self.morse.letter_to_dot_dash("T"), "-")
        self.assertEqual(self.morse.letter_to_dot_dash("U"), "..-")
        self.assertEqual(self.morse.letter_to_dot_dash("V"), "...-")
        self.assertEqual(self.morse.letter_to_dot_dash("W"), ".--")
        self.assertEqual(self.morse.letter_to_dot_dash("X"), "-..-")
        self.assertEqual(self.morse.letter_to_dot_dash("Y"), "-.--")
        self.assertEqual(self.morse.letter_to_dot_dash("Z"), "--..")
        self.assertEqual(self.morse.letter_to_dot_dash("0"), "-----")
        self.assertEqual(self.morse.letter_to_dot_dash("1"), ".----")
        self.assertEqual(self.morse.letter_to_dot_dash("2"), "..---")
        self.assertEqual(self.morse.letter_to_dot_dash("3"), "...--")
        self.assertEqual(self.morse.letter_to_dot_dash("4"), "....-")
        self.assertEqual(self.morse.letter_to_dot_dash("5"), ".....")
        self.assertEqual(self.morse.letter_to_dot_dash("6"), "-....")
        self.assertEqual(self.morse.letter_to_dot_dash("7"), "--...")
        self.assertEqual(self.morse.letter_to_dot_dash("8"), "---..")
        self.assertEqual(self.morse.letter_to_dot_dash("9"), "----.")

    def test_raises(self):
        self.assertRaises(ValueError, self.morse.letter_to_dot_dash, "±")
        self.assertRaises(ValueError, self.morse.letter_to_dot_dash, "§")
        self.assertRaises(ValueError, self.morse.letter_to_dot_dash, "`")

    def test_cw_timing(self):
        self.assertEqual(
            self.morse.cw_timing("a"), self.dot + self.gap + self.dash + self.endword
        )
        self.assertEqual(
            self.morse.cw_timing("b"),
            self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("c"),
            self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("d"),
            self.dash + self.gap + self.dot + self.gap + self.dot + self.endword,
        )
        self.assertEqual(self.morse.cw_timing("e"), self.dot + self.endword)
        self.assertEqual(
            self.morse.cw_timing("f"),
            self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("g"),
            self.dash + self.gap + self.dash + self.gap + self.dot + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("h"),
            self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("i"), self.dot + self.gap + self.dot + self.endword
        )
        self.assertEqual(
            self.morse.cw_timing("j"),
            self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("k"),
            self.dash + self.gap + self.dot + self.gap + self.dash + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("l"),
            self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("m"), self.dash + self.gap + self.dash + self.endword
        )
        self.assertEqual(
            self.morse.cw_timing("n"), self.dash + self.gap + self.dot + self.endword
        )
        self.assertEqual(
            self.morse.cw_timing("o"),
            self.dash + self.gap + self.dash + self.gap + self.dash + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("p"),
            self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("q"),
            self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("r"),
            self.dot + self.gap + self.dash + self.gap + self.dot + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("s"),
            self.dot + self.gap + self.dot + self.gap + self.dot + self.endword,
        )
        self.assertEqual(self.morse.cw_timing("t"), self.dash + self.endword)
        self.assertEqual(
            self.morse.cw_timing("u"),
            self.dot + self.gap + self.dot + self.gap + self.dash + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("v"),
            self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("w"),
            self.dot + self.gap + self.dash + self.gap + self.dash + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("x"),
            self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("y"),
            self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("z"),
            self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("A"), self.dot + self.gap + self.dash + self.endword
        )
        self.assertEqual(
            self.morse.cw_timing("B"),
            self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("C"),
            self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("D"),
            self.dash + self.gap + self.dot + self.gap + self.dot + self.endword,
        )
        self.assertEqual(self.morse.cw_timing("E"), self.dot + self.endword)
        self.assertEqual(
            self.morse.cw_timing("F"),
            self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("G"),
            self.dash + self.gap + self.dash + self.gap + self.dot + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("H"),
            self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("I"), self.dot + self.gap + self.dot + self.endword
        )
        self.assertEqual(
            self.morse.cw_timing("J"),
            self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("K"),
            self.dash + self.gap + self.dot + self.gap + self.dash + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("L"),
            self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("M"), self.dash + self.gap + self.dash + self.endword
        )
        self.assertEqual(
            self.morse.cw_timing("N"), self.dash + self.gap + self.dot + self.endword
        )
        self.assertEqual(
            self.morse.cw_timing("O"),
            self.dash + self.gap + self.dash + self.gap + self.dash + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("P"),
            self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("Q"),
            self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("R"),
            self.dot + self.gap + self.dash + self.gap + self.dot + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("S"),
            self.dot + self.gap + self.dot + self.gap + self.dot + self.endword,
        )
        self.assertEqual(self.morse.cw_timing("T"), self.dash + self.endword)
        self.assertEqual(
            self.morse.cw_timing("U"),
            self.dot + self.gap + self.dot + self.gap + self.dash + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("V"),
            self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("W"),
            self.dot + self.gap + self.dash + self.gap + self.dash + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("X"),
            self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("Y"),
            self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("Z"),
            self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("0"),
            self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("1"),
            self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("2"),
            self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("3"),
            self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("4"),
            self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dash
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("5"),
            self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("6"),
            self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("7"),
            self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("8"),
            self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.gap
            + self.dot
            + self.endword,
        )
        self.assertEqual(
            self.morse.cw_timing("9"),
            self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dash
            + self.gap
            + self.dot
            + self.endword,
        )

    def test_encode_paris(self):
        self.assertEqual(self.morse.cw_timing("paris"), ".g-g-g.e.g-e.g-g.e.g.e.g.g._")
        paris_timing = self.morse.cw_timing("paris")
        self.assertEqual(paris_timing.count(self.gap), 9, "Gap count")
        self.assertEqual(paris_timing.count(self.dot), 10, "Dot count")
        self.assertEqual(paris_timing.count(self.dash), 4, "Dash count")
        self.assertEqual(paris_timing.count(self.endletter), 4, "EndLetter count")
        self.assertEqual(paris_timing.count(self.endword), 1, "EndWord count")
        # dot + gap are both 1
        # gap is 9
        # dot is 10
        # dash is 4
        # endletter is 3
        # endwords is 7
        # 9+10+12+12+7=50

    def test_len_chr(self):
        self.assertEqual(self.morse.len_chr("p"), 8)
        self.assertEqual(self.morse.len_chr("a"), 4)
        self.assertEqual(self.morse.len_chr("r"), 5)
        self.assertEqual(self.morse.len_chr("i"), 2)
        self.assertEqual(self.morse.len_chr("s"), 3)

    def test_len_dits(self):
        self.assertEqual(self.morse.length_in_dits(self.morse.cw_timing("paris")), 50)
