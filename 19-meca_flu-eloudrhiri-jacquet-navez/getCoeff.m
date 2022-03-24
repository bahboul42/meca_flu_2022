function [j,a,b] = getCoeff(num_left, num_right, num_down, num_up, num_cent, type_cent, cl_cent)
%{
num_xxx : number of the xxx^th node (left, right, down, up)
type_cent : = 0 out of dom
            = 1 surrounded by nodes or limit conditons
            = 2 limit condition of Dirichlet
cl_cent : cl value by the considered node
a : column vector of equ's coefs of the central node
j : column numbers of the coefs inside a
b : fixed laplace valuea
%}

j = 0;
b = 0;

if type_cent == 1 % r + l + u + d - 4c = 0
    a = [1;1;1;1;-4];
    j = [num_left;num_right;num_down;num_up;num_cent];
elseif type_cent == 2 % c = b
    b = cl_cent;
    a = 1;
    j = num_cent;
else
    a = 0;
end

end 