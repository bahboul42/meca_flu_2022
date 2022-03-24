function p = pressure(dom,s,rho)
%% CONSTANTS
[row,column] = size(dom);
p = NaN(size(dom));

g = 9.81; % m/s^2
C = 0; % arbitrary

%% COMPUTATION
s = s.^2;

for i = 1:row
    for j = 1:column
        if(dom(i,j) ~=0)
            p(i,j) = rho*g*(C - (s(i,j)/(2*g)));
        end 
    end 
end
end 


