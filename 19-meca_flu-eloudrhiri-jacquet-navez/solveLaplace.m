function psi = solveLaplace(dom,num,cl)
%% INIT(s)
[row,column] = size(num);
n = nnz(dom);

b = ones(n,1);
L = spalloc(n,n,5*n);

%% COMPUTATION
% filling the laplace matrix
for l = 1:row
    for k = 1:column
        if num(l,k) > 0
            [j,a,b_i] = getCoeff(num(l-1,k), num(l+1,k), num(l,k-1), num(l,k+1), num(l,k), dom(l,k), cl(l,k));
            b(num(l,k),1) = b_i;
            
            L(num(l,k),j(:,1)) = a(:,1);
        end
    end
end

% solving the system
X = L\b;
psi = NaN(row,column);

% filling the psi matrix
for l = 1:row
    for k = 1:column
        if num(l,k) ~= 0
            psi(l,k) = X(num(l,k),1);
        end
    end
end 
end