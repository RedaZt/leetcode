var reverse = function (x) {
    s = +[...Math.abs(x).toString()].reverse().join('');
    if (s > Math.pow(2, 31)) 
        s=0;
    return x > 0 ? s : -s;
};