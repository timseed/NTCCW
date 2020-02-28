from unittest import TestCase
from unittest.mock import patch
from ham.cw.ntcexam import GenText


class TestGenText(TestCase):
    def setUp(self) -> None:
        self.gt = GenText()

    def test_exists(self):
        self.assertIsInstance(self.gt, GenText)

    def test_ntc_test(self):
        self.assertEqual(1, 1)

    @patch("ham.cw.ntcexam.GenText.count_wav")
    def test_count(self, patched_count_wav):
        patched_count_wav.return_value = 3

        self.assertEqual(self.gt.count_wav(), 3)
