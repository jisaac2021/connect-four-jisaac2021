def longest_streak(input_string):
    """
    Return the longest streak <int> of repeated characters in `input_string`
    """

    char = input_string[0]
    streak = 1
    longest = 0

    for ch in input_string[1:]:

        if ch == char:
            streak += 1

        else:
            streak = 1
            char = ch

        if streak > longest:
            longest = streak

    return longest
