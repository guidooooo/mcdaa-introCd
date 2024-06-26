"""
Middle English: - people.stanford.edu/widner/content/text-mining-middle-ages (slide 13), textifier.com/resources/common-english-words.txt, en.wikipedia.org/wiki/Middle_English, en.wiktionary.org/wiki/Category:Middle_English_prepositions, en.wiktionary.org/wiki/Category:MIddle_English_determiners, en.wiktionary.org/wiki/Category:MIddle_English_conjunctions
"""

STOPS: list[str] = [
    "ac",
    "afore",
    "ake",
    "an",
    "because",
    "ek",
    "fore",
    "for",
    "forthi",
    "whan",
    "whanne",
    "whilis",
    "if",
    "yf",
    "yif",
    "yiff",
    "yit",
    "yet",
    "and",
    "or",
    "any",
    "but",
    "a",
    "y",
    "ne",
    "no",
    "not",
    "nor",
    "nat",
    "however",
    "o",
    "than",
    "n",
    "nn",
    "nnn",
    "to",
    "with",
    "wyth",
    "at",
    "as",
    "of",
    "off",
    "from",
    "on",
    "before",
    "by",
    "after",
    "about",
    "above",
    "across",
    "among",
    "against",
    "below",
    "between",
    "during",
    "into",
    "in",
    "out",
    "over",
    "under",
    "abord",
    "aboven",
    "afore",
    "aftir",
    "bi",
    "bifor",
    "bisyde",
    "bitwixten",
    "byfore",
    "bytwene",
    "down",
    "doun",
    "embe",
    "fra",
    "ine",
    "mid",
    "sanz",
    "tyll",
    "umbe",
    "vnto",
    "vpon",
    "withouten",
    "with",
    "wth",
    "wtout",
    "can",
    "cannot",
    "can't",
    "t",
    "could",
    "did",
    "do",
    "does",
    "wyl",
    "will",
    "would",
    "haven",
    "hast",
    "haþ",
    "havende",
    "hadde",
    "haddest",
    "hadden",
    "had",
    "hadn't",
    "has",
    "hasn't",
    "hasn",
    "have",
    "haven't",
    "haven",
    "having",
    "be",
    "ben",
    "been",
    "am",
    "art",
    "is",
    "ys",
    "aren",
    "are",
    "aren't",
    "bende",
    "isn't",
    "isn",
    "wæs",
    "was",
    "wasn't",
    "wasn",
    "weren",
    "were",
    "weren't",
    "þe",
    "the",
    "þat",
    "þenne",
    "þis",
    "whiche",
    "which",
    "while",
    "who",
    "whom",
    "what",
    "when",
    "where",
    "why",
    "that",
    "that's",
    "s",
    "there",
    "ther",
    "þer",
    "there's",
    "these",
    "this",
    "those",
    "boþe",
    "thilke",
    "eiþer",
    "either",
    "neither",
    "al",
    "all",
    "also",
    "ane",
    "ic",
    "ich",
    "i",
    "i'd",
    "d",
    "i'll",
    "ll",
    "i'm",
    "m",
    "i've",
    "ve",
    "me",
    "mi",
    "my",
    "minen",
    "min",
    "mire",
    "minre",
    "myself",
    "þu",
    "þou",
    "tu",
    "þeou",
    "thi",
    "you",
    "þe",
    "þi",
    "ti",
    "þin",
    "þyn",
    "þeself",
    "you'd",
    "you'll",
    "you're",
    "re",
    "you've",
    "your",
    "yours",
    "yourself",
    "yourselves",
    "thee",
    "thy",
    "thou",
    "ye",
    "thine",
    "he",
    "he'd",
    "he'll",
    "he's",
    "she",
    "sche",
    "she'd",
    "she'll",
    "she's",
    "her",
    "heo",
    "hie",
    "hies",
    "hire",
    "hir",
    "hers",
    "hio",
    "heore",
    "herself",
    "him",
    "hine",
    "hisse",
    "hes",
    "himself",
    "his",
    "hys",
    "hym",
    "hit",
    "yt",
    "it",
    "its",
    "it's",
    "tis",
    "twas",
    "itself",
    "þay",
    "youre",
    "hyr",
    "hem",
    "we",
    "we'd",
    "we'll",
    "we're",
    "we've",
    "us",
    "ous",
    "our",
    "ure",
    "ures",
    "urne",
    "ours",
    "oures",
    "ourselves",
    "their",
    "theirs",
    "them",
    "themselves",
    "thai",
    "thei",
    "they",
    "they'd",
    "they'll",
    "they're",
    "they've",
    "whan",
    "shall",
    "may",
    "thus",
    "hath",
    "doth"
]
