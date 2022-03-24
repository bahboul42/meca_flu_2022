function [fx, fy] = getForce(dom, p, Qin)
%% BLOCK DIMENSIONS
% x constant, y varies
x = 36:108;
y1 = ones(size(36:108)) * 11;
y2 = ones(size(36:108)) * 42;

% y constant, x varies
y = 11:42;
x1 = ones(size(11:42)) * 36;
x2 = ones(size(11:42)) * 108;

%% COMPUTATION
Py1 = zeros(size(x));
Py2 = Py1;
for k=1:length(x)
    Py1(k) = p(x(k), y1(k));
    Py2(k) = p(x(k), y2(k));
end

Px1 = zeros(size(y));
Px2 = Px1;
for k = 1:length(y)
    Px1(k) = p(x1(k), y(k));
    Px2(k) = p(x2(k), y(k));
end

% y component on the x axis because the domain is facing downward
[fy1, ~] = force(Py1,x,y1);
[fy2, ~] = force(Py2,x,y2);

% x component on the y axis because the domain is facing downward
[~, fx1] = force(Px1,x1,y);
[~, fx2] = force(Px2,x2,y);

fx = (fx1 - fx2) * sign(Qin);
fy = fy1 - fy2;

end


 