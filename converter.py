

from typing import Dict, List
from pda import PDA


class CFGtoPDAConverter:
    def __init__(self, cfg: Dict[str, List[str]], start_symbol: str):
        self.cfg = cfg
        self.start_symbol = start_symbol

    def convert(self) -> PDA:
        pda = PDA()

        pda.start_stack_symbol = self.start_symbol

        for variable, productions in self.cfg.items():
            for production in productions:
                replacement = list(production)[::-1] if production else []
                pda.add_transition(
                    "q", "", variable, "q", replacement
                )  
        
        terminals = {c for prods in self.cfg.values() for p in prods for c in p if c.islower()}
        for terminal in terminals:
            pda.add_transition("q", terminal, terminal, "q", [])

        return pda
