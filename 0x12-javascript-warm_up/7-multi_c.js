#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
