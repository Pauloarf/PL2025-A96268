import ply.lex as lex
import sys

#region ============== Declarations ==============
tokens = (
    "FILENAME",
    "NEWLINE",
    "PARAV",
    "SEP",
    "ABC",
    "VERSE",
    "ESEP",
)
states = (
    ("META", "exclusive"),
    # ("ABC", "exclusive"),
    ("POEM", "exclusive"),
)
#endregion ============== Declarations ==============

#region ============== Initializations ==============
def t_ANY_COM(t): r"<!--(.|\n)*-->"; pass

def t_ANY_FILENAME(t): r"^==>(.+)"; t.lexer.begin("META"); return t

def t_META_SEP(t): r"\n\n+"; t.lexer.begin("POEM"); return t
def t_META_PARAV(t): 
    r"(?P<key>\w+):(?P<value>.*)"
    groups = t.lexer.lexmatch.groupdict()
    t.value = (groups["key"], groups["value"])
    return t

def t_POEM_ABC(t): r"<abc>(?P<abcbody>[\s\S]*)</abc>"; t.value = t.lexer.lexmatch.groupdict()["abcbody"]; return t 
def t_POEM_VERSE(t): r"\w.*"; return t
def t_POEM_ESEP(t): r"\n\n+"; return t

def t_ANY_NEWLINE(t): r"\n+"; t.lexer.lineno += len(t.value); pass
def t_ANY_error(t): 
    print(f"\x1b[31mERROR @{t.lexer.lexstate} #{t.lexer.lexpos}:\x1b[0m Unexpected character: {repr(t.value[0])}")
    t.lexer.skip(1)
    pass
#endregion ============== Initializations ==============

#region ============== Processing ==============
lexer = lex.lex()
lexer.input(sys.stdin.read())

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break

    print(f"\x1b[36mTOKEN:\x1b[0m {tok}")
    match ((tok.type, tok.value)):
        case ("PARAV", ("title", v)):
            print(f"\x1b[93mPARAV (title):\x1b[0m {v}")
#endregion ============== Processing ==============
