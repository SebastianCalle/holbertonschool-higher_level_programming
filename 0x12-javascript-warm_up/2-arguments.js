#!/usr/bin/node
// Script that verificated if pass arguments
const args = process.argv.slice(2);
if (args.length === 1) {
  console.log('Argument found');
} else if (args.length > 1) {
    console.log('Arguments found');
} else {
  console.log('No argument');
}
