# quiz.py refactor

import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
  "When was the first known use of the word 'quiz'": [
      "1781", "1771","1871", "1881"
  ],
  "Which built in function can get information from the user": [
      "input", "get", "print", "write"
  ],
  "Which Keyword do you use to loop over a given list of elements": [
      "for", "while", "each", "loop"
  ],
  "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
  "What's the name of Python's sorting algorithm": [
        "Timesort", "Quicksort", "Merge sort", "Bubble sort"
    ],
  "What does dict.get(key) return if key isn't found in dict": [
        "None", "key", "True", "False",
    ],
  "What's the official name of the := operator": [
        "Assignment expression",
        "Named expression",
        "Walrus operator",
        "Colon equals operator",
    ],
  "What's one effect of calling random.seed(42)": [
        "The random numbers are reproducible.",
        "The random numbers are more random.",
        "The computer clock is reset.",
        "The first random number is always 42.",
    ],
  "When does __name__ == '__main__' equal True in a Python file": [
        "When the file is run as a script",
        "When the file is imported as a module",
        "When the file has a valid name",
        "When the file only has one function",
    ]
}

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

