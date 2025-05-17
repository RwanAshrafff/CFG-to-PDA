from typing import List, Tuple, Dict


class PDATransition:
    def __init__(self, input_symbol: str, stack_top: str, next_state: str, stack_replace: List[str]):
        self.input_symbol = input_symbol  # '' for epsilon
        self.stack_top = stack_top
        self.next_state = next_state
        self.stack_replace = stack_replace  # can be []

    def __repr__(self):
        return f"δ({self.input_symbol}, {self.stack_top}) → ({self.next_state}, {''.join(self.stack_replace) or 'ε'})"


class PDA:
    def __init__(self):
        self.states = {"q"}
        self.input_alphabet = set()
        self.stack_alphabet = set()
        self.transitions: Dict[Tuple[str, str, str], List[Tuple[str, List[str]]]] = {}
        self.start_state = "q"
        self.start_stack_symbol = "Z"
        self.accept_states = {"q"}

    def add_transition(self, state: str, input_symbol: str, stack_top: str, next_state: str, stack_replace: List[str]):
        key = (state, input_symbol, stack_top)
        if key not in self.transitions:
            self.transitions[key] = []
        self.transitions[key].append((next_state, stack_replace))
        self.stack_alphabet.add(stack_top)
        self.stack_alphabet.update(stack_replace)

    def __repr__(self):
        rep = []
        for key, vals in self.transitions.items():
            for (next_state, stack_replace) in vals:
                rep.append(
                    f"δ({key[0]}, {key[1] or 'ε'}, {key[2]}) → ({next_state}, {''.join(stack_replace) or 'ε'})"
                )
        return "\n".join(rep)
