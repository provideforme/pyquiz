# quiz.py 

from string import ascii_lowercase

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
    ]
}

num_correct = 0
for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    answer_label = input(f"\nChoice? ")
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        num_correct += 1
        print("⭐ Correct! ⭐")
    else:
      print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")