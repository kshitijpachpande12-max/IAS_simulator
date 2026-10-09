# IAS Machine Simulator & Assembler

A Python implementation of an **IAS computer simulator and assembler** that translates assembly instructions into binary machine code and simulates their execution.

The project demonstrates fundamental concepts of computer architecture, including instruction encoding, memory organization, registers, and instruction execution.

## Overview

The project consists of two main components:

* **Assembler:** Reads assembly instructions from `assembly.txt`, converts supported instructions into binary representations, and writes the output to `binary.text`.
* **IAS Simulator:** Reads the generated binary program and simulates instruction execution while displaying the state of the machine's registers.

The simulator models the IAS computer's 40-bit memory words, which can hold two 20-bit instructions.

## Features

* Converts assembly instructions into binary machine code.
* Supports instruction encoding using 8-bit opcodes and 12-bit memory addresses.
* Represents memory words using 40-bit binary strings.
* Simulates instruction execution using IAS registers.
* Implements left- and right-half instruction execution.
* Supports arithmetic, memory access, jump, and control instructions.
* Displays register states during execution for debugging and tracing.

## Supported Instructions

The following instructions are included in the assembler's opcode mapping:

| Instruction | Opcode     | Description                                                                       |
| ----------- | ---------- | --------------------------------------------------------------------------------- |
| `LOAD`      | `11111111` | Loads a value from memory into the accumulator.                                   |
| `STOR`      | `00100001` | Stores the accumulator's value in memory.                                         |
| `ADD`       | `00000101` | Adds a memory value to the accumulator.                                           |
| `SUB`       | `00000110` | Subtracts a memory value from the accumulator.                                    |
| `JUMP_L`    | `00001101` | Jumps to the left instruction of a memory word.                                   |
| `JUMP_R`    | `00001110` | Jumps to the right instruction of a memory word.                                  |
| `JUMP+_L`   | `00001111` | Conditionally jumps to the left instruction when the accumulator is nonnegative.  |
| `JUMP+_R`   | `00010000` | Conditionally jumps to the right instruction when the accumulator is nonnegative. |
| `HALT`      | `00000000` | Stops execution.                                                                  |
| `NOP`       | `00000001` | Performs no operation.                                                            |

*Note: The instruction names and opcode mappings reflect this implementation. They should not be assumed to match every standard IAS instruction encoding.*

## IAS Machine Registers

The simulator maintains the following registers and state variables:

| Register | Purpose                                                                        |
| -------- | ------------------------------------------------------------------------------ |
| `PC`     | Program Counter: tracks the current memory word.                               |
| `IBR`    | Instruction Buffer Register: holds the right-hand instruction when applicable. |
| `IR`     | Instruction Register: holds the opcode of the instruction being executed.      |
| `MAR`    | Memory Address Register: holds the memory address used by an instruction.      |
| `MBR`    | Memory Buffer Register: holds data or instructions read from memory.           |
| `AC`     | Accumulator: stores arithmetic results and values loaded from memory.          |

## Project Structure

```text
IAS-Machine-Simulator/
├── assembler.py       # Converts assembly into binary machine code
├── simulator.py       # Simulates IAS instruction execution
├── assembly.txt       # Input assembly program
├── binary.text        # Generated binary representation
└── README.md           # Project documentation
```

The filenames in this structure are illustrative; adjust them to match the actual filenames in your repository.

## Requirements

* Python 3
* No external Python packages are required by the code shown.

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd IAS-Machine-Simulator
```

Replace `<your-repository-url>` with your GitHub repository's URL.

### 2. Prepare an assembly program

Write your assembly program in `assembly.txt`, following the instruction and operand formats expected by the assembler.

### 3. Assemble the program

Run the assembler:

```bash
python assembler.py
```

The assembler generates the binary representation in `binary.text`.

### 4. Execute the program

Run the simulator:

```bash
python simulator.py
```

The simulator executes the binary program and prints the machine's register state during execution.

**Important:** The assembler and simulator must use the same input and output filenames. Ensure that the generated binary file is valid before running the simulator.

## Concepts Demonstrated

This project explores several foundational computer science concepts:

* Computer architecture and the IAS stored-program model.
* Binary number representation and instruction encoding.
* Assembly language and machine code.
* Fetch-decode-execute cycles.
* Register-based computation.
* Memory addressing and instruction storage.
* Control flow and conditional branching.
* Simulation of hardware behavior using Python.

## Future Improvements

Potential improvements include:

* Adding input validation and clearer error messages.
* Refactoring repeated assembler logic into reusable functions.
* Supporting labels and symbolic addresses in assembly programs.
* Implementing signed-number representation and arithmetic.
* Adding automated tests for instructions and execution behavior.
* Providing an optional execution trace and clearer output formatting.
* Improving the assembler's handling of invalid instructions and operands.

## Author

**Kshitij Pachpande**

A computer science project exploring computer architecture and instruction-level simulation using Python.
