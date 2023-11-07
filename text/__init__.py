""" from https://github.com/keithito/tacotron """
import re
from text.symbols import symbols

_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = {i: s for i, s in enumerate(symbols)}


def text_to_sequence(text):
    return [_symbol_to_id.get(char,_symbol_to_id[" "]) for char in text]

def sequence_to_text(sequence):
    return [_id_to_symbol.get(symbol," ") for symbol in sequence]
    # result = ""
    # for symbol_id in sequence:
    #     if symbol_id in _id_to_symbol:
    #         s = _id_to_symbol[symbol_id]
    #         # Enclose ARPAbet back in curly braces:
    #         if len(s) > 1 and s[0] == "@":
    #             s = "{%s}" % s[1:]
    #         result += s
    # return result.replace("}{", " ")