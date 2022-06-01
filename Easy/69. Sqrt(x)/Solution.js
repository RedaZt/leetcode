var mySqrt = function(x) {
    var res = 0;
    while (Math.pow(res, 2) <= x)
        res++;
    return res - 1;
};