# _pad = "_"
# _punctuation = "!'(),.:;? "
# _special = "-/"
# _letters = 'abbʲcdʐdʑd̪d̪z̪ffʲijj̃klmmʲn̪ppʲrrʲs̪tɕtʂtʲt̪t̪s̪uvvʲwxz̪çŋɔɔ̃ɕɛɛ̃ɟɡɨɲʂʎʐʑʔ'
# _silences = ["@sp", "@spn", "@sil"]

# # Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
# _arpabet = ["@" + s for s in cmudict.valid_symbols]
# #_pinyin = ["@" + s for s in pinyin.valid_symbols]
# _tagdict = ["@" + s for s in tagdict.valid_symbols]

# # Export all symbols:
# symbols = (
#     [_pad]
#     + list(_special)
#     + list(_punctuation)
#     + list(_letters)
#     + _arpabet
#     #+ _tagdict
#     #+ _pinyin
#     + _silences
# )
symbols = "\n '-0123456789_abcdefghijklmnopqrstuvwxyz{|}çóąćęłńŋśźżɔɕɛɟɡɨɲʂʎʐʑʔʲ̪̃"
