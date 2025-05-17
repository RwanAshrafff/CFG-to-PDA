import sys
import itertools
from collections import defaultdict, deque
from graphviz import Digraph
from grammar import read_grammar
from pda import build_pda, print_delta, draw, accepts

if __name__ == "__main__":
    print("Paste your CFG (blank line to end):")
    txt = []
    while True:
        try: line = input()
        except EOFError: break
        if not line.strip(): break
        txt.append(line)
    try:
        start, terms, prods = read_grammar('\n'.join(txt))
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

    delta = build_pda(start, terms, prods)
    print_delta(delta)
    print("\nRendering PDA to pda_graph.png …")
    draw(delta)

    while True:
        try: s = input("\nTest string (blank = quit): ")
        except (EOFError, KeyboardInterrupt): break
        if s == "": break
        print("✔ accepted" if accepts(delta, s) else "✘ rejected")
