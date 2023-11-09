# cpu-simulator
## Introduction
This is a simulation of a very simple CPU that can be run through the terminal. It is meant to illustrate the relationships and functions of the CPU, ALU, cache and memory systems. The program is able to read MIPS instructions

## Program Structure
The CPU functions by reading instructions from a text file using a method of the CPU class, specifically, .execute_file('filename'), which takes a single argument: the filename of a .txt file consisting of MIPS instructions, delimited by commas(,) and separated by new lines. The .txt file can have an arbitrary number of MIPS instructions formatted in this way. There is an example instruction file attached with the filename 'instructions.txt'.
Unlike a normal CPU, there is no binary used in this project. All data saved in registers, cache or memory is of list, dict, int or str type. Instructions are read in MIPS and translated into the appropriate data type for processing and storage.

## List of valid MIPS Instructions
Due to the limited nature of this simulation, not all MIPS32 instructions are programmed. The following is a list of all instructions in the program, their arguments and a short description:
Rs -> Source Register
Rt -> Target Register
Rd -> Destination Register
Immd -> Immediate (Constant)
HI -> Special Register
LO -> Special Register

[Instruction] - [Argument(s)] - [Description]

### Arithmetic
ADD - Rd, Rs, Rt - Add the contents of Rs to the contents of Rt and store the result  at Rd.
ADDI - Rd, Rs, Immd - Add the contents of Rs to the immediate value and store the result at Rd.
SUB - Rd, Rs, Rt - Subtract the contents of Rt from the contents of Rs and store the result at Rd.
MUL - Rd, Rs, Rt - Multiply the contents of Rs and Rt and store the result at Rd.
DIV - Rs, Rt - Divide the contents of Rs by the contents of Rt and store the quotient at LO and the remainder at HI.

### Logical Operations


### HI/LO Register Access
MFHI - Rd - Move the contents of the HI register to the indicated destination register (Rd).
MFLO - Rd - Move the contents of the LO register to the indicated destination register (Rd).
MTHI - Rs - Move the contents of the source register (Rs) to the HI register.
MTLO - Rs - Move the contents of the source register (Rs) to the LO register.
