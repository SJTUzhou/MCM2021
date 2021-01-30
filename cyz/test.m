a = [3,24,49,59,21,38,110,5,19,12,11,33,45,22,57,53,140,30,149,20,20,85,68,41,26,9,51,123,122,49,35,5];
b = [2188,2914,2693,2713,2530,2667,2672,2712,2173,2935,2913,2917,2490,2758,2929,3108,2872,2520,2706,3175,2974,2981,2937,2967,2912,2774,3059,2942,2901,2604,2695,3020];


%a = (a-mean(a))/std(a);
%b = (b-mean(b))/std(b);
%r = corrcoef(a,b);

[ab, lags_ab] = xcorr(a, b);
subplot(1,3,1);
stem(lags_ab,ab);
title("xcorr");

[aa, lags_aa] = xcorr(a);
subplot(1,3,2);
stem(lags_aa,aa);
title("macro market: num of containers");

[bb, lags_bb] = xcorr(b);
subplot(1,3,3);
stem(lags_bb,bb);
title("daily freight rate");
%%
data = readmatrix("./钦州_宁波.csv");
amt = data(:,4);
volume = data(:,5);
log_amt = log10(amt);
log_volume = log10(volume);
