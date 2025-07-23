import sys

def calculate_happiness():
    if len(sys.argv) != 4:
        print("Please provide exactly three strings as command line arguments.")
        return
    like_str = sys.argv[1]
    dislike_str = sys.argv[2]
    given_str = sys.argv[3]
    likes = set(map(int, like_str.split('-')))
    dislikes = set(map(int, dislike_str.split('-')))
    given_numbers = list(map(int, given_str.split('-')))

    happiness = 0

    for num in given_numbers:
        if num in likes:
            happiness += 1
        elif num in dislikes:
            happiness -= 1
        # Otherwise, happiness stays the same

    print("Final happiness:", happiness)
calculate_happiness()
