# taking example of the wumpus world to show resolution algorithm

def checkIfSubset(new, clauses):
    for clause in new:
        if not clause in clauses: return False
    return True

def PLResolve(clause1, clause2):
    commonLiterals = [value for value in clause1 if value in clause2]
    for literal in commonLiterals:
        clause1.remove(literal)
        clause2.remove(literal)

    l1_tp, l2_tp = [], []

    for l1 in clause1:
        for l2 in clause2:
            cond1 = len(l1) == 1 and len(l2) == 2 and l1[0] == l2[1]
            cond2 = len(l2) == 1 and len(l1) == 2 and l2[0] == l1[1]
            if cond1 or cond2:
                l1_tp.append(l1), l2_tp.append(l2)

    if l1_tp == [] and l2_tp == []: return None

    for l1 in l1_tp: clause1.remove(l1)
    for l2 in l2_tp: clause2.remove(l2)

    return sorted(commonLiterals+clause1+clause2)

def PLResolution(clauses):
    for clause in clauses: sorted(clause)
    new = []
    while True:
        pairs = [(ci, cj) for idx, ci in enumerate(clauses) for cj in clauses[idx + 1:]]
        for pair in pairs:
            resolvent = PLResolve(pair[0].copy(),pair[1].copy())
            print(f"{pair[0]} {pair[1]} -> {resolvent}")
            if resolvent is None: None
            elif len(resolvent) == 0: return True
            else:
                if not resolvent in new :
                    new.append(resolvent)
        if checkIfSubset(new,clauses): return False
        clauses.extend(clause for clause in new if clause not in clauses)

# A -> P(2,1)
# B -> P(1,2)
# C -> B(1,1)
# If a set of clauses is unsatisfiable, then the resolution closure of those clauses
# contains the empty clause.
# If True then set of clauses are unsatisfiable

clauses = [
    ["~A","C"],
    ["A","B","~C"],
    ["~B","C"],
    ["~C"],
    ["B"],
]

print(PLResolution(clauses))