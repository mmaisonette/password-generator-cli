import io
import unittest
from unittest.mock import patch

from app import build_alphabet, password_generator


class TestPasswordGenerator(unittest.TestCase):
    def test_returns_error_message_when_length_is_not_numeric(self):
        with patch("builtins.input", return_value="abc"):
            result = password_generator()

        self.assertEqual(
            result,
            "\nYou must submit the number of characters you want using numbers!",
        )

    def test_returns_none_and_prints_message_when_length_is_out_of_range(self):
        for invalid_length in ("10", "50"):
            with self.subTest(length=invalid_length):
                with (
                    patch("builtins.input", return_value=invalid_length),
                    patch("sys.stdout", new_callable=io.StringIO) as fake_stdout,
                ):
                    result = password_generator()

                self.assertIsNone(result)
                self.assertIn(
                    "Length must be between 20 and 40!", fake_stdout.getvalue()
                )

    def test_generates_password_with_requested_length(self):
        with patch("builtins.input", side_effect=["20", "n"]):
            password = password_generator()

        self.assertIsNotNone(password)
        self.assertEqual(len(password), 20)

    def test_generates_password_without_ambiguous_characters_when_requested(self):
        ambiguous = set("O0oIl1|")
        with patch("builtins.input", side_effect=["30", "y"]):
            password = password_generator()

        self.assertIsNotNone(password)
        self.assertTrue(all(ch not in ambiguous for ch in password))


class TestBuildAlphabet(unittest.TestCase):
    def test_build_alphabet_removes_ambiguous_characters(self):
        alphabet = build_alphabet(avoid_ambiguous=True)

        for ch in "O0oIl1|":
            self.assertNotIn(ch, alphabet)
