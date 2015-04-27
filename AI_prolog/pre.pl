pre([], L).
pre([H|TA], [H|TB]) :- pre(TA, TB).


/*
pre(A, B):- append(A, _, B).

append([], A, B).
append([H|A], B, [H|C]) :- append(A, B, C).
*/
