#!/usr/bin/node
// Script that verificated if pass arguments
if(process.argv){
	console.log(process.argv[2]);
} else {
	console.log('No argument');
}
