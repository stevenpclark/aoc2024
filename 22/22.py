from itertools import product

def encode(arr):
    #expect arr to be a list of nums in range [-9,9]
    return ''.join([chr(x+ord('m')) for x in arr])


class Buyer:
    def __init__(self, secret):
        self.secret = secret
        self.prices = [secret%10]
        self.deltas = list()

    def mix(self, val):
        self.secret = self.secret ^ val

    def prune(self):
        self.secret = self.secret % 16777216

    def step(self):
        self.mix(self.secret*64)
        self.prune()

        self.mix(self.secret//32)
        self.prune()

        self.mix(self.secret*2048)
        self.prune()

        self.prices.append(self.secret%10)
        self.deltas.append(self.prices[-1]-self.prices[-2])

    def encode(self):
        self.pattern = encode(self.deltas)

    def get_price(self, seq_pat):
        i = self.pattern.find(seq_pat)
        if i >= 0:
            return self.prices[i+4]
        else:
            return 0


def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    buyers = [Buyer(int(li)) for li in lines]

    for b in buyers:
        for i in range(2000):
            b.step()
        b.encode()


    if not part2:
        total = sum([b.secret for b in buyers])
        return total
    else:
        peak = 0
        for arr in product(range(-9,10), repeat=4):
            seq_pat = encode(arr)
            total = sum(b.get_price(seq_pat) for b in buyers)
            if total > peak:
                peak = total
                print(arr, peak)
        return peak




    
if __name__ == '__main__':
    assert solve('test.txt') == 37327623
    print(solve('input.txt'))
    assert solve('test2.txt', part2=True) == 23
    print(solve('input.txt', part2=True))
