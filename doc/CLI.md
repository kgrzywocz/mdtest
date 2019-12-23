# Command Line Interface

## [Help](- "cli")

    mdtest --help

[Shows](- "run_shell(#code1)==#code2") available commands:

    Markdown Test (mdtest)

    Runs tests embedded in markdown similar to way as pytest does.

    Usage:
      mdtest [--skip=TEST_NAME]...
      mdtest TEST_SUITE... [--skip=TEST_NAME]...
      mdtest (-h | --help)

    Options:
      -h --help                   Show this screen.
      --skip=TEST_NAME            Skips test with given name.

## [Run specified/single test suite](- "cli")

Instead of discovering tests you can specify test suites to run. So:

    mdtest doc/BasicConcordionExample.md

will [Ran 1 test](- "c:assert-contain=run_shell(#code1)") from suite [BasicConcordionExample.md](BasicConcordionExample.md) in this case.

## [Skip](- "cli")

You can skip the execution of some test(s):

    mdtest doc/BasicConcordionExample.md --skip=Example

Will [Ran 0 tests](- "c:assert-contain=run_shell(#code1)").
