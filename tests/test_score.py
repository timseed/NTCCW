from unittest import TestCase
from unittest.mock import MagicMock, patch
from ham.cw.score import Score


class TestScore(TestCase):
    @patch("ham.cw.score.Score.__init__")
    def setUp(self, mock_parent_init) -> None:
        mock_parent_init.return_value = None
        self.score = Score("a", "b")

    def test_instance(self):
        self.assertIsInstance(self.score, Score)

    def test_same(self):
        self.score._setstr1('abc')
        self.score._setstr2('abc')
        self.assertEqual(self.score.get_score(), 0)

    def test_same_case_insensative(self):
        self.score._setstr1('abc')
        self.score._setstr2('ABC')
        self.assertEqual(self.score.get_score(), 0)

    def test_not_same(self):
        self.score._setstr1('abc')
        self.score._setstr2('A C')
        self.assertNotEqual(self.score.get_score(), 0)
        self.assertEqual(self.score.get_score(), 1)
