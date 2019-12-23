from mdtest.structures import MdTest, CommandCode, CommandBlock
import markdownparser

splittingNames_md_concordionExample = '''
# Splitting Names

To help personalise our mailshots we want to have the first name and last name of the customer.
Unfortunately the customer data that we are supplied only contains full names.

The system therefore attempts to break a supplied full name into its constituents by splitting around whitespace.

### [Example](- "basic")

The full name [Jane Smith](- "#name") is [broken](- "#result = split(#name)") into first name [Jane](- "?=#result.firstName") and last name [Smith](- "?=#result.lastName").
'''
expected_code_splittingNames_md_concordionExample = MdTest("Example", "basic")
expected_code_splittingNames_md_concordionExample.add_commands([
    CommandCode("Jane Smith", "#name"),
    CommandCode("broken", "#result = split(#name)"),
    CommandCode("Jane", "?=#result.firstName"),
    CommandCode("Smith", "?=#result.lastName"),
])


def assert_code_produces(text, expected_tests):
    tests = markdownparser.parseMarkdownForConcordionTests(
        text)
    assert tests == expected_tests


def assert_commands_in_basic_tests(text, commands):
    expected_test = MdTest("Basic", "basic")
    expected_test.add_commands(commands)

    assert_code_produces(text, [expected_test])


def test_ConcordionExample_SplitingNamesaces():
    assert_code_produces(splittingNames_md_concordionExample,
                         expected_tests=[
                             expected_code_splittingNames_md_concordionExample
                         ])


def test_multiple_tests():
    assert_code_produces(splittingNames_md_concordionExample
                         + splittingNames_md_concordionExample,
                         expected_tests=[
                             expected_code_splittingNames_md_concordionExample,
                             expected_code_splittingNames_md_concordionExample
                         ])


def test_should_escape_non_alfacharacters_names():
    expected_test = MdTest("Example_2", "basic_2")
    expected_test.add_command(CommandCode("Jane Smith", "#name"))

    assert_code_produces(
        text='''
# [Example 2](- "basic 2")
[Jane Smith](- "#name")).
''',
        expected_tests=[expected_test]
    )


def test_empty_test():
    assert_code_produces('''### [Empty](- "basic")''',
                         expected_tests=[MdTest("Empty", "basic")])


def test_fixtures_without_hyphen_willbe_ignored():
    assert_code_produces('''### [Empty]("basic")''',
                         expected_tests=[]
                         )


def test_commands_without_hyphen_willbe_ignored():
    assert_code_produces(
        text='''
# [Not all urls are commands](- "basic")
[Jane Smith]("#name")).
''',
        expected_tests=[MdTest("Not_all_urls_are_commands", "basic")]
    )


def test_codeblocks():
    expected_test = MdTest("Blocks", "basic")
    expected_test.add_command(CommandBlock("Some code"))

    assert_code_produces(
        text='''
# [Blocks](- "basic")
```
Some code
```
''',
        expected_tests=[expected_test]
    )


def test_concordion_example_should_end_when_another_starts():
    assert_code_produces(
        text='''
### [Blocks](- "basic")

### [Blocks2](- "basic")
''',
        expected_tests=[
            MdTest("Blocks", "basic"),
            MdTest("Blocks2", "basic")
        ]
    )


def test_concordion_example_should_end_when_higher_level_header_starts():
    assert_code_produces(
        text='''
### [Blocks](- "basic")

## Blocks2
[Should be ignored](- "#name")).
''',
        expected_tests=[
            MdTest("Blocks", "basic")
        ]
    )


def test_concordion_example_should_continue_when_same_level_header_starts():
    expected_test = MdTest("Blocks", "basic")
    expected_test.add_command(CommandCode("command", "#name"))

    assert_code_produces(
        text='''
### [Blocks](- "basic")

### Blocks2
[command](- "#name")).
''',
        expected_tests=[expected_test]
    )


def test_concordion_example_should_continue_when_lower_level_header_starts():
    expected_test = MdTest("Blocks", "basic")
    expected_test.add_command(CommandCode("command", "#name"))

    assert_code_produces(
        text='''
### [Blocks](- "basic")

#### Blocks2
[command](- "#name")).
''',
        expected_tests=[
            expected_test
        ]
    )


def test_hanging_command_shouldbe_ignored():
    assert_code_produces(
        text='''
# Something
[value](- "command")
''',
        expected_tests=[]
    )


def test_concordion_instrumeting_overview():
    assert_commands_in_basic_tests(
        text='''
# [Basic](- "basic")
[value](- "command")
''',
        commands=[CommandCode("value", "command")]
    )


def test_concordion_instrumeting_overview_reference_link():
    assert_commands_in_basic_tests(
        text='''
# [Basic](- "basic")
[value][id]

[id]: - "command"
''',
        commands=[CommandCode("value", "command")]
    )


def test_concordion_instrumeting_overview_reference_link_by_text():
    assert_commands_in_basic_tests(
        text='''
# [Basic](- "basic")
[value][]

[value]: - "command"
''',
        commands=[CommandCode("value", "command")]
    )


def test_instrumeting_overview_link_with_inner_formating_escapes_it():
    assert_commands_in_basic_tests(
        text='''
# [Basic](- "basic")
[*em*](- "sth(#TEXT)")
''',
        commands=[CommandCode("em", "sth(#TEXT)")]
    )


def test_instrumeting_overview_link_with_inner_code():
    assert_commands_in_basic_tests(
        text='''
# [Basic](- "basic")
[```code```](- "sth(#TEXT)")
''',
        commands=[CommandCode("code", "sth(#TEXT)"), CommandBlock("code")]
    )


def test_concordion_example_implementation_status_should_skip_test():
    assert_code_produces(
        text='''
# [Blocks](- "basic c:status=ExpectedToFail")
[command](- "#name")).
''',
        expected_tests=[]
    )


def test_next_test_with_implementation_status_should_end_case():
    expected_test = MdTest("Blocks", "basic")
    expected_test.add_command(CommandCode("command", "#name"))

    assert_code_produces(
        text='''
# [Blocks](- "basic")
[command](- "#name")).

# [Blocks](- "basic c:status=ExpectedToFail")
[command2](- "#name")).
''',
        expected_tests=[expected_test]
    )
