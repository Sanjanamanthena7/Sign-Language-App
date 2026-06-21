def fingers_up(hand):
    thumb = hand[4].x > hand[3].x

    index = hand[8].y < hand[6].y
    middle = hand[12].y < hand[10].y
    ring = hand[16].y < hand[14].y
    pinky = hand[20].y < hand[18].y

    return [thumb, index, middle, ring, pinky]


def detect_gesture(hand):

    fingers = fingers_up(hand)

    if fingers == [False, False, False, False, False]:
        return "FIST"

    elif fingers == [True, True, True, True, True]:
        return "FIVE"

    elif fingers == [False, True, False, False, False]:
        return "ONE"

    elif fingers == [False, True, True, False, False]:
        return "VICTORY"

    elif fingers == [True, False, False, False, False]:
        return "THUMBS UP"

    elif fingers == [True, True, False, False, True]:
        return "LOVE YOU"

    elif fingers == [True, True, False, False, False]:
        return "L"

    return "UNKNOWN"