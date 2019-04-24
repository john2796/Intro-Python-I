# Stretch Goals

# 1.[] One of Python's main philosophical tenets is its emphasis on readability. To
# that end, the Python community has standardized around a style guide called
# [PEP 8](https://www.python.org/dev/peps/pep-0008/). Take a look at it and
# then go over the code you've written and make sure it adheres to what PEP 8
# recommends. Alternatively, PEP 8 linters exist for most code editors (you can
# find instructions on installing a Python linter for VSCode
# [here](https://code.visualstudio.com/docs/python/linting)). Try installing
# one for your editor!


# 2. .[] Rewrite code challenges you've solved before or projects you've implemented
#    before in a different language in Python. Start getting in as much practice
#    with the language as possible!
strArr = ['sssssssssshortssssssssssshorts',
          'really, really longs!', 'mediumaaaaaaaa']
print(max(strArr, key=len))
# --------------------- Longest Str JS version------------------------
# function longestString(arr) {
#   const longest = arr.reduce(function (a, b) { return a.length >= b.length ? a : b });
#   return longest
# }
# const strings1 = ['short', 'really, really long!', 'medium'];
# console.log(longestString(strings1)); // <--- 'really, really long!'


# 3.[] Write a program to determine if a number, given on the command line, is prime.

# 1.  How can you optimize this program?
# 2.  Implement [The Sieve of
#     Erathosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
#     of the oldest algorithms known (ca. 200 BC).

def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


isPrime(6)
