import sys

if __name__ == "__main__":
    real_output = sys.stdin.read()

    assert int(sys.argv[1]) != 0    # exit code
    assert 'fixture_with_problem.py' in real_output
    assert 'Problem_in_fixture' in real_output
    assert 'line 9' in real_output
