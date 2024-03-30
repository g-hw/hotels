from django.test import TestCase

from hotels_service.core import helpers


class TestHelpers(TestCase):

    def test_get_longest_length(self):
        self.assertEqual(helpers.get_longest_length(["abc", "abcd", "abcde"]), "abcde")

    def test_get_first_value(self):
        self.assertEqual(helpers.get_first_value([None, "a"]), "a")

    def test_compare_list(self):
        self.assertEqual(helpers.compare_list(["a", " b"], ["b"]), ["b"])

    def test_Remove_duplicates_in_list(self):
        self.assertEqual(helpers.remove_duplicates_in_list(["a", "a", "b"]), ["a", "b"])
