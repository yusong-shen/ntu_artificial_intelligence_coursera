/* prolog tutorial  2.7 Prolog lists */

/*   built-in SWI-Prolog  
member(X,[X|R]).
member(X,[Y|R]) :- member(X,R).
*/

takeout(X,[X|R],R).
takeout(X,[F|R],[F|S]) :- takeout(X,R,S).

putin(X,L,R) :- takeout(X,R,L).

/*   built-in SWI-Prolog
append([X|Y],Z,[X|W]) :- append(Y,Z,W).
append([],X,X).
*/

*/    BUILT-IN SWI-Prolog
reverse([X|Y],Z,W) :- reverse(Y,[X|Z],W).
reverse([],X,X).

reverse(A,R) :- reverse(A,[],R).
*/

perm([X|Y],Z) :- perm(Y,W), takeout(X,Z,W).   
perm([],[]).

subset([X|R],S) :- member(X,S), subset(R,S).
subset([],_).

union([X|Y],Z,W) :- member(X,Z),  union(Y,Z,W).
union([X|Y],Z,[X|W]) :- \+ member(X,Z), union(Y,Z,W).
union([],Z,Z).
 
intersection([X|Y],M,[X|Z]) :- member(X,M), intersection(Y,M,Z).
intersection([X|Y],M,Z) :- \+ member(X,M), intersection(Y,M,Z).
intersection([],M,[]).

mergesort([],[]).    /* covers special case */
mergesort([A],[A]).
mergesort([A,B|R],S) :-  
   split([A,B|R],L1,L2),
   mergesort(L1,S1),
   mergesort(L2,S2),
   merge(S1,S2,S).

split([],[],[]).
split([A],[A],[]).
split([A,B|R],[A|Ra],[B|Rb]) :-  split(R,Ra,Rb).

merge(A,[],A).
merge([],B,B).
merge([A|Ra],[B|Rb],[A|M]) :-  A =<B, merge(Ra,[B|Rb],M).
merge([A|Ra],[B|Rb],[B|M]) :-  A >B,  merge([A|Ra],Rb,M).



sequence_append((X,R),S,(X,T)) :-
           !, 
           sequence_append(R,S,T).
sequence_append((X),S,(X,S)). 

