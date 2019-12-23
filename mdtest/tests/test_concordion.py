import markdownparser
import codegenerator


def test_ConcordionExample_SplitingNamesaces():
    splittingNames_md_concordionExample = '''
# Splitting Names

To help personalise our mailshots we want to have the first name and last name of the customer. 
Unfortunately the customer data that we are supplied only contains full names.

The system therefore attempts to break a supplied full name into its constituents by splitting around whitespace.

### [Example](- "basic")

The full name [Jane Smith](- "#name") is [broken](- "#result = split(#name)") into first name [Jane](- "?=#result.firstName") and last name [Smith](- "?=#result.lastName").
'''
    tests = markdownparser.parseMarkdownForConcordionTests(
        splittingNames_md_concordionExample)
    tests_function_code = codegenerator.parseTest2code(tests[0]).get_code()

    expected_code = '''
from fixture_basic import *

def test_Example(self):
    name = """Jane Smith"""
    result = split(name)
    self.assertEqual( """Jane""", result.firstName)
    self.assertEqual( """Smith""", result.lastName)
'''.lstrip()

    assert expected_code == tests_function_code
