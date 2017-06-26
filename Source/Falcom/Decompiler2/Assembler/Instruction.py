from Common import *
from .InstructionTable import *
from .Function import *
from enum import IntFlag

class Label:
    def __init__(self, label: str, offset: int):
        self.label = label          # label name
        self.offset = offset        # label offset in instruction

class Operand:
    def __init__(self):
        self.operand    = None      # type: int
        self.size       = None      # type: int

class Flags(IntFlag):
    EndBlock            = 1 << 0
    StartBlock          = 1 << 1
    Call                = (1 << 2) | StartBlock
    Jump                = (1 << 3) | EndBlock

    FormatArgNewLine    = 1 << 4

    @property
    def isEndBlock(self):
        return bool(self.value & self.EndBlock)

    @property
    def isStartBlock(self):
        return bool(self.value & self.StartBlock)

    @property
    def isCall(self):
        return bool(self.value & self.Call & ~self.StartBlock)

    @property
    def isJump(self):
        return bool(self.value & self.Jump & ~self.EndBlock)

    @property
    def isArgNewLine(self):
        return bool(self.value & self.FormatArgNewLine)


class Instruction:
    def __init__(self):
        self.op         = None      # type: int
        self.operands   = []        # type: List[Operand]
        self.branches   = []        # type: List[CodeBlock]
        self.descriptor = None
        self.label      = None
        self.flags      = None      # type: Flags