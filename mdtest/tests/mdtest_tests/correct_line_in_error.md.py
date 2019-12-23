import sys

if __name__ == "__main__":
    real_output = sys.stdin.read()

    assert int(sys.argv[1]) != 0    # exit code
    assert 'correct_line_in_error.md' in real_output
    assert 'Testcase2' in real_output
    assert 'line 7' in real_output
    assert '''Some test [this is wrong](- "True==False")''' in real_output
