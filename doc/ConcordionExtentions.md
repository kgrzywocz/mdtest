# Extra semantics and additional functionality

## [Code blocks are enumerated](- "basic")

In every test case each block will be enumerated. So

    some code

will be assigned to variable ```code1```. So ```code1``` is equal to [some code](?=#code1) and ```code2``` is equal to [code1](- "?=#code2") etc.

## [Assert statements](- "basic")

In order to make some verification easier - especially comparing code blocks to some desired output (e.g. from shell command or some http repose) ```==``` assertion was added with following syntax:

    #some_variable == #some_otherVariable

It asserts simple conditions like [2+2==4](- "2+2==4")

Also to make it easier to verify texts

    c:assert-contain=

was added. So when you have [some long string](- "#text") you can easy verify that word [string](- "c:assert-contain=#text") is in it. I found it very useful on verifying some outputs of commands etc.

## [Python syntax](- "basic")

Let me be clear: **YOU SHOULD NOT** overuse this feature. Logic should be done in ``DSL Script`` (Domain Specific Language Script) or in ``fixture``. You can read more about it [here](https://concordion.org/technique/java/markdown/#evolve-a-domain-specific-language).

This feature kind of side effect, so **IT WILL CHANGE IN THE FUTURE**, but I think some features can be useful.

As you can see in previous example some python syntax might be use. In general commands produces code interpreted by python, so python syntax should be valid. Be aware that ```markdown-python``` has some limitation especially in escaping special characters. Also some syntax is catch for some purpose running Concordion testcases.

### What is working for sure?

- basic arithmetics like calculations resulting in [6](- "?=str(2+2*2)")
- string concatenation, so [Alice](- "#name") has a [cat](- "#pet") should produce [Alice has a cat](- "?=#name+' has a '+#pet"). Notice: you ``markdown-python`` has some limitations in escaping " and '.

## [Variable #TEST_NAME](- "basic")

Variable ``#TEST_NAME`` is expanded to test name used in code - name without non-alphanumeric characters. In this case it will be [Variable_TEST_NAME](- "?=#TEST_NAME").
