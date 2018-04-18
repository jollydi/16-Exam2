"""
Exam 2, problem 1.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Isaiah Jolly.  April 2018.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1()


###############################################################################
# DONE: 2.  READ the code of the  Rect  class below.
#
#   Once you are confident that you understand the  Rect  class and its code,
#   change the TO-DO for this problem to DONE.
#
#   If you do NOT understand the  Rect  class and its code,
#   talk to your instructor to see how to proceed.
###############################################################################
class Rect(object):
    def __init__(self, width, height):
        self.w = width
        self.h = height


def run_test_problem1():
    """ Tests the   problem1   function. """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement at least 2 tests of the  problem1  function.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1   function:')
    print('--------------------------------------------------')

    # Test 1:
    rect1 = Rect(3, 2)
    rect2 = Rect(5, 12)
    expected = 66
    actual = problem1([rect1, rect2])
    print('Test 1 Expected:', expected)
    print('  Test 1 Actual:', actual)

    # Test 2:
    rect1 = Rect(3, 2)
    rect2 = Rect(5, 12)
    rect3 = Rect(14, 2)
    rect4 = Rect(9, 3)
    expected = 121
    actual = problem1([rect1, rect2, rect3, rect4])
    print('Test 2 Expected:', expected)
    print('  Test 2 Actual:', actual)


def problem1(rectangles):
    """
    What comes in:  A sequence of  Rect  objects.
    What goes out:  Returns the sum of the areas of the given  Rect  objects.
    Side effects:   None.
    Example:
      problem1([Rect(5, 10),
                Rect(4, 3),
                Rect(100, 7)]
         returns 50 + 12 + 700, which is 762

    Type hints:
    :param rectangles: [Rect]
    :return: int
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # -------------------------------------------------------------------------

    total = 0
    for k in range(len(rectangles)):
        area = rectangles[k].w * rectangles[k].h
        total = total + area
    return total


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()