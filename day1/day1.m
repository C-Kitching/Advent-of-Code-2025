function day1()
    part1();
    part1_efficient();

    part2();
    part2_efficient();
end

function part1()
    
    lines = readlines("input.txt");

    pos = 50;
    count = 0;

    for line = lines'

        str = line{1};
        if isempty(str)
            continue;
        end

        dir = str(1);
        val = str2double(line{1}(2:end));

        if dir == 'R'
            pos = pos + val;
        else
            pos = pos - val;
        end

        pos = mod(pos, 100);

        if pos == 0
            count = count + 1;
        end

    end

    disp(count)

end



function part1_efficient()

    % read all lines into string array
    lines = readlines("input.txt");

    % remove any empty lines
    lines = lines(lines ~= "");

    % extract directions and values
    dirs = extractBefore(lines, 2); % first letter
    vals = double(extractAfter(lines, 1)); % remaining numbers as double

    changes = -vals; % default left as negative
    isRight = (dirs == 'R'); % find indicies of right moves
    changes(isRight) = vals(isRight);

    % compute position at every step
    path = 50 + cumsum(changes);

    % take mod of every point in path
    path = mod(path, 100);

    % compute number of 0 crosses
    count = sum(path == 0);

    disp(count);

end


function part2()

    % read file
    lines = readlines("input.txt");
    lines = lines(lines ~= "");

    % extract directions and values
    dirs = extractBefore(lines, 2); % first letter
    vals = double(extractAfter(lines, 1)); % remaining numbers as double

    pos = 50;
    count = 0;

    for i = 1:length(dirs)
        if dirs(i) == 'L'
            step = -1;
        else
            step = 1;
        end

        for j = 1:vals(i)
            pos = mod(pos + step, 100);
            if pos == 0
                count = count + 1;
            end
        end

    end

    disp(count);

end


function part2_efficient()

    % read file
    lines = readlines("input.txt");
    lines = lines(lines ~= "");

    % extract directions and values
    dirs = extractBefore(lines, 2); % first letter
    vals = double(extractAfter(lines, 1)); % remaining numbers as double

    % calculate continuous path
    changes = -vals;
    changes(dirs == "R") = vals(dirs == "R");

    % get current path, i.e. position after every move
    current_path = 50 + cumsum(changes);

    % get previous path, i.e. position before every move
    previous_path = [50; current_path(1:end-1)];

    % right moves
    right_mask = changes > 0;
    cross_R = floor(current_path(right_mask)/100) - floor(previous_path(right_mask)/100);

    % left moves
    left_mask = changes < 0;
    cross_L = ceil(current_path(left_mask)/100) - ceil(previous_path(left_mask)/100);

    % count differences
    total_crossings = sum(abs(cross_R)) + sum(abs(cross_L));

    disp(total_crossings);

end