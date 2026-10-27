"""Run with: python -m unittest test_week5.py -v"""

import re
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run_script(filename, user_input=""):
    return subprocess.run(
        [sys.executable, str(HERE / filename)],
        input=user_input, text=True, capture_output=True, check=True, timeout=25
    ).stdout


class Week5Tests(unittest.TestCase):
    def test_multiplication_for_and_while(self):
        output = run_script("multiply-all.py", "10\n13\n")
        self.assertIn("For loop result: 17160", output)
        self.assertIn("While loop result: 17160", output)
        self.assertIn("results are same", output)

    def test_multiplication_range_with_zero(self):
        output = run_script("multiply-all.py", "-2\n2\n")
        self.assertIn("For loop result: 0", output)
        self.assertIn("results are same", output)

    def test_cupcake_puzzle(self):
        output = run_script("cupcake-guess-check.py")
        for expected in ("David packed 5", "Emma packed 8", "Frank packed 15"):
            self.assertIn(expected, output)

    def test_binary_integers(self):
        for value, binary in (("13", "1101"), ("0", "0"), ("-13", "-1101")):
            with self.subTest(value=value):
                output = run_script("binary-integers.py", value + "\n")
                self.assertIn(f"is {binary}", output)

    def test_floating_error(self):
        output = run_script("floating-error.py")
        self.assertIn("0.9999999999999999", output)
        self.assertIn("False", output)

    def test_binary_fractions(self):
        output = run_script("binary-fractions.py", "13.375\n")
        self.assertIn("1101.011", output)

    def test_binary_one_tenth(self):
        output = run_script("binary-01.py")
        self.assertIn("Within tolerance? True", output)
        self.assertIn("Number of fractional binary digits: 16", output)
        error = float(re.search(r"Absolute error:\s*(\S+)", output).group(1))
        self.assertLess(error, 1e-5)

    def test_square_root_converges(self):
        for value in ("36", "24", "2", "12345"):
            with self.subTest(value=value):
                output = run_script("approximate-square-root.py", value + "\n")
                self.assertIn("Success: approximation is within epsilon.", output)
                error = float(re.search(r"Absolute squared error:\s*(\S+)", output).group(1))
                self.assertLess(error, 0.01)

    def test_square_root_overshoot_guard(self):
        output = run_script("approximate-square-root.py", "54321\n")
        self.assertIn("Tolerance not reached", output)
        self.assertIn("Try reducing increment", output)

    def test_square_root_negative_input(self):
        output = run_script("approximate-square-root.py", "-9\n")
        self.assertIn("not a real number", output)

    def test_bisection_page_148_in_eight_guesses(self):
        output = run_script("bisection-pages.py", "higher\n" * 7 + "correct\n")
        self.assertIn("Found your favorite page: 148", output)
        self.assertIn("Number of guesses: 8", output)


if __name__ == "__main__":
    unittest.main()
