import networkx as nx

def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    G = nx.Graph()

    for li in lines:
        c1, c2 = li.split('-')
        G.add_edges_from([(c1, c2)])

    if not part2:
        valid = set()
        for c1 in G.nodes():
            if c1[0] != 't':
                continue
            s1 = set(G.neighbors(c1))
            for c2 in s1:
                s2 = set(G.neighbors(c2))
                shared = s1.intersection(s2)
                for c3 in shared:
                    valid.add(tuple(sorted((c1, c2, c3))))
        return len(valid)
    else:
        longest = list()
        cliques = nx.find_cliques(G)
        for clique in cliques:
            if len(clique) > len(longest):
                longest = clique
        return ','.join(sorted(longest))
    
if __name__ == '__main__':
    assert solve('test.txt') == 7
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 'co,de,ka,ta'
    print(solve('input.txt', part2=True))
