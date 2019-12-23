import sys

if __name__ == "__main__":
    real_output = sys.stdin.read()

    assert int(sys.argv[1]) != 0    # exit code
    assert 'correct_line_when_missing_bracket.md' in real_output
    assert 'missing_bracket' in real_output
    assert 'line 2' in real_output
