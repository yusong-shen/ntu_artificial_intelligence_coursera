rev([X|Y],Z,W) :- rev(Y,[X|Z],W).
rev([],X,X).

rev(A,B) :- rev(B,[],A).
