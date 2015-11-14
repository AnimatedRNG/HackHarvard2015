def read_from_file():
    rules = {}
    with open("config.txt") as f:
        lines = f.readlines()
        for line in lines:
            genRule(line, rules)
    return rules

MOVES = {'r_', 'ur', 'u_', 'ul', 'l_', 'ld', 'd_', 'dr'}

"""
RIGHT r_
UP_RIGHT ur
UP u_
UP_LEFT ul
LEFT l_
DOWN_LEFT ld
DOWN d_
DOWN_RIGHT dr
"""

def genRule(line, rules):
    assert line[0] == '0', 'Rule does not start with root node!'
    i = 1
    currentLevel = rules
    while(line[i] != ':'):
        assert line[i] == '-', 'Invalid config at line: \n' + line
        move = line[i+1:i+3]
        assert move in MOVES
        if not (move in currentLevel):
            currentLevel[move] = {}
        currentLevel = currentLevel[move]
        i += 3
        assert i + 3 < len(line), 'Invaid config at line: \n' + line

    assert (line[i + 1] == ' ' or line[i + 1] == '\t'), 'Character after : must be whitespace'
    assert (line[i + 2] == "\"" and line[-2] == "\""), 'Command must be enclosed in quotations'
    currentLevel[move] = line[i + 3: len(line) - 1]