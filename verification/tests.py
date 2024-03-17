"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [8, 4],
            "answer": [5, 4, 6, 1, 3, 8, 7, 2],
        },
        {
            "input": [7, 11],
            "answer": [7, 2, 3, 1, 5, 6, 4],
        },
        {
            "input": [3, 1],
            "answer": [1, 2, 3],
        },
    ],
    "Extra": [
        {
            "input": [15, 4],
            "answer": [4, 7, 12, 1, 11, 5, 13, 2, 8, 10, 6, 3, 15, 14, 9],
        },
        {
            "input": [3, 5],
            "answer": [3, 1, 2],
        },
        {
            "input": [12, 12],
            "answer": [2, 11, 3, 10, 7, 4, 6, 9, 8, 5, 12, 1],
        },
        {
            "input": [13, 11],
            "answer": [12, 10, 6, 13, 8, 9, 7, 3, 2, 4, 1, 11, 5],
        },
        {
            "input": [1, 1],
            "answer": [1],
        },
    ]
}
