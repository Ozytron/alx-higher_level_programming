#!/usr/bin/node
function add (num1, num2) {
    return num1 + num2;
}
  
console.log(add(Number(process.argv[2]), Number(process.argv[3])));