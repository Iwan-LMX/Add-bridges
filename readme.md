# Project Overview
This project implements an algorithm to find and add bridges in a graph, which is a crucial aspect of understanding the graph’s structure and connectivity. It is part of Homework 1 for the CS3411 course at UNSW. The task involves identifying bridges that, when removed, increase the number of connected components in the graph.

# How to Use
## Requirements
- Ensure you have a C compiler (like gcc) installed on your system.

## Compilation
To compile the code, run the following command:

```bash
Copy code
gcc -o add_bridges add_bridges.c
```
## Running the Program
After compiling, you can run the program as follows:

```bash
Copy code
./add_bridges < input.txt
```
Where `input.txt` is a file containing the graph’s representation.

### Input Format
The input should consist of the number of vertices and edges, followed by the list of edges.

```
5 5
1 2
1 3
3 4
2 4
2 5
```
### Output
The program will output the edges identified as bridges in the graph.

## Features
- Efficient graph traversal using DFS (Depth-First Search).
- Bridge detection based on low-link values and discovery times.

### Example
Input:
```
5 5
1 2
1 3
3 4
2 4
2 5
```
Output:

```
2 5
```
This output indicates that removing the edge (2, 5) will split the graph into disconnected components.
