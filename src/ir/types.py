from __future__ import annotations # Needed for typehint inside class (e.g: Name); will be default in python 3.10
from typing import List, Dict
import re
from util.error import CompilerError

class Name():

    def __init__(self, names : List[str]):

        self.names = names
    
    @staticmethod
    def from_str(names : str) -> Name:

        if re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z0-9_]+)*", names) is None:
            raise CompilerError("TODO")

        return Name(names.split("."))

    def __len__(self):
        return len(self.names)

    def __getitem__(self, key):
        return self.names.__getitem__(key)

    def __setitem__(self, key, value):
        return self.names.__setitem__(key, value)

    def __delitem__(self, key):
        return self.__delitem__(key)

    def __eq__(self, other):
        return self.names == other


class Node():

    def __init__(self,
                 root : Node,
                 name : str,
                 fullname : Name,
                 idx : int,
                 includes : Dict[str, Node] = None,
                 stms : List[Stm] = None,
                 fields : List[Field] = None):

        self.root = root

        self.name = name
        self.fullname = fullname
        self.idx = idx

        self.includes = includes

        self.elems = []
        
        self.stms = stms
        self.fields = fields

    def search(self, name : Name) -> Node:

        if len(name) < 1:
            return None

        if name[0] != self.name:
            return None

        if len(name) == 1:
            return self

        for elem in self.elems:
            if r := elem.search(name[1:]):
                return r

        return None

    def search_local(self, name : Name) -> Node:
        # Same as search but also search includes for first node

        if res := self.search(name):
            return res

        if len(name) < 1:
            return None

        if node := includes[name[0]]:

            return node.search(name[1:])
        

    def insert(self, name : Name, node : Node):

        if len(name) < 1:
            raise CompilerError("Unable to insert node with empty name")

        if len(name) > 1:

            pass

        elif len(name) == 1:

            pass

        else:
            assert false



class Stm():

    def __init__(self):
        pass

class Field():

    def __init__(self):
        pass




