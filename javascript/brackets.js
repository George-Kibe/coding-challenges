// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.
 

// Example 1:
// Input: s = "()"
// Output: true
// Example 2:
// Input: s = "()[]{}"
// Output: true
// Example 3:
// Input: s = "(]"
// Output: false
// Example 4:
// Input: s = "([])"
// Output: true





(function main() {
    const readline = require("readline");
    const r1 = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
    
    var solution = function(s) {
      const stack = [];
      // Object to map closing brackets to their corresponding opening brackets
      const matchingBracket = {
          ')': '(',
          '}': '{',
          ']': '['
      };
  
      // Iterate over each character in the string
      for (char of s) {
          // If the character is a closing bracket
          if (char in matchingBracket) {
              // Check if stack is not empty and top of stack matches the corresponding opening bracket
              if (stack.length > 0 && stack[stack.length - 1] === matchingBracket[char]) {
                  stack.pop(); // Pop the matched opening bracket from the stack
              } else {
                  return false; // Mismatch found or stack is empty
              }
          } else {
              // If it's an opening bracket, push it onto the stack
              stack.push(char);
          }
      }
  
      // If stack is empty, all brackets matched correctly
      return stack.length === 0;
  
    };
   
    var n, k;
    r1.on("line", (input) => {
      n = input;
    }).on("close", () => {
      console.log(solution(n));
    });
  })();
  