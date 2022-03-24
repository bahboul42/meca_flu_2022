function v = deriv(f_left, f_c, f_right, type_left, type_c, type_right,h)
%% COMPUTATION
if(type_left == 0 && type_c == 0 && type_right == 0)
   % trivial case
   v = 0;
elseif(type_left == 0) 
    % rear centered derivative
    v = (f_right - f_c)/h; 
elseif(type_right ==0) 
    % front centered derivative
    v = (f_c - f_left)/h;
elseif(type_c ==0 && type_r ~= 0 && type_l ~=0) 
    v=(f_c - f_left)/h;
else
    % centered derivative -> most common case
    v = (f_right - f_left)/(2*h);
end
end