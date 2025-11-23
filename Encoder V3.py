# gknp_v2_encoder.py
import json
from datetime import datetime

# Paste full 1000-entry dict here as DICT_V2 = { ... }

def gknp_v2_encode(prompt: str):
    prompt_lower = prompt.lower().strip()
    packet = {
        "gk_version": "2.0",
        "ts": int(datetime.now().timestamp()),
        "codes": [],
        "args": []
    }
    
    remaining = prompt_lower
    while remaining:
        best_code = None
        best_phrase = ""
        for code, phrase in DICT_V2.items():
            p = phrase.lower()
            if remaining.startswith(p) and len(p) > len(best_phrase):
                best_code = code
                best_phrase = p
        
        if best_code:
            packet["codes"].append(best_code)
            remaining = remaining[len(best_phrase):].strip()
        else:
            # Fallback to pure Kaprekar if no match
            packet["fallback"] = kaprekar_fallback(remaining)
            break
    
    if remaining and "fallback" not in packet:
        packet["args"].append(prompt.split()[-1])  # last word as arg
    
    return packet
