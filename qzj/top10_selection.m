clear;
clc;

csv = importdata('../zjy/direction.csv');

weight = [0.3045; 0.5454; 0.0486; 0.1015];

data = [csv.data(:,2:3), csv.data(:,6:7)];

direction = csv.textdata(2:end,1);

data_weight = data*weight;
% directions = [direction, data_weight];
% select_direction = sortrows(direction,2);
% top10 = select_direction(1:10,1);
