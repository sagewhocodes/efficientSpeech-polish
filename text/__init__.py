""" from https://github.com/keithito/tacotron """
import re
from text.symbols import symbols

_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = {i: s for i, s in enumerate(symbols)}


def text_to_sequence(text):
    return [_symbol_to_id.get(char,_symbol_to_id[" "]) for char in text]

def sequence_to_text(sequence):
    return [_id_to_symbol.get(symbol," ") for symbol in sequence]