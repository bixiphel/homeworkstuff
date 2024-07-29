% Completed by: bixiphel

% Here are some men
man(stuart).
man(kurt).
man(mark).
man(raymond).
man(august).
man(hans).
man(ryan).
man(adam).
man(max).

% Here are some women.
woman(erica).
woman(susan).
woman(elaine).
woman(viola).
woman(ida).
woman(florence).
woman(marissa).
woman(annika).
woman(kaita).

% For our purposes, we will always put the woman's name first in the
% marriage facts.
married(erica, stuart).
married(susan, mark).
married(elaine, raymond).
married(viola, august).
married(ida, hans).
married(marissa, ryan).
married(annika, adam).

% For our purposes, the parent's name always comes first
parent(susan, marissa).
parent(mark, marissa).
parent(susan, annika).
parent(mark, annika).
parent(elaine, mark).
parent(raymond, mark).
parent(elaine, stuart).
parent(raymond, stuart).
parent(elaine, kurt).
parent(raymond, kurt).
parent(viola, elaine).
parent(august, elaine).
parent(ida, raymond).
parent(hans, raymond).





% Returns true if X is Y's mother-in-law
motherInLaw(X,Y) :- 
    married(Q, Y), % Checks if Y is married
    woman(X), % Checks if X is in the list of women
    parent(X, Q). % Checks if X is Q's parent

% Checks if X is Y's grandparent
grandParent(X,Y) :- 
    parent(X,Z), % Checks if X is Z's parent
    parent(Z, Y). % Checks if Z is Y's parent

% Checks if X is Y's grandmother
grandMother(X,Y) :- 
    parent(X,Z), % Checks if X is Z's parent
    parent(Z, Y), % Checks if Z is Y's parent
    woman(X). % Checks if X is in the list of women














