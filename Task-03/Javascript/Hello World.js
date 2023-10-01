function Prime(n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 === 0 || n % 3 === 0) return false;
    for (var i = 5; i * i <= n; i += 6) {
        if (n % i === 0 || n % (i + 2) === 0) return false;
    }
    return true;
}
var N = parseInt(prompt("Enter a value for N:"));

if (!isNaN(N)) {
    var result = [];

    for (var i = 1; i <= N; i++) {
        if (Prime(i)) {
            result.push(i);
        }
    }
    console.log("Prime numbers up to " + N + " are: " + result.join(", "));
} else {
    console.log("Invalid input. Please enter a valid number.");
}
