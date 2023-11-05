# TODO: make the CPU class, cache class, study inheritance, main memory class, ALUs, write the binary reference file

class CPU:
    def __init__(self, name = 'CPU'):
        self.name = name
        self.cache = None
        self.memory = None
        self.ALU = None

    def get_cache(self):
        return cache

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
        return cache

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
        print(f'{ALU.name} added as main memory to {self.name}')
        self.ALU = ALU

    def remove_ALU(self):
        if self.ALU == None:
            print('Unable to remove ALU, no ALU exists')
            return
        print(f'{self.ALU.name} removed as ALU from {self.name}')
        self.ALU = None

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

    def add(self, val1, val2):
        return val1 + val2

    def subtract(self, val1, val2):
        return val1 - val2

    def multiply(self, val1, val2):
        return val1 * val2

    def divide(self, val1, val2):
        return val1 % val2

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

    def write(self, data, address):
        super().write()
        for i in self.data:
            if i['tag'] == address:
                self.main_memory.write(i['data'], address)
                i['data'] = data
        self.data[self.current_block] = {'tag': address, 'data': data}
        self.increment_block()

class MainMemory(Memory):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.data = ['' for i in range(32)]

    def __repr__(self):
        return (f'Main Memory: {self.name}')

    def print(self):
        print(self.data)

    def read(self):
        super().read()
        return self.data[address]

    def write(self, data, address):
        super().write()
        self.data[address] = data

myCPU = CPU()
cache = Cache('Cache_1')
memory = MainMemory('MainMemory_1')
ALU = ALU('ALU_1')
myCPU.add_cache(cache)
myCPU.add_memory(memory)
myCPU.add_ALU(ALU)

cache.write('apple', 0)
cache.write('orange', 1)
cache.write('berry', 4)

cache.read(0)
cache.write('mango', 0)

myCPU.cache.print()
myCPU.memory.print()
