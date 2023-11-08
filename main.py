# TODO: make the CPU class, cache class, study inheritance, main memory class, ALUs, write the binary reference file

class CPU:
    def __init__(self, name = 'CPU'):
        self.name = name
        self.cache = None
        self.memory = None
        self.ALU = None
        self.registers = {'R{}'.format(i): None for i in range(32)}
        self.registers['R0'] = 0
        self.HI = None
        self.LO = None

    def get_cache(self):
        return self.cache

    def add_cache(self, cache):
        if self.cache != None:
            print('Unable to add a cache, cache already exists')
            return
        print(f'{cache.name} added as a cache to {self.name}')
        self.cache = cache
        if self.memory is not None:
            self.cache.main_memory = self.memory

    def remove_cache(self):
        if self.cache == None:
            print('Unable to remove cache, no cache exists')
            return
        print(f'{self.cache.name} removed as cache from {self.name}')
        self.cache.remove_memory()
        self.cache = None

    def get_memory(self):
        return self.memory

    def add_memory(self, memory):
        if self.memory != None:
            print('Unable to add a main memory, main memory already exists')
            return
        print(f'{memory.name} added as main memory to {self.name}')
        self.memory = memory
        if self.cache is not None:
            self.cache.add_memory(memory)

    def remove_memory(self):
        if self.memory == None:
            print('Unable to remove main memory, no main memory exists')
            return
        print(f'{self.memory.name} removed as main memory from {self.name}')
        self.cache.remove_memory()
        self.memory = None

    def add_ALU(self, ALU):
        if self.ALU != None:
            print('Unable to add ALU, ALU already exists')
            return
        print(f'{ALU.name} added as ALU to {self.name}')
        self.ALU = ALU

    def remove_ALU(self):
        if self.ALU == None:
            print('Unable to remove ALU, no ALU exists')
            return
        print(f'{self.ALU.name} removed as ALU from {self.name}')
        self.ALU = None

    def write_to_register(self, address, data):
        print(f' - Writing value: {data} to register: {address}')
        self.registers[address] = data

    def read_from_register(self, address):
        print(f' - Reading from register: {address}')
        return self.registers[address]

    def print_registers(self):
        print(f'Registers: {self.registers}\n HI: {self.HI}\n LO: {self.LO}')

    def MIPS_processor(self, instruction):
        split_instruction = instruction.split(',')
        si_len = len(split_instruction)
        opcode = split_instruction[0]
        if si_len == 1:
            return None
        if si_len == 2:
            rd = split_instruction[1]
            if opcode == 'MFHI':
                self.write_to_register(rd, self.HI)
            elif opcode == 'MFLO':
                self.write_to_register(rd, self.LO)
            elif opcode == 'MTHI':
                self.HI = self.read_from_register(rd)
            elif opcode == 'MTLO':
                self.LO = self.read_from_register(rd)
            elif opcode == 'HALT':
                print('--------Execution Complete--------')
        if si_len == 3:
            rd = split_instruction[1]
            rs = split_instruction[2]
            if opcode == 'DIV':
                self.LO, self.HI =  self.ALU.DIV(self.read_from_register(rd), self.read_from_register(rs))
            elif opcode == 'NOT':
                self.write_to_register(rd, self.ALU(self.read_from_register(rs)))
            elif opcode == 'MOVE':
                self.write_to_register(rd, self.read_from_register(rd))
            elif opcode == 'NEGU':
                self.write_to_register(rd, neg(self.read_from_register(rd)))
            elif opcode == 'SW':
                self.cache.write(rd, self.read_from_register(rs))
            elif opcode == 'LW':
                self.write_to_register(rd, self.cache.read(rs))
            elif opcode == 'LI':
                self.write_to_register(rd, int(rs))
        if si_len == 4:
            if opcode[-1] == 'I':
                rd = split_instruction[1]
                rs = int(self.read_from_register(split_instruction[2]))
                rt = int(split_instruction[3])
            else:
                rd = split_instruction[1]
                rs = int(self.read_from_register(split_instruction[2]))
                rt = int(self.read_from_register(split_instruction[3]))
            if opcode in ('ADD', 'ADDI'):
                print(f' - Adding values {rs} and {rt}')
                result = self.ALU.ADD(rs, rt)
            elif opcode == 'SUB':
                print(f' - Subtracting values {rt} from {rs}')
                result = self.ALU.SUB(rs, rt)
            elif opcode == 'MUL':
                print(f' - Multiplying values {rs} and {rt}')
                result = self.ALU.MUL(rs, rt)
            elif opcode in ('SLT', 'SLTI'):
                print(f' - Evaluating {rs} < {rt}')
                result = rs < rt
            elif opcode in ('AND', 'ANDI'):
                print(f' - Evaluating {rs} AND {rt}')
                result = self.ALU.AND(rs, rt)
            elif opcode in ('OR', 'ORI'):
                print(f' - Evaluating {rs} OR {rt}')
                result = self.ALU.OR(rs, rt)
            elif opcode in ('XOR', 'XORI'):
                print(f' - Evaluating {rs} XOR {rt}')
                result = self.ALU.XOR(rs, rt)
            self.write_to_register(rd, result)

class ALU:
    def __init__(self, name):
        self.name = name

    def NAND(self, val1, val2):
      if val1:
        if val2:
          return False
      return True

    def NOT(self, val1):
      if val1:
        return False
      return True

    def AND(self, val1, val2):
      if val1:
        if val2:
          return True
      return False

    def OR(self, val1, val2):
      if val1:
        return True
      if val2:
        return True
      return False

    def XOR(self, val1, val2):
      if self.AND(val1, val2):
        return False
      if val1:
        if self.NOT(val2):
          return True
      if val2:
        if self.NOT(val1):
          return True
      return False

    def ADD(self, val1, val2):
        return (val1 + val2)

    def SUB(self, val1, val2):
        return (val1 - val2)

    def MUL(self, val1, val2):
        return (val1 * val2)

    def DIV(self, val1, val2):
        return divmod(val1, val2)

class Memory:
    def __init__(self, name):
        self.name = None

    def read(self):
        print(f' - {self.name} read: ', end = '')

    def write(self):
        print(f' - {self.name} write: ', end = '')

class Cache(Memory):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.current_block = 0
        self.main_memory = None
        self.data = [
        {'tag': None, 'data': None},
        {'tag': None, 'data': None},
        {'tag': None, 'data': None},
        {'tag': None, 'data': None},
        {'tag': None, 'data': None},
        {'tag': None, 'data': None},
        {'tag': None, 'data': None},
        {'tag': None, 'data': None}
        ]

    def __repr__(self):
        return(f'Cache: {self.name}')

    def print(self):
        print(self.data)

    def increment_block(self):
        if self.current_block < 7:
            self.current_block += 1
        else:
            self.current_block = 0
        print(f'Current cache block is: {self.current_block + 1}')

    def add_memory(self, memory):
        self.main_memory = memory

    def remove_memory(self):
        self.main_memory = None

    def read(self, address):
        super().read()
        data = None
        for i in self.data:
            if i['tag'] == address:
                print('Cache Hit')
                data = i['data']
                return data
        print('Cache Miss')
        data = self.main_memory.read(address)
        self.data[self.current_block] = {'tag': address, 'data': data}
        self.increment_block()
        return data

    def write(self, address, data):
        super().write()
        for i in self.data:
            if i['tag'] == address:
                self.main_memory.write(i['data'], address)
                i['data'] = data
        self.data[self.current_block] = {'tag': address, 'data': data}
        self.increment_block()

    def flush(self):
        print(f'Flushing Cache: {self.name}')
        self.data = [
        {'tag': None, 'data': None},
        {'tag': None, 'data': None},
        {'tag': None, 'data': None},
        {'tag': None, 'data': None},
        {'tag': None, 'data': None},
        {'tag': None, 'data': None},
        {'tag': None, 'data': None},
        {'tag': None, 'data': None}
        ]

class MainMemory(Memory):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.data = [None for i in range(16)]

    def __repr__(self):
        return (f'Main Memory: {self.name}')

    def print(self):
        print(self.data)

    def read(self):
        super().read()
        return self.data[address]

    def write(self, address, data):
        super().write()
        self.data[address] = data

myCPU = CPU()
cache = Cache('Cache_1')
memory = MainMemory('MainMemory_1')
ALU = ALU('ALU_1')
myCPU.add_cache(cache)
myCPU.add_memory(memory)
myCPU.add_ALU(ALU)

myCPU.print_registers()
myCPU.MIPS_processor('LI,R1,4')
myCPU.MIPS_processor('LI,R2,2')
myCPU.MIPS_processor('ADDI,R3,R1,6')
myCPU.MIPS_processor('DIV,R3,R1')
myCPU.MIPS_processor('MFLO,R4')
myCPU.MIPS_processor('MFHI,R5')
myCPU.MIPS_processor('MUL,R6,R4,R5')
myCPU.MIPS_processor('HALT,;')
myCPU.print_registers()
