# Withdrawal Tool
### A tool made for gathering DSC 40B specific email lists automatically

To run,
`python run.py`

This command generates two separate `csv` files:
1. `slip_days_{x}` includes the number of slip days each student has used.
2. `missing_{x}` includes the number of consecutive assignments not turned in by the student.

## TODO:
- Automatically detect how many assignments are graded.
- Implement an `argparse` API.

