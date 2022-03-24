function [u,v,s] = velocity(psy,dom,h)
%% SPEED DOMAIN
u = NaN(size(dom)); % speed x component
v = NaN(size(dom)); % speed y component
s = NaN(size(dom)); % speed magnitude i.e mean speed
%% COMPUTATION
[row, column] = size(dom);
for i = 2:row
   for j = 2:column
       if (dom(i,j) ~= 0)
           u(i,j) = deriv(psy(i,j-1),psy(i,j),psy(i,j+1),dom(i,j-1),dom(i,j),dom(i,j+1),h);
           v(i,j) = -deriv(psy(i-1,j),psy(i,j),psy(i+1,j),dom(i-1,j),dom(i,j),dom(i+1,j),h);
           s(i,j) = sqrt((u(i,j)).^2 + (v(i,j).^2));
       end
   end 
end 

end 
