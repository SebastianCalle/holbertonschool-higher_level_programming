#!/usr/bin/node
// Script that verificated if pass arguments
const args = process.argv.slice(2);
if (args) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
