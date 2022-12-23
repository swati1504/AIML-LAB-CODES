mov(0,1).
mov(0,2).
mov(0,3).
mov(1,0).
mov(1,2).
mov(2,0).
mov(2,1).
mov(2,4).
mov(3,0).
mov(4,2).

dfs_call(Start,End) :- write('dfs: '), nl, dfs([], Start, End).
dfs(_, End, End):- true.
dfs(P, Start, End):- mov(Start, K), not(member(K, P)), write(K), write('->'), dfs([Start|P], K,End).



