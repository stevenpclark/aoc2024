class Computer:
    def __init__(self, lines):
        self.a = int(lines[0].split()[-1])
        self.b = int(lines[1].split()[-1])
        self.c = int(lines[2].split()[-1])

        ops_str = lines[4].split()[-1]
        self.ops = [int(c) for c in ops_str.split(',')]
        assert len(self.ops)%2 == 0

    def get_combo(self, x):
        assert 0 <= x <= 6
        if x == 4:
            return self.a
        elif x == 5:
            return self.b
        elif x == 6:
            return self.c
        else:
            return x

    def get_output(self):
        test_a = 1
        while True:
            self.a = test_a
            output = list()

            i = 0
            while i < len(self.ops):
                op = self.ops[i]
                operand = self.ops[i+1]
                if op == 0: #adv (division)
                    self.a = int(self.a / 2**self.get_combo(operand))
                elif op == 1: #bxl (bitwise XOR)
                    self.b = self.b ^ operand
                elif op == 2: #bst (combo modulo 8)
                    self.b = self.get_combo(operand) % 8
                elif op == 3: #jnz (jump)
                    if self.a != 0:
                        i = operand - 2
                elif op == 4: #bxc (bitwise XOR of B and C)
                    self.b = self.b ^ self.c
                elif op == 5: #out
                    out = self.get_combo(operand) % 8
                    if self.ops[len(output)] != out:
                        if len(output) > 10:
                            print(len(output), test_a)
                        break #failed to replicate
                    output.append(out)
                elif op == 6: #bdv
                    self.b = int(self.a / 2**self.get_combo(operand))
                elif op == 7: #cdv
                    self.c = int(self.a / 2**self.get_combo(operand))
                else:
                    print('AAAAA!')
                i += 2

            if output == self.ops:
                print(test_a)
                return test_a
            #if test_a % 10000 == 0:
                #print(test_a)
            test_a += 1



        output_str = ','.join([str(x) for x in output])
        print(output_str)
        return output_str


def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    comp = Computer(lines)

    return comp.get_output()

if __name__ == '__main__':
    #assert solve('test.txt') == '4,6,3,5,6,3,5,2,1,0'
    #print(solve('input.txt'))
    assert solve('test2.txt', part2=True) == 117440
    print(solve('input.txt', part2=True))
