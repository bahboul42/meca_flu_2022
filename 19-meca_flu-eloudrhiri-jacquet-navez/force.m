function [fx,fy]=force(p,x,y) 
%% CONSTANT(s)
h=0.01;
%% COMPUTATION
fy=0;
fx=0;

for i = 1:length(x)-1
    if x(i) < x(i+1)
        fx = fx + (h)*(p(i)+p(i+1))/2;
    elseif x(i+1) < x(i)
        fx = fx + (-h)*(p(i)+p(i+1))/2;
    end
    
    if y(i) < y(i+1)
        fy = fy + (-h)*(p(i)+p(i+1))/2;
    elseif y(i+1) < y(i)
        fy = fy + (h)*(p(i)+p(i+1))/2;
    end
end 

end 