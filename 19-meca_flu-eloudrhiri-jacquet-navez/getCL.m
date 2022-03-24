% CALL : CL = getCL(domain, spacial_step, flux, mode, p)
% IF MODE == 1 : CASE #01 classical pipe
% IF MODE == 2 : CASE #02 classical pipe with narrowing and positive Qin
% IF MODE == 3 : CASE #03 classical pipe with narrowing and negative Qin
% IF MODE >= 4 : CASE #04 & #05 block with with a disbursment's fraction of F

function CL = getCL(dom,h,Qin, mode, F)
%% CONSTANT(s)
[row,column] = size(dom);
%% COMPUTATION
if mode == 1
    %% MODE 1
    CL = dlmread('1-cl.txt','\t');
else
    %% MODE 2 & 3
    % input length
    len_in = 0; 
    lens_in = [];
    k=1;

    lens_in(1) = 0;

    for j = 2:column
        if(dom(2,j) == 2)
            len_in = len_in + 1;
            lens_in(k+1) = k*h;
            k=k+1;
        end 
    end

    nodes_in = len_in;
    len_in = len_in*h - h;
    U_in = Qin/len_in;

    % ouput length
    len_out = 0;
    lens_out = [];
    k = 1;

    lens_out(1) = 0;

    for j=2:column
        if (dom(201,j) == 2)
            len_out = len_out + 1;
            lens_out(k+1) = k*h;
            k=k+1;
        end
    end

    nodes_out = len_out;
    len_out = len_out*h - h;
    U_out = Qin/len_out;

    % INNER
    CL = NaN(size(dom));
    
    for i=1:row 
        for j=1:column 
            if (dom(i,j) == 0 || dom(i,j) == 1)
                CL(i,j) = 0;
            end 
        end 
    end

    % INPUT
    k = 1;
    i = 2; % input on i == 2
    
    for j = 2:column
        if (dom(i,j) == 2) %% input on i = 2
            if(k <= nodes_in)
                CL(i,j) = (Qin/(len_in)) * lens_in(k);
                k = k + 1;
            end
        end
    end

    % input sides
    CL(2:22,14) = CL(2,14);
    CL(2:22,39) = CL(2,39);

    % first corners
    CL(22,2:14) = CL(22,14);
    CL(22,39:51) = CL(22,39);

    % inner sides
    CL(22:181,2) = CL(22,2);
    CL(22:181,51) = CL(22,51);

    % second corners
    CL(181,2:19) = CL(181,2);
    CL(181,34:51) = CL(181,51);

    % output sides
    CL(181:201,19) = CL(181,19);
    CL(181:201,34) = CL(181,34);

    % OUTPUT
    k = 1;
    i = 201; % output on i == 201
    
    for j = 1:column
        if (dom(i,j) == 2)
            if(k <= nodes_out)
                CL(i,j) = (Qin/(len_out)) * lens_out(k);
                k = k + 1;
            end
        end
    end
    %% MODE 4 & 5
    if F > 0
        C = 0; % integration constant
        cl = F*Qin + C; % value of the limit condition on the block
        
        CL(36:108,11:42) = cl; % applies cl to the block's outer border
        CL(37:107,12:41) = 0;
    end
end
end