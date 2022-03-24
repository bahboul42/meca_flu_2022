function c = circu(u,v,x,y)
%% INIT(s)
circulation = zeros(size(x));
%% COMPUTATION
for i = 1:length(x)-1
    if y(i) ~= y(i+1)
        circulation(i) = (y(i+1)-y(i))*((v(i+1)+v(i))/2);
    else
        circulation(i) = (x(i+1)-x(i))*((u(i+1)+u(i))/2);
    end
end

c = sum(circulation);
end 