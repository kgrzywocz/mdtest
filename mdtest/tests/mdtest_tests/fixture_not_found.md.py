import sys

if __name__ == "__main__":
    real_output = sys.stdin.read()

    assert int(sys.argv[1]) != 0    # exit code
    assert 'fixture_not_found.md' in real_output
    assert 'Testcase_with_no_existing_fixture' in real_output
    assert 'not_existing_fixture' in real_output
