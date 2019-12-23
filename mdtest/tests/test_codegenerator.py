from structures import MdTest, CommandCode, CommandBlock
from codegenerator import *


class TestCodeGenerator():

    def test_parseTest(self):
        test = MdTest("Example", "basic", 25)
        test.add_commands([
            CommandCode("Jane Smith", "#name"),
            CommandCode("broken", "#result = split(#name)"),
            CommandCode("Jane", "?=#result.firstName"),
            CommandCode("Smith", "?=#result.lastName"),
        ])
        expected_code = '''
from fixture_basic import *

def test_Example(self):
    name = """Jane Smith"""
    result = split(name)
    self.assertEqual( """Jane""", result.firstName)
    self.assertEqual( """Smith""", result.lastName)
'''.lstrip()

        compiled_test = parseTest2code(test)

        assert expected_code == compiled_test.get_code()
        assert compiled_test.get_code2source_map() == [
            0, 25, 25, 25, 0, 0, 0, 0]

    def test_parseTestWithoutCommands(self):
        test = MdTest("Empty", "basic")

        expected_code = '''
from fixture_basic import *

def test_Empty(self):
    pass
'''.lstrip()

        compiled_test = parseTest2code(test)

        assert expected_code == compiled_test.get_code()

    def test_multipleCodeBlocks(self):
        test = test = MdTest("MultipleCodeBlocks", "basic")
        test.add_commands([
            CommandBlock("First some code"),
            CommandBlock("Second some code"),
        ])

        expected_code = '''
from fixture_basic import *

def test_MultipleCodeBlocks(self):
    code1 = """First some code"""
    code2 = """Second some code"""
'''.lstrip()

        compiled_test = parseTest2code(test)

        assert expected_code == compiled_test.get_code()

    def test_codeBlocksShouldbeGeneratedFirst(self):
        test = test = MdTest("CodeBlocksShouldbeGeneratedFirst", "basic")
        test.add_commands([
            CommandBlock("First some code"),
            CommandCode("Action", "#code1==#code2"),
            CommandBlock("Second some code"),
        ])

        expected_code = '''
from fixture_basic import *

def test_CodeBlocksShouldbeGeneratedFirst(self):
    code1 = """First some code"""
    code2 = """Second some code"""
    self.assertEqual( code1,code2 )
'''.lstrip()

        compiled_test = parseTest2code(test)

        assert expected_code == compiled_test.get_code()

    def test_substitution_TEST_NAME_variable(self):
        test = test = MdTest("substitution_TEST_NAME", "basic")
        test.add_commands([
            CommandCode("command", 'log_name(#TEST_NAME)'),
        ])

        expected_code = '''
from fixture_basic import *

def test_substitution_TEST_NAME(self):
    log_name("""substitution_TEST_NAME""")
'''.lstrip()

        compiled_test = parseTest2code(test)

        assert expected_code == compiled_test.get_code()


def assert_command_produces_line(command, expected_line):
    assert CommandParser().parse_command(command) == expected_line


class TestCommandParser():

    def test_generateAsign(self):
        assert_command_produces_line(
            CommandCode("Jane Smith", "#name"),
            expected_line='''name = """Jane Smith"""''')

    def test_generateFunCall(self):
        assert_command_produces_line(
            CommandCode("something", "fun_call()"),
            expected_line='''fun_call()''')

    def test_generateAssert(self):
        assert_command_produces_line(
            CommandCode("Jane", "?=#result.firstName"),
            expected_line='''self.assertEqual( """Jane""", result.firstName)''')

    def test_codeBlock_generateVariable(self):
        assert_command_produces_line(
            command=CommandBlock("Some code"),
            expected_line='''code1 = """Some code"""''')

    def test_generateAssertExtension(self):
        assert_command_produces_line(
            CommandCode("Action", "#code1 == #code2"),
            expected_line='''self.assertEqual( code1 , code2 )''')

    def test_generateAssertExtensionWithFunctionCall(self):
        assert_command_produces_line(
            CommandCode('Shows', 'runCli(#code1)==#code2'),
            expected_line='''self.assertEqual( runCli(code1),code2 )''')

    def test_concordion_instrumenting_assertequals_command(self):
        assert_command_produces_line(
            CommandCode('Hello World!', '?=getGreeting()'),
            expected_line='''self.assertEqual( """Hello World!""", getGreeting())''')

    def test_concordion_instrumenting_assertequals_command_PropertiesSupport(self):
        assert_command_produces_line(
            CommandCode('Hello World!', '?=greeting'),
            expected_line='''self.assertEqual( """Hello World!""", greeting)''')

    def test_concordion_instrumenting_assertequals_command_function_call_with_multiple_args(self):
        assert_command_produces_line(
            CommandCode('3', "?=add(#x, #y)"),
            expected_line='''self.assertEqual( """3""", add(x, y))''')

    def test_concordion_instrumenting_assertequals_command_explicit_commnad(self):
        assert_command_produces_line(
            CommandCode('Yo',
                        'c:assert-equals=greet(#firstName, #lastName)'),
            expected_line='''self.assertEqual( """Yo""", greet(firstName, lastName))''')

    def test_extention_assertcontain_explicit(self):
        assert_command_produces_line(
            CommandCode('Yo',
                        'c:assert-contain=greet(#firstName, #lastName)'),
            expected_line='''self.assertIn( """Yo""", greet(firstName, lastName))''')

    def test_concordion_instrumenting_set_command_explicit_commnad(self):
        assert_command_produces_line(
            CommandCode('Bob', 'c:set=#firstName'),
            expected_line='''firstName = """Bob"""''')

    def test_explicit_command_explicit_may_end_with_space(self):
        assert_command_produces_line(
            CommandCode('Bob', 'c:set #firstName'),
            expected_line='''firstName = """Bob"""''')

    def test_concordion_instrumenting_asserttrue(self):
        assert_command_produces_line(
            CommandCode('today', 'c:assert-true=isCompletionToday()'),
            expected_line='''self.assertTrue( isCompletionToday() )''')

    def test_concordion_instrumenting_assertfalse(self):
        assert_command_produces_line(
            CommandCode('today', 'c:assert-false=isCompletionToday()'),
            expected_line='''self.assertFalse( isCompletionToday() )''')

    def test_concordion_instrumenting_TEXT_variable(self):
        assert_command_produces_line(
            CommandCode('09:00AM', 'setCurrentTime(#TEXT)'),
            expected_line='''setCurrentTime("""09:00AM""")''')

    def test_concordion_instrumenting_execute_explicit(self):
        assert_command_produces_line(
            CommandCode('09:00AM', 'c:execute=setCurrentTime()'),
            expected_line='''setCurrentTime()''')
