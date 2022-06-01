var plusOne = function(digits) {
    var l = BigInt(digits.map(x=>x.toString()).join("")) + 1n;
    return l.toString().split("");
};