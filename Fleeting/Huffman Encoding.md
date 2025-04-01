20250328144246

Tags:

Huffman encoding is a scheme that takes symbols and produces a codeword for whatever the symbol represents based on their frequency.

## Encoding Scheme
The codeword for a symbol in a Huffman encoding scheme is related to the frequency that symbol occurs. The frequency of the symbols occurring will split the symbols along a binary tree. 

| Symbol | Frequency |
| ------ | --------- |
| A      | 70        |
| B      | 3         |
| C      | 20        |
| D      | 37        |
For the above table, the tree representation would look like the following. 
![[Pasted image 20250328145056.png|800]]

## Procedure
The procedure for a Huffman encoding starts with sorting the table first. Then, take the first two, or lowest 2, symbols, put the lower on the left and the greater on the right, and their parent node will be the sum of the two nodes. Take the second 2, and do the same thing. They both are placed back on the table as an internal node. with their frequency being the sum. An example table will be the following

| Symbol | Frequency |
| ------ | --------- |
| A      | 5         |
| B      | 9         |
| C      | 12        |
| D      | 13        |
| E      | 16        |
| F      | 45        |
A and B will be grouped together and C and D will be grouped together as well

| Symbol | Frequency |
| ------ | --------- |
| A + B  | 14        |
| E      | 16        |
| C + D  | 25        |
| F      | 45        |
E and A + B will be grouped together, and this forms the tree
![[Pasted image 20250329113654.png|800]]

| Symbol    | Frequency |
| --------- | --------- |
| C + D     | 25        |
| A + B + E | 30        |
| F         | 45        |
Group the bottom two again

| Symbol            | Frequency |
| ----------------- | --------- |
| F                 | 45        |
| A + B + C + D + E | 55        |

![[Pasted image 20250329113925.png|800]]
Group them all together to form
![[Pasted image 20250329113948.png|800]]
And then, from this, label the edges with zeros for left and ones for right, to form the Huffman encoding. 

| Symbol | Frequency |
| ------ | --------- |
| F      | 0         |
| C      | 100       |
| D      | 101       |
| A      | 1100      |
| B      | 1101      |
| E      | 111       |

## Runtime Complexity
The time complexity of Huffman encoding is $O(n\log(n))$, where $n$ is the number of unique characters in sequence. 
___
# References
