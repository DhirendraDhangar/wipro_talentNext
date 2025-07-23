from collections import Counter

def get_meeting_details(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    n_lines = len(lines)
    if n_lines > 12:
        hour = n_lines % 12
        hour = 12 if hour == 0 else hour  # 12 instead of 0
        meeting_time = f"{hour} PM"
    else:
        meeting_time = f"{n_lines} AM"
    full_text = ' '.join(lines).lower()
    words = full_text.split()
    word_freq = Counter(words)
    meeting_place = word_freq.most_common(1)[0][0]
    meeting_place = f"{meeting_place.capitalize()} Street"

    print("Meeting time:", meeting_time)
    print("Meeting place:", meeting_place)
get_meeting_details("Sample.txt")
