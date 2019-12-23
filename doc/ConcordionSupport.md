# Concordion support

This file discus support for Concordion 2 Markdown syntax.

## What is supported?

- Commands in Markdown links
- Multiple tests in file aka example command
- assert-equals command
- set command
- ``#TEXT`` variable

More details about:

- [instrumenting](https://concordion.org/instrumenting/java/markdown/)
- original Concordion [markdown syntax](https://concordion.github.io/concordion/latest/spec/specificationType/markdown/Markdown.html) and [grammar](https://concordion.github.io/concordion/latest/spec/specificationType/markdown/MarkdownGrammar.html).

## What is different?

- In [example command handling](https://concordion.github.io/concordion/latest/spec/common/command/example/Example.html)
  - Markdown link title is used for fixture name
  - Test name mangling can be different

## What is missing?

- Tabels support
  - execute command on a table
  - run each row as an example
  - execute command on a list
  - verify-rows command
- In [example command handling](https://concordion.github.io/concordion/latest/spec/specificationType/markdown/MarkdownExampleCommand.html)
  - ``before``
  - ``after``
  - [ExampleListener](https://concordion.github.io/concordion/latest/spec/common/extension/listener/ExampleListener.html)
- Assertion and other commands out of example section will not work
- [run command](https://concordion.github.io/concordion/latest/spec/specificationType/markdown/MarkdownExecuteCommand.html)
- HTML Support
  - markdown html generation with results
  - echo command
  - Embedding HTML && HTML entities with commnads
- operator ``?`` in [expresions](https://concordion.github.io/concordion/latest/spec/common/command/expressions/Expressions.html)
- [ComplexExpressions](https://concordion.github.io/concordion/latest/spec/common/command/expressions/ComplexExpressions.html) - It is not supported now, although it may work now due to some Python Syntax support - see [ConcordionExtentions.md](ConcordionExtentions.md)
