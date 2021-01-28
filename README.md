# Withdrawal Tool
### A tool made for gathering DSC 40B specific email lists automatically

## Examples
To run,
```
python run.py
```

This command generates two separate `csv` files:
1. `slip_days_{x}` includes the number of slip days each student has used.
2. `missing_{x}` includes the number of consecutive assignments not turned in by the student.

where `{x}` is 2 if 2 homeworks have been graded so far.

You can also specify custom file paths to the gradebook.
```
python run.py --path ./gradebook.csv
```

You can also add `--email` to only get the emails of the students who have not submitted at least one assignment or have used at least one slip day. I will be trying to eventually make this send emails automatically.
```
python run.py --email
```

## TODO:
- ~Automatically detect how many assignments are graded.~
- ~Implement an `argparse` API.~
- Set up an email server to work with the script.
- Add more structure to the codebase.
- Source Gradebook automatically every week.
