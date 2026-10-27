# EE103 | Week 5 | 27 October 2026

Solutions for **EE103 Introduction to Programming** at Izmir Institute of Technology, following the 4-page Week 5 handout.

## Task-to-file guide

| Handout task | Python file | Topic |
|---|---|---|
| Recap: Multiply-all-1/2 and sanity check | `multiply-all.py` | `for`, `while`, inclusive ranges and result comparison |
| Recap: Guess & Check | `cupcake-guess-check.py` | Three nested loops |
| Recap Part 2: Binary integers | `binary-integers.py` | Divide by two, collect remainders |
| Recap Part 3: Floating error | `floating-error.py` | Summation of 0.1 ten times |
| Recap Part 4: Binary fractions | `binary-fractions.py` | Integer and fractional binary representation |
| Recap Part 5: Binary 0.1 | `binary-01.py` | Approximate representation with error below 0.00001 |
| Tasks Part 1: Approximate square root | `approximate-square-root.py` | Guess increments, tolerance, debugging, overshoot guard |
| Tasks Part 2: Bisection pages | `bisection-pages.py` | Binary search on pages 1 through 148 |
| Test suite | `test_week5.py` | Automated correctness checks |
| Turkish explanations | `ACIKLAMALAR_TR.md` | Step-by-step worked explanations |
| Example outputs | `SAMPLE_OUTPUTS.txt` | Checked examples and edge cases |

## Running the programs

Python 3 is required. There are no third-party dependencies.

Open a terminal in the `Week5` directory and run one script at a time:

```bash
python multiply-all.py
python cupcake-guess-check.py
python binary-integers.py
python floating-error.py
python binary-fractions.py
python binary-01.py
python approximate-square-root.py
python bisection-pages.py
```

On macOS/Linux, you may need to use `python3` instead of `python`.

To run all tests:

```bash
python -m unittest test_week5.py -v
```

## Results

- Multiplying 10, 11, 12, 13 gives **17160** for both loops.
- Cupcakes: **David 5, Emma 8, Frank 15**.
- Decimal **13** converts to binary **1101**.
- Adding 0.1 ten times produces `0.9999999999999999` in Python's usual floating-point representation.
- Decimal **13.375** converts to binary **1101.011**.
- **0.1** is approximated by `0.0001100110011001`, error **9.1552734375e-06** (below 0.00001).
- The fixed-step square-root program succeeds for 36, 24, 2 and 12345 with `increment=0.0001`, but can **overshoot** for 54321. The guard prevents an endless loop; trying `increment=0.00001` improves the accuracy.
- For secret page **148**, the bisection guesses are 74, 111, 130, 139, 144, 146, 147, 148 (8 guesses). Any page from 1 to 148 can be found in at most **8 guesses** with truthful hints.

### Precision caveat in Tasks Part 1

The task's step 6 checks `abs(guess**2 - number) < epsilon`, the **squared-value residual**. This differs from the introductory sentence's root error `abs(guess - sqrt(number))`. The supplied script follows the explicit loop condition in step 6. Enable `DEBUG = True` to print every 1000th estimate. The `guess**2 <= number` condition prevents continued iteration after overshooting.

## GitHub assignment submission

This folder is intended to be committed into the existing public `EE103` repository under `main`. Verify all files appear in GitHub before sharing:

`https://github.com/mahmutdmr/EE103/tree/main/Week5`

The course submission field requires the **GitHub folder link**, not a local file path. The original handout PDF is included in the companion downloadable ZIP, but is not required to execute any of the repository code.
