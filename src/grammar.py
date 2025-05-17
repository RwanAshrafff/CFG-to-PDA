from collections import defaultdict

def read_grammar(text: str):
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if len(lines) < 3:
        raise ValueError("Need start symbol, terminals, and at least one rule.")
    start = lines[0]
    terms = set(lines[1].split(','))
    prods = defaultdict(list)
    for ln in lines[2:]:
        ln = ln.replace('→', '->')
        h, rhs = map(str.strip, ln.split('->'))
        for alt in rhs.split('|'):
            alt = alt.strip()
            if alt in {'', 'ε', 'λ'}:
                prods[h].append([])
            else:
                prods[h].append(alt.split())
    return start, terms, prods