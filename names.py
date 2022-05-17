from converter import rType, iType, jType


insCodes = {
    "add": ("000000", "100000"),  ## R types
    "addu": ("000000", "100001"),
    "sub": ("000000", "100010"),
    "subu": ("000000", "100011"),
    "sll": ("000000", "000000"),
    "srl": ("000000", "000010"),
    "mult": ("000000", "011000"),
    "multu": ("000000", "011001"),
    "div": ("000000", "011010"),
    "divu": ("000000", "011011"),
    "mfhi": ("000000", "010000"),
    "mflo": ("000000", "010010"),
    "jr": ("000000", "001000"),
    "and": ("000000", "100100"),
    "or": ("000000", "100101"),
    "xor": ("00000", "100110"),
    "nor": ("000000", "100111"),
    "slt": ("000000", "101010"),
    "sltu": ("000000", "101011"),
    "addi": ("001000", "000000"),  ## I types
    "lw": ("100010", "000000"),
    "beq": ("000100", "000000"),
    "bne": ("000101", "000000"),
    "sw": ("101011", "000000"),
    "j": ("000010", "000000"),  ## J types
    "jal": ("000011", "000000"),
}


instructionHandler = {
    "add": rType,
    "addu": rType,
    "sub": rType,
    "subu": rType,
    "sll": rType,
    "srl": rType,
    "mult": rType,
    "multu": rType,
    "div": rType,
    "divu": rType,
    "mfhi": rType,
    "mflo": rType,
    "jr": rType,
    "and": rType,
    "and": rType,
    "or": rType,
    "xor": rType,
    "nor": rType,
    "slt": rType,
    "sltu": rType,
    "addi": iType,
    "lw": iType,
    "beq": iType,
    "bne": iType,
    "sw": iType,
    "j": jType,
    "jal": jType,
}

registersNames = {
    'zero': 0,   'at': 1,   'v0': 2,   'v1': 3,
    'a0': 4,   'a1': 5,   'a2': 6,   'a3': 7,
    't0': 8,   't1': 9,   't2': 10,  't3': 11,
    't4': 12,  't5': 13,  't6': 14,  't7': 15,
    's0': 16,  's1': 17,  's2': 18,  's3': 19,
    's4': 20,  's5': 21,  's6': 22,  's7': 23,
    't8': 24,  't9': 25,  'k0': 26,  'k1': 27,
    'gp': 28,  'sp': 29,  'fp': 30,  'ra': 31
}
