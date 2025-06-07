"""Monotonic stacks are generally used for solving questions of the type - next greater element, next smaller element, previous 
greater element and previous smaller element. We are going to create a template for each of the format, and then use them to 
solve variety of problems. To keep things simple, while traversing through an array, we always go from left to right. 

What is monotonic stack?
There could be four types of monotonic stacks. Please read them carefully, we'll refer to these types at multiple places in the 
sections below.

Strictly increasing - every element of the stack is strictly greater than the previous element. Example - [1, 4, 5, 8, 9]
Non-decreasing - every element of the stack is greater than or equal to the previous element. Example - [1, 4, 5, 5, 8, 9, 9]
Strictly decreasing - every element of the stack is strictly smaller than the previous element - [9, 8, 5, 4, 1]
Non-increasing - every element of the stack is smaller than or equal to the previous element. - [9, 9, 8, 5, 5, 4, 1]
We also assume that the right most element is at the top of the stack and left most element is at the bottom of the stack.

A generic template
We can use the following template to build a stack that keep the monotonous property alive through the execution of the program. 

function buildMonoStack(arr) {
  // initialize an empty stack
  stack = [];
  
  // iterate through all the elements in the array
  for (i = 0 to arr.length - 1)) {
    while (stack is not empty && element represented by stack top `OPERATOR` arr[i]) {
      // if the previous condition is satisfied, we pop the top element
      let stackTop = stack.pop();
  
      // do something with stackTop here e.g.
      // nextGreater[stackTop] = i
    }
  
    if (stack.length) {
      // if stack has some elements left
      // do something with stack top here e.g.
      // previousGreater[i] = stack.at(-1)
    }

    // at the ened, we push the current index into the stack
     stack.push(i);
  }
  
  // At all points in time, the stack maintains its monotonic property
}
Notes about the template above
- We initialize an empty stack at the beginning.
- The stack contains the index of items in the array, not the items themselves
- There is an outer for loop and inner while loop.
- At the beginning of the program, the stack is empty, so we don't enter the while loop at first.
- The earliest we can enter the while loop body is during the second iteration of for loop. That's when there is at least an 
item in the stack.
- At the end of the while loop, the index of the current element is pushed into the stack
- The OPERATOR inside the while loop condition decides what type of monotonic stack are we creating.
- The OPERATOR could be any of the four  >, >=, <, <=

Time complexity - It can be argued that no element is accessed more than four times (a constant) - one, when comparing its value 
with the item on the stack (while conditional). two, when pushing the item onto the stack. three, when comparing this item on the 
stack with the current item being iterated (while conditional again). four, when popping the item out of stack. As a result, the 
time complexity of this algorithm is linear. - O(n) where n is the number of elements in the array.

Space complexity - Because we are using an external data structure - stack. In the worst can it can be filled with all the 
elements in the array. The space complexity is also linear. - O(n) where n is the number of elements in the array.

In our implementation, finding next greater and previous greater elements require building a monotone decreasing stack. For finding 
next smaller and previous smaller requires building a monotone increasing stack. To help you remember this, think of this as an 
inverse relation - greater requires decreasing, smaller requires increasing stacks.

1. Next Greater
Let's start with this example. We are given with the following array and we need to find the next greater elements for each of 
items of the array. arr = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]

Next greater elements (what is the next greater element for the item at this index) -
nextGreaterElements = [null, 9, 5, 9, 5, 9, 12, 12, 12, null]

On the place of writing the element itself, we can also write its index -
nextGreaterIndexes = [-1, 6, 3, 6, 5, 6, 9, 9, 9, -1] (for 13 and 12, because there are no greater elements after themselves, 
we use -1, an invalid index value of the next greater element. You could use null or arr.length as well. 13 is the greatest 
number in the array, and 12 is the last element in the array and as such there is nothing greater than 13 and nothing comes
after 12 so both get -1 or null.

Let's use the template given above to solve this question. The following code uses the template and implement next greater 
element program. Please read the comments in the code to understand what we are doing on these lines.


function findNextGreaterIndexes(arr) {
  // initialize an empty stack
  let stack = [];
  
  // initialize nextGreater array, this array hold the output
  // initialize all the elements are -1 (invalid value)
  let nextGreater = new Array(arr.length).fill(-1);
  
  // iterate through all the elements of the array
  for (let i = 0; i < arr.length; i++) {
  
    // while loop runs until the stack is not empty AND
    // the element represented by stack top is STRICTLY SMALLER than the current element
    // This means, the stack will always be monotonic non increasing (type 4)
    while (stack.length && arr[stack.at(-1)] < arr[i]) {
    
      // pop out the top of the stack, it represents the index of the item
      let stackTop = stack.pop();
      
      // as given in the condition of the while loop above,
      // nextGreater element of stackTop is the element at index i
      nextGreater[stackTop] = i;
    }
    
    // push the current element
    stack.push(i);
  }
  return nextGreater;
}

Notes
- For finding next greater elements (not equal) we use a monotonic non increasing stack (type 4) since stack can have equal values
- If the question was to find next greater or equal elements, then we would have used a monotonic strictly decreasing 
stack (type 3), since the stack only contains distinct values
- We use the operator < in while loop condition above - this results in a monotonic non increasing stack (type 4). If we use 
<= operator, then this becomes a monotonic strictly decreasing stack (type 3). This means in the first case if we come across an
equal value, we append to the stack without popping. In the second case, if we come across an equal value, we pop from the stack.

Time and space complexity - O(n) - When we find that the current peek element of the stack is less than the current loop element
we know that we have found the peek element's next greater value, so we pop it and update its index in the result array with the
current loop element before adding the current loop element to the top of the stack.


2. Previous Greater
This time we want to find the previous greater elements. One option is to iterate from arr.length - 1 to 0 and use the same logic as 
above in the opposite direction. In order to keep things simple, I rather like another flavour of the template above where we add 
three more lines after the while loop to get the previous greater element. Let's see how to do that.

arr = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]

Previous greater elements -
previousGreaterElements = [null, 13, 8, 8, 5, 8, 13, 9, 7, 13]
nextGreaterIndexes = [-1, 0, 1, 1, 3, 1, 0, 6, 7, 0]


function findPreviousGreaterIndexes(arr) {
  // initialize an empty stack
  let stack = [];
  
  // initialize previousGreater array, this array hold the output
  // initialize all the elements are -1 (invalid value)
  let previousGreater = new Array(arr.length).fill(-1);
  
  // iterate through all the elements of the array
  for (let i = 0; i < arr.length; i++) {
  
     // while loop runs until the stack is not empty AND
     // the element represented by stack top is SMALLER OR EQUAL to the current element
     // This means, the stack will always be strictly decreasing (type 3) - because elements are popped when they are equal
     // so equal elements will never stay in the stack (definition of strictly decreasing stack)
    while (stack.length && arr[stack.at(-1)] <= arr[i]) {
    
      // pop out the top of the stack, it represents the index of the item
      let stackTop = stack.pop();
    }
    
    // after the while loop, only the elements which are greater than the current element are left in stack
    // this means we can confidentally decide the previous greater element of the current element i, that's stack top
    if (stack.length) {
      previousGreater[i] = stack.at(-1);
    }
    
    // push the current element
    stack.push(i);
  }
  return previousGreater;
}

Notes
- For finding previous greater elements (not equal) we use a monotonic strictly decreasing stack (type 3)
- If the question was to find previous greater or equal elements, then we would have used a monotonic non increasing stack (type 4) 
- We use the operator <= in while loop condition above - this results in a monotonic strictly decreasing stack (type 3). If we use 
< operator, then this becomes a monotonic non increasing stack (type 4).

Time and space complexity - O(n) . This is because for each current loop element we pop all previous values that are less than or equal, 
leaving the previous greater element of the current loop element as the stack peek value. 


3. Next Greater and Previous Greater at the same time
If we merge the code from heading (1) and (2) both above, we can get next greater and previous greater from the same program. There is 
only one limitation. One of previousGreater or nextGreater won't be strictly greater (but greater or equal). If this satisfies our 
requirement, we can use the following solution.

For example, in the array [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]
The next greater element for the first 5 will be 9, the previous greater element for the second 5 will be 5 (not 8)
OR
The next greater element for the first 5 will be 5 (not 9), the previous greater element for the second 5 will be 8.

This solution works if you are okay with one of the two cases above. Let's look at the code now.

function findNextAndPreviousGreaterIndexes(arr) {
  // initialize an empty stack
  let stack = [];
  
  // initialize previousGreater and nextGreater arrays
  let previousGreater = new Array(arr.length).fill(-1);
  let nextGreater = new Array(arr.length).fill(-1);
  
  // iterate through all the elements of the array
  for (let i = 0; i < arr.length; i++) {
  
     // while loop runs until the stack is not empty AND
     // the element represented by stack top is SMALLER OR EQUAL to the current element
     // This means, the stack will always be strictly decreasing (type 3) - because elements are popped when they are equal
     // so equal elements will never stay in the stack (definition of strictly decreasing stack)
    while (stack.length && arr[stack.at(-1)] <= arr[i]) {
    
      // pop out the top of the stack, it represents the index of the item
      let stackTop = stack.pop();
      
      // This is the only additional line added to the last approach
      // decides the next greater element for the index popped out from stack
      nextGreater[stackTop] = i;
    }
    
    // after the while loop, only the elements which are greater than the current element are left in stack
    // this means we can confidentally decide the previous greater element of the current element i, that's stack top
    if (stack.length) {
      previousGreater[i] = stack.at(-1);
    }
    
    // push the current element
    stack.push(i);
  }
  return [previousGreater, nextGreater];
}

Note: In the code example given above, the nextGreater array points at next greater or equal element. While previousGreater array 
points at strictly greater elements in the leftward direction (previous strictly greater).



4. Next Smaller (strictly smaller)
If you have were able to understand the logic until this point, finding next smaller and previous smaller shouldn't be difficult at 
all. To get next smaller element we take the next greater element code and simply flip the operator from < to >. To get previous 
smaller elements we take the previous greater element code and simply flip the operator from <= to >=. By doing this we end up 
creating a non-decreasing (type 2) array for the next smaller element and a strictly increasing (type 1) for the previous smaller 
element. Given that I've already explained the corresponding cases for next greater and previous greater elements, let me directly 
show you code examples below.


function findNextSmallerIndexes(arr) {
  // initialize an empty stack
  let stack = [];
  
  // initialize nextGreater array, this array hold the output
  // initialize all the elements are -1 (invalid value)
  let nextSmaller = new Array(arr.length).fill(-1);
  
  // iterate through all the elements of the array
  for (let i = 0; i < arr.length; i++) {
  
    // while loop runs until the stack is not empty AND
    // the element represented by stack top is STRICTLY LARGER than the current element
    // This means, the stack will always be monotonic non decreasing (type 2)
    while (stack.length && arr[stack.at(-1)] > arr[i]) {
    
      // pop out the top of the stack, it represents the index of the item
      let stackTop = stack.pop();
      
      // as given in the condition of the while loop above,
      // nextSmaller element of stackTop is the element at index i
      nextSmaller[stackTop] = i;
    }
    
    // push the current element
    stack.push(i);
  }
  return nextSmaller;
}

5. Previous Smaller (strictly smaller)

function findPreviousSmallerIndexes(arr) {
  // initialize an empty stack
  let stack = [];
  
  // initialize previousSmaller array, this array hold the output
  // initialize all the elements are -1 (invalid value)
  let previousSmaller = new Array(arr.length).fill(-1);
  
  // iterate through all the elements of the array
  for (let i = 0; i < arr.length; i++) {
  
    // while loop runs until the stack is not empty AND
    // the element represented by stack top is LARGER OR EQUAL to the current element
    // This means, the stack will always be monotonic strictly increasing (type 1)
    while (stack.length && arr[stack.at(-1)] >= arr[i]) {
    
      // pop out the top of the stack, it represents the index of the item
      let stackTop = stack.pop();
    }
    
    // this is the additional bit here
    if (stack.length) {
      // the index at the stack top refers to the previous smaller element for `i`th index
      previousSmaller[i] = stack.at(-1);
    }
    
    // push the current element
    stack.push(i);
  }
  return previousSmaller;
}

6. Next Smaller and Previous Smaller (merged, one strictly smaller, and the other smaller or equal)

function findNextSmallerIndexes(arr) {
  // initialize an empty stack
  let stack = [];
  
  // initialize previousSmaller array, this array hold the output
  // initialize all the elements are -1 (invalid value)
  let previousSmaller = new Array(arr.length).fill(-1);
  
  // iterate through all the elements of the array
  for (let i = 0; i < arr.length; i++) {
  
    // while loop runs until the stack is not empty AND
    // the element represented by stack top is LARGER OR EQUAL to the current element
    // This means, the stack will always be monotonic strictly increasing (type 1)
    while (stack.length && arr[stack.at(-1)] >= arr[i]) {
    
      // pop out the top of the stack, it represents the index of the item
      let stackTop = stack.pop();
      
      // as given in the condition of the while loop above,
      // nextSmaller element of stackTop is the element at index i
      nextSmaller[stackTop] = i;
    }
    
    // this is the additional bit here
    if (stack.length) {
      // the index at the stack top refers to the previous smaller element for `i`th index
      previousSmaller[i] = stack.at(-1);
    }
    
    // push the current element
    stack.push(i);
  }
  return [nextSmaller, previousSmaller];
}

Summary
Let's summarize all the approaches here, to cement our learning.

Problem	            Stack Type	                        Operator in while loop	        Assignment Position
next greater	      non-increasing (equal allowed)	      stackTop < current	            inside while loop
previous greater	  strictly decreasing                   stackTop <= current	            outside while loop
next/prev greater   strictly decreasing                   stackTop <= current             inside/outside loop
next smaller	      non-decreasing (equal allowed)	      stackTop > current	            inside while loop
previous smaller	  strictly increasing                   stackTop >= current	            outside while loop

"""

def previousGreater(nums):
  stack = []
  previous = [-1]*len(nums)

  for i in reversed(range(len(nums))):
    while stack and nums[stack[-1]] < nums[i]:
      stackTop = stack.pop()
      previous[stackTop] = i
    stack.append(i)
  return previous



def nextPrevGreater(nums):
  stack = []
  nextG = [-1]*len(nums)
  prevG = [-1]*len(nums)

  for i in range(len(nums)):
    
    while stack and nums[stack[-1]] <= nums[i]:
      nextG[stack.pop()] = i

    if stack:
        prevG[i] = stack[-1]

    stack.append(i)

  return [nextG, prevG]


arr = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]
print(nextPrevGreater(arr))
