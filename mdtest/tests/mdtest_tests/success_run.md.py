import sys

if __name__ == "__main__":
    expected_output = 'Test success_run.py start\n'
    expected_output += 'shellRun\n\n'
    expected_output += 'Test success_run.py PASSED'
    real_output = sys.stdin.read()

    assert int(sys.argv[1]) == 0  # exit code
    assert expected_output in real_output
