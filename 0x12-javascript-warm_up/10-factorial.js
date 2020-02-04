#!/usr/bin/node
// Script that computes and prints a factorial
const fac = function factorial (x) {
  if (x <= 0) {
    return 1;
  } else {
    return (x * factorial(x - 1));
  }
};
if (parseInt(process.argv[2])) {
  console.log(fac(parseInt(process.argv[2])));
} else {
  console.log(1);
}
