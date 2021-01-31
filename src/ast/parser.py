from . import _gen


class Parser(_gen.CLSParser):

    def __init__(self):

        super().__init__(whitespace=" \t\n",
                         nameguard=None,
                         comments_re=r"\(\*.*?\*\)",
                         eol_comments_re=r"\\\\.*?",
                         ignorecase=False,
                         left_recursion=False,
                         parseinfo=False, # TODO: change to True
                         keywords=None,
                         namechars='')

    def parse(self, txt):

        return super().parse(txt, rule_name="start")
