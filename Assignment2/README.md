# Assignment 2

Input1.txt - 7 nodes

$ time /usr/local/bin/python3 main.py input.txt 1.5
0.04s user 0.01s system 88% cpu 0.054 total

--

Input2.txt - 1,000 nodes

$ time /usr/local/bin/python3 main.py input.txt 1.5
0.34s user 0.01s system 97% cpu 0.364 total

--

Input3.txt - 10,000 nodes

$ time /usr/local/bin/python3 main.py input.txt 1.5
32.77s user 0.06s system 99% cpu 32.922 total

--

Input4.txt - 100,000 nodes

$ time /usr/local/bin/python3 main.py input.txt 1.5
8903.56s user 51.83s system 69% cpu 3:35:53.08 total

--

Input5.txt - 1,000,000 nodes

Expected to take 600+ hours

--

In order for this to run within a reasonable amount of time, I would suggest using a faster sorting method or being able to use another data structure for comparing chromosome arm positions.

The other thing I noticed is that adding more function calls in Python slows everything down. When I switched to adding more encapsulation, it slowed the entire program down (as expected), however, over the large amount of calls in the 10,000 and 100,000 input files, this added up.