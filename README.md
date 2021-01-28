# Withdrawal Tool
### A tool made for gathering DSC 40B specific email lists automatically

## Examples
To run,
```
python run.py --count 2
```

Here `--count` is a mandatory argument for now to specify how many homeworks
have been graded so far. This is to not confuse the script with homeworks
that have been submitted but not graded so it becomes difficult to tell if the student submitted the homework or not. I am trying to get the code to infer this automatically in a future build.

This command generates two separate `csv` files:
1. `slip_days_{x}` includes the number of slip days each student has used.
2. `missing_{x}` includes the number of consecutive assignments not turned in by the student.
where {x} is 2 in this example.

You can also specify custom file paths to the gradebook.
```
python run.py --path ./gradebook.csv --count 2
```

You can also add `--email` to only get the emails of the students who have not submitted at least one assignment or have used at least one slip day. I will be trying to eventually make this send emails automatically.
```
python run.py --count 2 --email
```

## TODO:
- Automatically detect how many assignments are graded.
- ~Implement an `argparse` API.~
- Set up an email server to work with the script.
- Add more structure to the codebase

