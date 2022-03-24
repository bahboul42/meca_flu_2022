function c = getCircu(dom, u, v, h)
%% DOMAIN DIMENSIONS
x = [2:21               , ones(size(2:14))*22, 23:180              , ones(size(2:19))*181, 182:200               , ones(size(19:34))*201, 200:-1:180            , ones(size(2:19))*181, 180:-1:23            , ones(size(51:-1:39 ))*22, 21:-1:2                , ones(size(14:39))*2];
y = [ones(size(2:21))*14, 14:-1:2            , ones(size(23:180))*2, 2:19                , ones(size(182:200))*19, 19:34                , ones(size(180:200))*34, 34:51               , ones(size(23:180))*51, 51:-1:39                 , ones(size(21:-1:2))*39, 39:-1:14           ];

%% COMPUTATION
U = zeros(size(x));
V = U;

for k=1:length(x)
    U(k) = u(x(k),y(k));
    V(k) = v(x(k),y(k));
end

c = h * circu(U,V,x,y);
end
