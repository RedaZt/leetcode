var trailingZeroes = function(n) {
    var c = 0;
    while (n) {
        n = Math.floor(n/5);
        c+=n;
    }
    return c;
};