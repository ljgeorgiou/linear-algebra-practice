# linear-algebra-practice
What does add do?
Add works by going through two lists together, position by position. It takes the items at the same position in each list, adds them, and appends the result to a new list. It repeats this for every position, then returns the new list of sums. For this to work, both lists must be the same size.

What does dot product do?
Dot product works by going through two lists together, position by position. It takes the items at the same position in each list, multiplies them and adds that result to a running total. It repeats this for every position, then returns the total, which is the sum of every multiplication. For this to work, both lists must be the same size.

What does matrix times vector do?
Matrix times vector takes in a matrix (a list containing lists of integers) and a vector (a list of integers). It performs the dot product of the first row of the matrix with the vector and appends that result to a new list. It then repeats this for every row of the matrix, and returns the new list. For this to work, the number of columns in the matrix must equal the size of the vector.

My reflection on why NumPy exists:
NumPy exists to make working with data shaped like vectors and matrices much faster and simpler. Instead of writing a function every time you need to add vectors, take a dot product, or multiply matrices, NumPy has these built in. Each one becomes a single operation (+, np.dot, @) instead of several lines of looping.

My hand-written loops are fine for three numbers, but if each vector held a million numbers, a plain Python loop would be extremely slow, while NumPy handles it almost instantly. 

The benefit of building it from scratch allows you to see what is going on behind the scenes, but once you understand that, using NumPy lets you do the same work more efficiently with far less code.