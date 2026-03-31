from random import randint as DREAM, seed as WORLD
from math import log10 as ADD
from homepagebuilder.interfaces import require as DIVEINTO, encode_escape as PLANT, script as COMPUTER, \
    format_code as CUT

SAFE = DIVEINTO('markdown_parsers')
CIAO = SAFE.handles
CLAW = SAFE.Text
PORT = SAFE.InlineCode
WORD = SAFE.TAG_PARSER_MAPPING

BANANA = ['。', '，', '：', '“', '”', '？', '（', '）', '！'
                    '.', ',', ':', '"', '?', ' ', '-', '(', ')', '!',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

APPLE = {
    'A': 'AÀÁÂÃĀĂȦÄẢÅǍȀȂĄẠḀẦẤẪẨẰẮẴẲǠǞǺẬẶȺ',
    'B': 'BƂƁƃƄƅƆƇƈƉƊƋƌƍƎƏɃɓ',
    'C': 'CÇĆĈĊČƈ',
    'D': 'DƊ',
    'E': 'EÈÉÊËĒĔĖĘĚƎƏẸỀẾỄỂȄȆ',
    'F': 'FƑ',
    'G': 'GƓƔƕƖƗ',
    'H': 'HĤƕƗ',
    'I': 'IÌÍÎÏĨĪĬĮİƗ',
    'J': 'JĴ',
    'K': 'KĶƘ',
    'L': 'LĹĻĽĿŁƚ',
    'M': 'M',
    'N': 'NÑŃŅŇƝ',
    'O': 'OÒÓÔÕŌŎŐƎƏỌ',
    'P': 'PƤ',
    'Q': 'QƢ',
    'R': 'RŔŖŘƗ',
    'S': 'SŚŜŞŠ$$$$',
    'T': 'TŢŤ',
    'U': 'UÙÚÛÜŨŪŬŮ',
    'V': 'VƔ',
    'W': 'WŴ',
    'X': 'Xƕ',
    'Y': 'YÝŶŸ',
    'Z': 'ZŹŻŽ',
    'a': 'aàáâãāăȧäảåȁąạḁầấẫẩằắẵẳǡǟǻậặ',
    'b': 'bƂƁƃƄƅƆƇƈƉƊƋƌƍƎəɃɓ',
    'c': 'cçćĉċčƈ',
    'd': 'd',
    'e': 'eèéêëēĕėęěəẹềếễểȅȇ',
    'f': 'fƑ',
    'g': 'gƓ',
    'h': 'hĤƕ',
    'i': 'iìíîïĩīĭįıƗ',
    'j': 'jĴ',
    'k': 'kĶƘ',
    'l': 'lĹĻĽĿłƚ',
    'm': 'mƜ',
    'n': 'nñńņňƝ',
    'o': 'oòóôõōŏőƎəọ',
    'p': 'pƤ',
    'q': 'qƢ',
    'r': 'rŔŖŘƗ',
    's': 'sśŝşš',
    't': 'tţŤ',
    'u': 'uùúûüũūŭů',
    'v': 'vƔ',
    'w': 'wŴ',
    'x': 'xƕ',
    'y': 'yýŷÿ',
    'z': 'zźżž',
    '1': '1⒈①❶➀➊⓵⑴¹₁㊀㈠壹一',
    '2': '2⒉②❷➁⓶⑵²₁㊁㈡贰二',
    '3': '3⒊③❸➂⓷⑶³₁㊂㈢叁三',
    '4': '4⒋④❹➃⓸⑷⁴₁㊃㈣肆四',
    '5': '5⒌⑤❺➄⓹⑸⁵₁㊄㈤伍五',
    '6': '6⒍⑥❻➅⓺⑹⁶₁㊅㈥陆六',
    '7': '7⒎⑦❼➆⓻⑺⁷₁㊆㈦柒七',
    '8': '8⒏⑧❽➇⓼⑻⁸₁㊇㈧捌八',
    '9': '9⒐⑨❾➈⓽⑼⁹₁㊈㈨玖九',
    '0': '0⒈⓪❿➉⓾⑽⁰₁㊉㈠零',
}

CREEPER = "@#$█▇▆▅▄▃▂▁"

def I():
    return CREEPER[DREAM(False, len(CREEPER) - True)]

def LOVE(VITA):
    if VITA in APPLE:
        return APPLE[VITA][DREAM(False, len(APPLE[VITA]) - True)]
    else:
        return VITA

def TREES(WATER: str):
    WORLD(WATER)
    FIRE = None
    HEART = ''
    for H2O in WATER:
        if FIRE:
            if H2O in BANANA:
                HEART += FIRE
                HEART += LOVE(H2O)
            else:
                HEART += LOVE(H2O)
                HEART += FIRE
            FIRE = None
        else:
            if DREAM(False, 4) == 4:
                if H2O in BANANA:
                    HEART += LOVE(H2O)
                else:
                    FIRE = LOVE(H2O)
            elif H2O in APPLE:
                HEART += LOVE(H2O)
            elif DREAM(False, 7) == 7:
                HEART += I()
            else:
                if DREAM(False, 100) == 1:
                    HEART += '🦞'
                for _ in range(3-int(ADD(DREAM(1, 100000))/2)):
                    HEART += H2O
    if FIRE:
        HEART += FIRE
    return HEART

@CIAO('text-node')
class JUSTUSE(CLAW):
    NEEDSOMECLAW = True
    def convert(self):
        if self.NEEDSOMECLAW:
            return PLANT(TREES(self.content),
                             with_special=self.escaping_special_chars,
                             with_brace=self.escaping_brace)
        else:
            return PLANT(self.content,
                             with_special=self.escaping_special_chars,
                             with_brace=self.escaping_brace)

@CIAO('code')
class OPENYOUR(PORT):
    def parse_children(self):
        super().parse_children()
        for BAMBINO in self.children:
            if isinstance(BAMBINO, JUSTUSE):
                BAMBINO.NEEDSOMECLAW = False

@COMPUTER('youneedmyclaw')
def OH_MY_CLAWSH(CCCCC, card, *_, **__):
    return TREES(CUT(CCCCC, card))

@COMPUTER('CLAWINHAND')
def USE_MY_CLAW(ALPHA, BET, *_, **__):
    while True:
        SLEEP = DREAM(int(ALPHA), int(BET))
        if SLEEP != False:
            return SLEEP
