"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
# ----------solution one -------------
with open('foo.txt', 'r') as f:  # content way of reading it auto close file
    for line in f:
        print(line, end="")
f_contents = f.read(100)  # arg how many file you want
print(f_contents)

# ----------solution two -------------
with open('foo.txt', 'r') as f:  # content way of reading it auto close file
    size_to_read = 100
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end="")
        f_contents = f.read(size_to_read)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# ----------solution  -------------

with open("bar.txt", "w") as f:
    print(f.write(" Write three lines of arbitrary content to that file,"))
    print(f.write(" Write three lines of arbitrary content to that file,"))
    print(f.write(" Write three lines of arbitrary content to that file,"))
