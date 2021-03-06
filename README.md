# Markdown Test (mdtest)

Framework for verifying/testing documentation in markdown format. It can be used to do Behavior Test Driven Development (BTDD).  This document is also a living example of self verified documentation (some kind of SSOT - single source of truth). Syntax is inspired by [Concordion](https://concordion.org) and it's [syntax](https://concordion.org/instrumenting/java/markdown/). Implementation based on [python-markdown](https://python-markdown.github.io/).

**NOTICE:** Project is still in very early stage of development!!! It might be unstable and a lot of things will probably change (At least output and traceability)

## [How to run](- "cli")

Just install python package. Then in the project root run:

    mdtest

It will search for ```README.md``` and markdown files(ending on ```.md```) in ```doc/``` for a valid test (or "example" in Concordion language). For this project it will [Ran 12 tests](- "c:assert-contain=run_shell(#code1 +' --skip='+ #TEST_NAME)") + this test (it is skipped here to avoid recursion).

For more details about command options see [doc/CLI.md](doc/CLI.md).

## Concordion Syntax

You can easily start by looking at [doc/BasicConcordionExample.md](doc/BasicConcordionExample.md). It is a ```mdtest``` instrumented version of [Concordion Getting Started](https://concordion.org/tutorial/java/markdown/), which I recommend you to follow ;).

```mdtest``` aims to use the same syntax as [Concordion](https://concordion.org/) - it just provides different fixture implementation - python is a bit be more 'lightweight'.

Basic instrumentation syntax relays on commands, which are special markdown links:

    # [Test case](- "basic")

    Normal text and [text which might be verified](- "with some command")

This defines "Test Case" that runs "with some command" command (see "Commands examples" section for details).

**Notice:** commands links are always "-".

**Notice2:** This test case uses buildin fixture ```fixture_basic.py```. More details in section "Fixtures".

### [Commands examples](- "basic")

- assign text to variable ```[text will be value](- "#some_variable")``` [text will be value](- "#some_variable")
- assert variable value ```[text will be value](- "?=#some_variable")``` [text will be value](- "?=#some_variable")
- run some command from fixture```[text](- "?=get_first_word(#some_variable)")``` [text](- "?=get_first_word(#some_variable)")

More details which syntax is supported can be found in [doc/ConcordionSupport.md](doc/ConcordionSupport.md)

## Fixtures

Test cases definition contains annotation which fixture to be used:

    # [Test case](- "python_functions")

This makes mdtest look for a given fixture (in this case ```fixture_pythonfunctions.py```) in any path contains markdown files and builtin fixtures (like ```basic``` or ```cli```). Fixtures are just a python files, which may contain some useful function for instrumenting documentation. For details and examples see buildin [fixtures](mdtest/fixture) or just see ```fixture_*.py``` in this documentation doc file.

## [Changes to Concordion Syntax](- "basic")

Some additions to original syntax includes:

- Each ```block``` is assigned to variable ```codeX``` where X is sequence number in testcase, so [block is value of code1](- "'block'==code1"). This is useful for verifying some bigger blocks.
- "==" provides assert useful with blocks. See example above.
- Limited python syntax support

Example and more details can be found in [doc/ConcordionExtentions.md](doc/ConcordionExtentions.md)

## Other notices and practice hits

- To see how your files are rendered against different engines you can use [babelmark](https://babelmark.github.io/)
- Some useful practices can be found on [keepSpecsSimple](https://concordion.org/technique/java/markdown/#keepSpecsSimple) by Concordion

As a rule of thumb I would use this project for some high level verification(on integrating whole product only) and to keep the documentation/specification up to date. More use cases should be implemented as integration and unit tests. I will try to keep this project as an example, but I am only human and some mistakes are unavoidable - If you know how to make things better - let me know ;)
