import unittest
from API_Pro_Max_beta_v07.input_parser.input_parser import InputParser

class TestInputParser(unittest.TestCase):
    def setUp(self):
        self.parser = InputParser()

    def test_parse_invalid_input(self):
        with self.assertRaises(ValueError):
            self.parser.parse("")  # Тестуємо на пустий рядок
            self.parser.parse("invalid_format/")  # Тестуємо на неправильний формат
            self.parser.parse("posts/abc")  # Тестуємо на недійсне ID (не число)

    def test_parse_valid_input(self):
        result = self.parser.parse("posts/1")
        self.assertEqual(result, ("posts", "1"))

        result = self.parser.parse("comments")
        self.assertEqual(result, "comments")

if __name__ == "__main__":
    unittest.main()
