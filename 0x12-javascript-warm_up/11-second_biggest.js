#!/usr/bin/node
// script that searches the second biggest integer in the list
const args1 = process.argv.slice(2);
const args = args1.map((num) => parseInt(num));
args.sort(function (a, b) { return a - b; });
if (args.length <= 1) {
  console.log(0);
} else {
  console.log(args[args.length - 2]);
}
