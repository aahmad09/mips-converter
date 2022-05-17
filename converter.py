from typing import List
import names


## function to handle rType instructions
def rType(instList: str) -> str:
    # by default shamt is 000000
    bin_shamt = "00000"
    operation = instList[0]
    # gets op code and function code from the dictionary
    binOpCode = names.insCodes[operation][0]
    bin_funct = names.insCodes[operation][1]

    # zfill is an inbuilt function that pads the string with zeros until it is n characters long
    if operation in ["sll", "srl"]:
        # converts rd, rt, and shamt to thier binary equivalent and pads the string so each is 5 characters long
        bin_rd = convertDecToBin(instList[1]).zfill(5)
        bin_rt = convertDecToBin(instList[2]).zfill(5)
        bin_rs = "00000"
        bin_shamt = convertDecToBin(instList[3]).zfill(5)
    elif operation in ["mult", "div", "multu", "divu"]:
        bin_rd = "00000"
        bin_rs = convertDecToBin(instList[1]).zfill(5)
        bin_rt = convertDecToBin(instList[2]).zfill(5)
    elif operation == "jr":
        bin_rs = convertDecToBin(instList[1]).zfill(5)
        bin_rd = "00000"
        bin_rt = "00000"
    elif operation in ["mfhi", "mflo"]:
        bin_rd = convertDecToBin(instList[1]).zfill(5)
        bin_rs = "00000"
        bin_rt = "00000"
    else:  ## operation in ["add", "addu", "sub", "subu", "and"]
        bin_rd = convertDecToBin(instList[1]).zfill(5)
        bin_rs = convertDecToBin(instList[2]).zfill(5)
        bin_rt = convertDecToBin(instList[3]).zfill(5)

    # returns the string concat of all the fields
    return binOpCode + bin_rs + bin_rt + bin_rd + bin_shamt + bin_funct


## function to handle iType instructions
def iType(instList: str) -> str:
    operation = instList[0]
    binOpCode = names.insCodes[operation][0]

    if operation in ["beq", "bne"]:
        bin_rs = convertDecToBin(instList[1]).zfill(5)
        bin_rt = convertDecToBin(instList[2]).zfill(5)
        bin_imm = convertDecToBin(instList[3]).zfill(16)
    elif operation in ["lw", "sw"]:
        # special cases for handling lw and sw instructions which are in format sw $rt, imm($rs)
        splittedIns = instList[2].split("(")
        bin_imm = convertDecToBin(splittedIns[0]).zfill(16)
        bin_rs = convertDecToBin(splittedIns[1][:-1]).zfill(5)
        bin_rt = convertDecToBin(instList[1]).zfill(5)
    else:
        bin_rt = convertDecToBin(instList[1]).zfill(5)
        bin_rs = convertDecToBin(instList[2]).zfill(5)

    return binOpCode + bin_rs + bin_rt + bin_imm


## function to handle jType instructions
def jType(instList: str) -> str:
    operation = instList[0]
    address = instList[1]
    binOpCode = names.insCodes[operation][0].zfill(6)
    binAddress = convertDecToBin(address).zfill(26)
    return binOpCode + binAddress


# a simple function that converts decimal to binary equivalent using python in built functions
def convertDecToBin(dec: str) -> str:
    return str(bin(int(dec))[2:])


def convertToRegName(operands: List[str]) -> List[str]:
    if operands[0] in ["lw", "sw"]:
        splittedIns = operands[-1].split("(")
        reg = str(names.registersNames[splittedIns[-1][:-1]])
        lastOperand = splittedIns[0] + "(" + reg + ")"
        return (
            [operands[0]]
            + list(map(lambda x: names.registersNames[x], operands[1:-1]))
            + [lastOperand]
        )
    elif operands[0] in ["beq", "bne", "sll", "srl"]:
        return (
            [operands[0]]
            + list(map(lambda x: names.registersNames[x], operands[1:-1]))
            + [operands[-1]]
        )
    else:
        return [operands[0]] + list(
            map(lambda x: names.registersNames[x], operands[1:])
        )


# a function that determines what type of instruction it is
def convertMipsToBin(mipsInst: str, regFlags: bool) -> str:
    # splits on space character to get all operands/symbols
    seperatedInst = mipsInst.split()
    # if using register names then this conditional converts it to register numbers
    if regFlags:
        seperatedInst = convertToRegName(seperatedInst)

    # uses a dictionary to decide what type of instruction it is and passes it to the appropriate function
    converted = names.instructionHandler[seperatedInst[0]](seperatedInst)
    return converted


def main():
    ###
    # Uses a while loop to get mips instruction and converts to bin equivalent until the user enters "exit"
    ##
    f = open("guide.txt", "r")
    help_contents = f.read()
    print(help_contents)

    # a boolean to indicate whether to use reg names or reg numbers
    regNamesFlag = (
        True
        if input(
            "Do you want to use register names or register numbers? Enter 'y' for register names, 'n' for register numbers: "
        ).lower()
        == "y"
        else False
    )

    print("-" * 120)
    mipsInst = (
        input("Enter binary MIPS instruction to be converted: ")
        .lower()
        .replace(",", "")
        .replace("$", "")
    )

    try:
        while mipsInst != "exit":
            if mipsInst == "help":
                f = open("help.txt", "r")
                help_contents = f.read()
                print(help_contents)
            print(
                f"\tConverted instruction in binary:  {convertMipsToBin(mipsInst, regNamesFlag)}"
            )
            print("-" * 120)
            mipsInst = (
                input("Enter binary MIPS instruction to be converted: ")
                .lower()
                .replace(",", "")
                .replace("$", "")
            )
    except:
        print("ERROR: Invalid instruction format or instruction not supported.")


if __name__ == "__main__":
    main()
