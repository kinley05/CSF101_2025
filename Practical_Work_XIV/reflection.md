## Overview
In this project, I implemented a Binary Search Tree (BST) in Python. \nThe implementation includes core operations such as insertion, searching, traversals (in-order, pre-order, post-order, level-order), deletion, and additional utility methods like finding the maximum value, counting nodes, calculating tree height, and validating the BST property.

## What I Learned
While doing this project, I learned how trees are structured and how the BST rule makes it easy to keep values sorted: values smaller than the root go to the left and larger values go to the right. This simple rule makes searching and inserting much faster compared to searching through a list. I also understood how recursion fits naturally with tree problems since each subtree is itself a smaller tree.

## Challenges
The delete function was the most challenging part. It was not hard to handle when a node had no child or one child, but when a node had two children, I had to replace it with the smallest value from the right subtree. This was tricky at first, but after practicing, I understood it better.

## Future Improvements
