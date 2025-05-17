from typing import Dict, List

def parse_cfg_from_dict(cfg_dict: Dict[str, List[str]], start_symbol: str) -> Dict[str, List[str]]:
    """
    Validates and returns a CFG in internal format.
    """
    if start_symbol not in cfg_dict:
        raise ValueError("Start symbol must be in the CFG")
    for head, productions in cfg_dict.items():
        for prod in productions:
            if not isinstance(prod, str):
                raise ValueError(f"Invalid production: {prod} in {head}")
    return cfg_dict
