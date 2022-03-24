function [out] = main(coef, show) 
%% CONSTANT(s)
rho = 1000; % Kg/m^3
Qin = 55*10^-3; %m^2/s
%% CASES
if coef == 1
    dom = dlmread('1-dom.txt','\t');
    num = dlmread('1-num.txt','\t');
    h = 0.5;
    F = -1; % no disbursment
    cl = getCL(dom, h, Qin, coef, F);
elseif (coef == 2)
    dom = dlmread('2-dom.txt','\t');
    num = dlmread('2-num.txt','\t');
    h = 0.01;
    F = -1; % no disbursment
    cl = getCL(dom, h, Qin, coef, F);
elseif coef == 3
    dom = dlmread('2-dom.txt','\t');
    num = dlmread('2-num.txt','\t');
    h = 0.01;
    F = -1; % no disbursment
    Qin = -Qin;
    cl = getCL(dom, h, Qin, coef, F);
elseif coef == 4
    dom = dlmread('3-dom.txt','\t');
    num = dlmread('3-num.txt','\t');
    h = 0.01;
    F = 0.5; % disbursment
    cl = getCL(dom, h, Qin, coef, F);
else
    dom = dlmread('3-dom.txt','\t');
    num = dlmread('3-num.txt','\t');
    h = 0.01;
    F = 0.207;
    cl = getCL(dom, h, Qin, coef, F);
end
%% COMPUTATION    
psi = solveLaplace(dom, num, cl);
[u, v, s] = velocity(psi, dom, h);

if coef > 1
    p = pressure(dom, s, rho);
    c = getCircu(dom, u, v, h);
    [fx,fy] = getForce(dom, p, Qin);
    
    out = struct('dom', dom, 'num', num, 'cl', cl, 'psi', psi, 'u', u, 'v', v, 's', s, 'p', F, 'circu', c, 'trainee', fx, 'portance', fy);
else
    out = struct('dom', dom, 'num', num, 'cl', cl, 'psi', psi, 'u', u, 'v', v, 's', s);
end
%% PLOTS
if show == 1
    if coef > 1
        u = u';
        v = v';
        s = s';
        psi = psi';
        
        % Pressure
        figure
        pcolor(p')
        title('Pressure')
        xlabel('x')
        ylabel('y')
        axis equal
        shading flat
        colorbar
        colormap(jet)
    end
    % Horizontal Vel
    figure
    pcolor(u)
    title('Horizontal Velocity')
    xlabel('x')
    ylabel('y')
    axis equal
    shading flat
    colorbar
    colormap(jet)

    % Vertical Vel
    figure
    pcolor(v)
    title('Vertical Velocity')
    xlabel('x')
    ylabel('y')
    axis equal
    shading flat
    colorbar
    colormap(jet)

    % Mean Vel
    figure
    pcolor(s)
    title('Mean Velocity')
    xlabel('x')
    ylabel('y')
    axis equal
    shading flat
    colorbar
    colormap(jet)

    % Vel Field
    figure
    quiver(u, v, 'b');
    title('Velocity Field')
    xlabel('x')
    ylabel('y')
    axis equal

    % Stream line
    figure
    pcolor(psi)
    title('Streamlines / Stream function')
    xlabel('x')
    ylabel('y')
    axis equal
    shading flat
    colorbar
    colormap(jet)
    hold on;
    h = streamslice(u, v);
    set(h, 'Color', 'black')
end
end 
