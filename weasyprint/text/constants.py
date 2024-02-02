"""Constants used for text layout."""

from .ffi import pango

# Pango features
PANGO_STYLE = {
    'normal': pango.PANGO_STYLE_NORMAL,
    'oblique': pango.PANGO_STYLE_OBLIQUE,
    'italic': pango.PANGO_STYLE_ITALIC,
}
PANGO_STRETCH = {
    'ultra-condensed': pango.PANGO_STRETCH_ULTRA_CONDENSED,
    'extra-condensed': pango.PANGO_STRETCH_EXTRA_CONDENSED,
    'condensed': pango.PANGO_STRETCH_CONDENSED,
    'semi-condensed': pango.PANGO_STRETCH_SEMI_CONDENSED,
    'normal': pango.PANGO_STRETCH_NORMAL,
    'semi-expanded': pango.PANGO_STRETCH_SEMI_EXPANDED,
    'expanded': pango.PANGO_STRETCH_EXPANDED,
    'extra-expanded': pango.PANGO_STRETCH_EXTRA_EXPANDED,
    'ultra-expanded': pango.PANGO_STRETCH_ULTRA_EXPANDED,
}
# From https://drafts.csswg.org/css-fonts/#font-stretch-prop
PANGO_STRETCH_PERCENT = {
    50: pango.PANGO_STRETCH_ULTRA_CONDENSED,
    62.5: pango.PANGO_STRETCH_EXTRA_CONDENSED,
    75: pango.PANGO_STRETCH_CONDENSED,
    87.5: pango.PANGO_STRETCH_SEMI_CONDENSED,
    100: pango.PANGO_STRETCH_NORMAL,
    112.5: pango.PANGO_STRETCH_SEMI_EXPANDED,
    125: pango.PANGO_STRETCH_EXPANDED,
    150: pango.PANGO_STRETCH_EXTRA_EXPANDED,
    200: pango.PANGO_STRETCH_ULTRA_EXPANDED,
}
PANGO_WRAP_MODE = {
    'WRAP_WORD': pango.PANGO_WRAP_WORD,
    'WRAP_CHAR': pango.PANGO_WRAP_CHAR,
    'WRAP_WORD_CHAR': pango.PANGO_WRAP_WORD_CHAR
}

# Language system tags
# From https://docs.microsoft.com/typography/opentype/spec/languagetags
LST_TO_ISO = {
    'aba': 'abq',
    'afk': 'afr',
    'afr': 'aar',
    'agw': 'ahg',
    'als': 'gsw',
    'alt': 'atv',
    'ari': 'aiw',
    'ark': 'mhv',
    'ath': 'apk',
    'avr': 'ava',
    'bad': 'bfq',
    'bad0': 'bad',
    'bag': 'bfy',
    'bal': 'krc',
    'bau': 'bci',
    'bch': 'bcq',
    'bgr': 'bul',
    'bil': 'byn',
    'bkf': 'bla',
    'bli': 'bal',
    'bln': 'bjt',
    'blt': 'bft',
    'bmb': 'bam',
    'bri': 'bra',
    'brm': 'mya',
    'bsh': 'bak',
    'bti': 'btb',
    'chg': 'sgw',
    'chh': 'hne',
    'chi': 'nya',
    'chk': 'ckt',
    'chk0': 'chk',
    'chu': 'chv',
    'chy': 'chy',
    'cmr': 'swb',
    'crr': 'crx',
    'crt': 'crh',
    'csl': 'chu',
    'csy': 'ces',
    'dcr': 'cwd',
    'dgr': 'doi',
    'djr': 'dje',
    'djr0': 'djr',
    'dng': 'ada',
    'dnk': 'din',
    'dri': 'prs',
    'dun': 'dng',
    'dzn': 'dzo',
    'ebi': 'igb',
    'ecr': 'crj',
    'edo': 'bin',
    'erz': 'myv',
    'esp': 'spa',
    'eti': 'est',
    'euq': 'eus',
    'evk': 'evn',
    'evn': 'eve',
    'fan': 'acf',
    'fan0': 'fan',
    'far': 'fas',
    'fji': 'fij',
    'fle': 'vls',
    'fne': 'enf',
    'fos': 'fao',
    'fri': 'fry',
    'frl': 'fur',
    'frp': 'frp',
    'fta': 'fuf',
    'gad': 'gaa',
    'gae': 'gla',
    'gal': 'glg',
    'gaw': 'gbm',
    'gil': 'niv',
    'gil0': 'gil',
    'gmz': 'guk',
    'grn': 'kal',
    'gro': 'grt',
    'gua': 'grn',
    'hai': 'hat',
    'hal': 'flm',
    'har': 'hoj',
    'hbn': 'amf',
    'hma': 'mrj',
    'hnd': 'hno',
    'ho': 'hoc',
    'hri': 'har',
    'hye0': 'hye',
    'ijo': 'ijc',
    'ing': 'inh',
    'inu': 'iku',
    'iri': 'gle',
    'irt': 'gle',
    'ism': 'smn',
    'iwr': 'heb',
    'jan': 'jpn',
    'jii': 'yid',
    'jud': 'lad',
    'jul': 'dyu',
    'kab': 'kbd',
    'kab0': 'kab',
    'kac': 'kfr',
    'kal': 'kln',
    'kar': 'krc',
    'keb': 'ktb',
    'kge': 'kat',
    'kha': 'kjh',
    'khk': 'kca',
    'khs': 'kca',
    'khv': 'kca',
    'kis': 'kqs',
    'kkn': 'kex',
    'klm': 'xal',
    'kmb': 'kam',
    'kmn': 'kfy',
    'kmo': 'kmw',
    'kms': 'kxc',
    'knr': 'kau',
    'kod': 'kfa',
    'koh': 'okm',
    'kon': 'ktu',
    'kon0': 'kon',
    'kop': 'koi',
    'koz': 'kpv',
    'kpl': 'kpe',
    'krk': 'kaa',
    'krm': 'kdr',
    'krn': 'kar',
    'krt': 'kqy',
    'ksh': 'kas',
    'ksh0': 'ksh',
    'ksi': 'kha',
    'ksm': 'sjd',
    'kui': 'kxu',
    'kul': 'kfx',
    'kuu': 'kru',
    'kuy': 'kdt',
    'kyk': 'kpy',
    'lad': 'lld',
    'lah': 'bfu',
    'lak': 'lbe',
    'lam': 'lmn',
    'laz': 'lzz',
    'lcr': 'crm',
    'ldk': 'lbj',
    'lma': 'mhr',
    'lmb': 'lif',
    'lmw': 'ngl',
    'lsb': 'dsb',
    'lsm': 'smj',
    'lth': 'lit',
    'luh': 'luy',
    'lvi': 'lav',
    'maj': 'mpe',
    'mak': 'vmw',
    'man': 'mns',
    'map': 'arn',
    'maw': 'mwr',
    'mbn': 'kmb',
    'mch': 'mnc',
    'mcr': 'crm',
    'mde': 'men',
    'men': 'mym',
    'miz': 'lus',
    'mkr': 'mak',
    'mle': 'mdy',
    'mln': 'mlq',
    'mlr': 'mal',
    'mly': 'msa',
    'mnd': 'mnk',
    'mng': 'mon',
    'mnk': 'man',
    'mnx': 'glv',
    'mok': 'mdf',
    'mon': 'mnw',
    'mth': 'mai',
    'mts': 'mlt',
    'mun': 'unr',
    'nan': 'gld',
    'nas': 'nsk',
    'ncr': 'csw',
    'ndg': 'ndo',
    'nhc': 'csw',
    'nis': 'dap',
    'nkl': 'nyn',
    'nko': 'nqo',
    'nor': 'nob',
    'nsm': 'sme',
    'nta': 'nod',
    'nto': 'epo',
    'nyn': 'nno',
    'ocr': 'ojs',
    'ojb': 'oji',
    'oro': 'orm',
    'paa': 'sam',
    'pal': 'pli',
    'pap': 'plp',
    'pap0': 'pap',
    'pas': 'pus',
    'pgr': 'ell',
    'pil': 'fil',
    'plg': 'pce',
    'plk': 'pol',
    'ptg': 'por',
    'qin': 'bgr',
    'rbu': 'bxr',
    'rcr': 'atj',
    'rms': 'roh',
    'rom': 'ron',
    'roy': 'rom',
    'rsy': 'rue',
    'rua': 'kin',
    'sad': 'sck',
    'say': 'chp',
    'sek': 'xan',
    'sel': 'sel',
    'sgo': 'sag',
    'sgs': 'sgs',
    'sib': 'sjo',
    'sig': 'xst',
    'sks': 'sms',
    'sky': 'slk',
    'sla': 'scs',
    'sml': 'som',
    'sna': 'seh',
    'sna0': 'sna',
    'snh': 'sin',
    'sog': 'gru',
    'srb': 'srp',
    'ssl': 'xsl',
    'ssm': 'sma',
    'sur': 'suq',
    'sve': 'swe',
    'swa': 'aii',
    'swk': 'swa',
    'swz': 'ssw',
    'sxt': 'ngo',
    'taj': 'tgk',
    'tcr': 'cwd',
    'tgn': 'ton',
    'tgr': 'tig',
    'tgy': 'tir',
    'tht': 'tah',
    'tib': 'bod',
    'tkm': 'tuk',
    'tmn': 'tem',
    'tna': 'tsn',
    'tne': 'enh',
    'tng': 'toi',
    'tod': 'xal',
    'tod0': 'tod',
    'trk': 'tur',
    'tsg': 'tso',
    'tua': 'tru',
    'tul': 'tcy',
    'tuv': 'tyv',
    'twi': 'aka',
    'usb': 'hsb',
    'uyg': 'uig',
    'vit': 'vie',
    'vro': 'vro',
    'wa': 'wbm',
    'wag': 'wbr',
    'wcr': 'crk',
    'wel': 'cym',
    'wlf': 'wol',
    'xbd': 'khb',
    'xhs': 'xho',
    'yak': 'sah',
    'yba': 'yor',
    'ycr': 'cre',
    'yim': 'iii',
    'zhh': 'zho',
    'zhp': 'zho',
    'zhs': 'zho',
    'zht': 'zho',
    'znd': 'zne',
}

# Font features
LIGATURE_KEYS = {
    'common-ligatures': ['liga', 'clig'],
    'historical-ligatures': ['hlig'],
    'discretionary-ligatures': ['dlig'],
    'contextual': ['calt'],
}
CAPS_KEYS = {
    'small-caps': ['smcp'],
    'all-small-caps': ['c2sc', 'smcp'],
    'petite-caps': ['pcap'],
    'all-petite-caps': ['c2pc', 'pcap'],
    'unicase': ['unic'],
    'titling-caps': ['titl'],
}
NUMERIC_KEYS = {
    'lining-nums': 'lnum',
    'oldstyle-nums': 'onum',
    'proportional-nums': 'pnum',
    'tabular-nums': 'tnum',
    'diagonal-fractions': 'frac',
    'stacked-fractions': 'afrc',
    'ordinal': 'ordn',
    'slashed-zero': 'zero',
}
EAST_ASIAN_KEYS = {
    'jis78': 'jp78',
    'jis83': 'jp83',
    'jis90': 'jp90',
    'jis04': 'jp04',
    'simplified': 'smpl',
    'traditional': 'trad',
    'full-width': 'fwid',
    'proportional-width': 'pwid',
    'ruby': 'ruby',
}

# Fontconfig features
FONTCONFIG_WEIGHT = {
    'normal': 80,
    'bold': 200,
    100: 0,
    200: 40,
    300: 50,
    400: 80,
    500: 100,
    600: 180,
    700: 200,
    800: 205,
    900: 210,
}
FONTCONFIG_STYLE = {
    'normal': 'roman',
    'italic': 'italic',
    'oblique': 'oblique',
}
FONTCONFIG_STRETCH = {
    'normal': 'normal',
    'ultra-condensed': 'ultracondensed',
    'extra-condensed': 'extracondensed',
    'condensed': 'condensed',
    'semi-condensed': 'semicondensed',
    'semi-expanded': 'semiexpanded',
    'expanded': 'expanded',
    'extra-expanded': 'extraexpanded',
    'ultra-expanded': 'ultraexpanded',
}
