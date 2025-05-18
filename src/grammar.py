from collections import defaultdict


def read_grammar(text: str):
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if len(lines) < 3:
        raise ValueError(
            "Need start symbol, terminals, and at least one rule.")
    start = lines[0]
    terms = set(lines[1].split(','))
    prods = defaultdict(list)
    for ln in lines[2:]:
        ln = ln.replace('→', '->')
        Head, Values = map(str.strip, ln.split('->'))
        for value in Values.split('|'):
            value = value.strip()
            if value in {'', 'ε'}:
                prods[Head].append([])
            else:
                prods[Head].append(value.split())
    return start, terms, prods
