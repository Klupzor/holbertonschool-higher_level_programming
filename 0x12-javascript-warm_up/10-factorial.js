#!/usr/bin/node
function factorial (num) {
  if (num > 1) {
    return factorial(num - 1) * num;
  } else { return 1; }
}
const num = parseInt(process.argv[2]);
console.log(factorial(num));
