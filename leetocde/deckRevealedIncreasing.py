def deckRevealedIncreasing(deck):
    """
    https://leetcode.com/problems/reveal-cards-in-increasing-order/
    """
    deck.sort()
    curr = [deck[-1]]
    for num in deck[:-1][::-1]:
        curr = [curr[-1]] + curr[:-1]
        curr = [num] + curr
    return curr

print(deckRevealedIncreasing([17,13,11,2,3,5,7]))
