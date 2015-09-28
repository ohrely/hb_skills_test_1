"""Skills Assessment: Lists.

To work on an item, uncomment the entire function (including the docstring)
and then run this script. It should output an error that the newly-uncommented
function is now failing its tests.

Edit the function body until you have a solution and the test passes, and then
move on to the next function.

This assessment is DUE TO YOUR ADVISOR BY SUNDAY EVENING.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

    >>> all_odd([1, 2, 7, -5])
    [1, 7, -5]

    >>> all_odd([2, -6, 8])
    []

    """

    odd_list = []

    for integer in number_list:
        if integer % 2 == 1:
            odd_list.append(integer)

    return odd_list


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    even_list = []

    for integer in number_list:
        if integer % 2 == 0:
            even_list.append(integer)

    return even_list


def print_indeces(my_list):
    """Print the index of each list item, followed by the item itself.
    Do this without using a counting variable. I.e. don't do something
    like this:

    count = 0
    for item in list:
        print count
        count = count + 1

    Output should look like this:

    >>> print_indeces(["Toyota", "Jeep", "Volvo"])
    0 Toyota
    1 Jeep
    2 Volvo

    """

    # failed effort 1:
    # test_list = enumerate(my_list)
    # print (test_list)

    word_index = ""
    for word in my_list:
        word_index = my_list.index(word)
        print ("{} {}".format(word_index, word))

    #  failed effort 2:
    # def enum(some_list):
    #     enum_list = []
    #     for item in enumerate(some_list):
    #         enum_list.add(item)

    # my_enum_list = enum(my_list)
    # print (my_enum_list)


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    long_list = []

    for word in word_list:
        if len(word) > 4:
            long_list.append(word)

    return long_list


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

        >>> smallest_int([-5, 2, -5, 7])
        -5

    If the input list is empty, return None:

        >>> smallest_int([]) is None
        True

    """
    if len(number_list) is 0:
        smallest = None
    else:
        smallest = number_list[0]
        for num in number_list:
            if num < smallest:
                smallest = num
            else:
                pass

    # another solution:
    # smallest = 2147483647
    # for int in number_list:
    #     if int < smallest:
    #         smallest = int
    #     else:
    #         pass

    return smallest


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

        >>> largest_int([-5, 2, -5, 7])
        7

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    if len(number_list) is 0:
        largest = None
    else:
        largest = number_list[0]
        for num in number_list:
            if num > largest:
                largest = num
            else:
                pass

    return largest


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """

    half_list = []
    for orig_num in number_list:
        half_num = float(orig_num) / 2
        half_list.append(half_num)

    return half_list


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """

    length_list = []
    for word in word_list:
        length_list.append(len(word))

    return length_list


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """

    list_sum = 0
    for number in number_list:
        list_sum += number

    return list_sum


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """

    list_product = 1
    for number in number_list:
        list_product *= number

    return list_product


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python ha a built-in method on lists, `join` -- but this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """

    combo_string = ""
    for word in word_list:
        combo_string += word

    return combo_string


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    list_sum = 0
    for number in number_list:
        list_sum += number

    list_mean = float(list_sum) / len(number_list)

    return list_mean


#############################################################################
# END OF SKILLS TEST: You can stop here, or read on to work on advanced problem.

# Uncomment the function below to work on the advanced problem.
# Tip: To comment or uncomment blocks of code, highlight what you want to
#    comment or uncomment, and then CMD+"/" or CTRL-"/"

def advanced_join_strings(list_of_words):
    """Return a single string with each word from the input list
    separated by a comma.

        >>> advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> advanced_join_strings(["Pretzel"])
        'Pretzel'

    """
    combo_string = list_of_words[0]
    for word in list_of_words[1:]:
        combo_string += ", {}".format(word)

    return combo_string

# END OF ASSIGNMENT: You can ignore everything below.
##############################################################################

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print ("*** %s TESTS PASSED. GOOD WORK!" % result.attempted)
    print
