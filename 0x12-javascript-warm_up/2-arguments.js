#!/usr/bin/node
// Script that verificated if pass arguments
const args = process.argv.slice(2);
if(args.length !== 0){
  console.log('Argument found');
} else {
  console.log('No argument');
}
