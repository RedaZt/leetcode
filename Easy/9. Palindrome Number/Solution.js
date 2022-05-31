var isPalindrome = function(x) {
    num = x.toString();
    return num === [...num].reverse().join("");
};