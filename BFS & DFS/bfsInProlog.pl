s(a,b).
s(a,c).
s(b,d).
s(b,e).
s(c,f).
s(c,g).
s(d,h).
s(e,i).
s(e,j).
s(f,k).

goal(f).
goal(j).

solve(Start, Solution):-
	breadthfirst([[Start]], Solution).

breadthfirst([[Node|Path]|_], [Node|Path]) :- goal(Node).

breadthfirst([Path|Paths], Solution):-
	extend(Path, NewPaths), write(NewPaths), nl, conc(Paths, NewPaths, Paths1), breadthfirst(Paths1, Solution).

extend([Node|Path], NewPaths):-
	bagof([NewNode, Node|Path], (s(Node, NewNode), not(member(NewNode,[Node|Path]))), NewPaths), !.

extend(_, []).

conc([], L, L).
conc([X|L1], L2, [X|L3]):- write('conc'), write(X), write(' '), write(L1), write(' '), write(L2), conc(L1, L2, L3).
