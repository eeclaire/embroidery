from unittest import TestCase

from embroidery import pdf_reader as under_test


class PdfReader(TestCase):

    def test_is_thread_row__given_id_is_int__returns_true(self):
        row = {"id": 1}
        self.assertTrue(under_test.is_thread_row(row))

    def test_is_thread_row__given_id_is_int_str__returns_true(self):
        row = {"id": "1"}
        self.assertTrue(under_test.is_thread_row(row))

    def test_is_thread_row__given_id_non_num_str__returns_false(self):
        row = {"id": "rando"}
        self.assertFalse(under_test.is_thread_row(row))

    def test_is_thread_row__given_invalid_id__returns_False(self):
        invalid_ids = [1.1, "1.1", True]
        for id_value in invalid_ids:
            self.assertFalse(under_test.is_thread_row({"id": id_value}))

    def test_is_thread_row__given_invalid_row_count__returns_False(self):
        row = {
            "id": "1",
            "count": "garbage"
        }
        self.assertFalse(under_test.is_thread_row(row))

    def test_is_thread_row__given_row_count_is_x1__returns_False(self):
        row = {
            "id": "1",
            "count": "x 1"
        }
        self.assertTrue(under_test.is_thread_row(row))
