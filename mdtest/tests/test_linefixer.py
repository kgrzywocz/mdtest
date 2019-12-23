from linefixer import *
from mdtest.structures import MdTest, CompiledMdTest, CommandCode


class TestScanner:

    def test_find_occurrence(self):
        source = """a
        b
        c"""
        scanner = SourceScaner(source)

        assert scanner.get_next_lineno_matching('c') == 3

    def test_find_next_occurrence(self):
        source = """a
        b
        b
        c"""
        scanner = SourceScaner(source)

        assert scanner.get_next_lineno_matching('b') == 2
        assert scanner.get_next_lineno_matching('b') == 3

    def test_find_next_occurrence_in_same_line(self):
        source = """a
        b
        bb
        b
        c"""
        scanner = SourceScaner(source)

        assert scanner.get_next_lineno_matching('b') == 2
        assert scanner.get_next_lineno_matching('b') == 3
        assert scanner.get_next_lineno_matching('b') == 3
        assert scanner.get_next_lineno_matching('b') == 4


class TestAnnotateSourceLineno:

    def test_empty(self):
        annotate_source_lineno([], "")

    def test_single_test(self):
        test = MdTest("name", "fixture")

        annotate_source_lineno([test], """# [name](- "fixture")""")

        assert test.get_lineno() == 1

    def test_two_tests(self):
        test1 = MdTest("name", "fixture")
        test2 = MdTest("name2", "fixture")

        annotate_source_lineno([test1, test2],
                               """# [name](- "fixture")

        # [name2](- "fixture")
        """)

        assert test1.get_lineno() == 1
        assert test2.get_lineno() == 3

    def test_escape_name_in_test(self):
        test = MdTest("longer name", "longer fixture")

        annotate_source_lineno(
            [test], """# [longer name](- "longer fixture")""")

        assert test.get_lineno() == 1

    def test_single_command(self):
        test1 = MdTest("name", "fixture")
        command1 = CommandCode("text", "code")
        test1.add_command(command1)

        annotate_source_lineno([test1], """
        # [name](- "fixture")

        some text [text](- "code")
        """)

        assert test1.get_lineno() == 2
        assert command1.get_lineno() == 4

    def test_command_with_regex_inside(self):
        test1 = MdTest("name", "fixture")
        command1 = CommandCode("text", "?=#code")
        test1.add_command(command1)

        annotate_source_lineno([test1], """
        # [name](- "fixture")

        some text [text](- "?=#code")
        """)

        assert test1.get_lineno() == 2
        assert command1.get_lineno() == 4

    def test_command_with_html_inside_text(self):
        test1 = MdTest("name", "fixture")
        command1 = CommandCode("text", "code")
        test1.add_command(command1)

        annotate_source_lineno([test1], """
        # [name](- "fixture")

        some text [*text*](- "code")
        """)

        assert test1.get_lineno() == 2
        assert command1.get_lineno() == 4
