import itertools
from collections import defaultdict, deque
from graphviz import Digraph

EPS = 'ε'
BOT = '$'
Q1, Q2, Q3, QF = 'q1', 'q2', 'q3', 'qf'


def build_pda(start, terms, prods):
    d = defaultdict(lambda: defaultdict(set))
    def push(q, a, pop, qn, strg): return d[q][(a, pop)].add((qn, strg))
    push(Q1, EPS, EPS, Q2, BOT)
    push(Q2, EPS, EPS, Q3, start)
    for A, values in prods.items():
        for value in values:
            if not value:
                push(Q3, EPS, A, Q3, '')
            else:
                rev = value[::-1]
                last, rest = rev[0], rev[1:]
                h_curr = Q3
                h_id = itertools.count(start=4)
                h_next = f'q{next(h_id)}'
                push(h_curr, EPS, A, h_next, last)
                for sym in rest:
                    h_curr, h_next = h_next, f'q{next(h_id)}'
                    push(h_curr, EPS, EPS, h_next, sym)
                push(h_next, EPS, EPS, Q3, '')
    for a in terms:
        push(Q3, a, a, Q3, '')
    push(Q3, EPS, BOT, QF, '')
    return d


def print_delta(delta):
    print('\nδ transition table')
    print(f"{'from':<5} {'in':<2} {'pop':<3} → {'to':<5} {'push'}")
    print('-'*30)
    for q in delta:
        for (a, pop), tgts in delta[q].items():
            for qn, push in tgts:
                a = a or EPS
                pop = pop or EPS
                push = push or EPS
                print(f'{q:<5} {a:<2} {pop:<3} → {qn:<5} {push}')


def draw(delta, fname='pda_graph'):
    dot = Digraph('PDA', format='png')
    dot.attr(rankdir='LR', nodesep='0.9', ranksep='0.7',
            splines='polyline', fontname='Helvetica', fontsize='12')
    dot.attr('node', shape='circle', style='filled',
            fillcolor='#ffffff', color='#8e8e8e', width='0.8')
    mapping = {Q1: '1', Q2: '2', Q3: '3', QF: '4'}
    helper_counter = itertools.count(start=5)
    visible = {Q1, Q2, Q3, QF}
    for q in delta:
        for (a, pop), tgts in delta[q].items():
            for qn, _ in tgts:
                if qn not in mapping:
                    mapping[qn] = str(next(helper_counter))
                    visible.add(qn)

    dot.node(mapping[Q1], _attributes={'root': 'true'})
    for q in visible:
        shape = 'doublecircle' if q == QF else 'circle'
        dot.node(mapping[q], label=mapping[q], shape=shape)
    
    def lbl(a, pop, push):
        return f'{a or EPS}, {pop or EPS} → {push or EPS}'
    for q in delta:
        for (a, pop), tgts in delta[q].items():
            for qn, push in tgts:
                tail, head = mapping[q], mapping[qn]
                attrs = {}
                if q == qn and a == pop and push == '' and a in 'abcdefghijklmnopqrstuvwxyz':
                    attrs = dict(tailport='s', headport='w', loop='left')
                dot.edge(tail, head, label=lbl(a, pop, push), **attrs)
    dot.render(fname, view=True)
