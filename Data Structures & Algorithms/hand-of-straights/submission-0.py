from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        n = len(hand)

        if n % groupSize != 0:
            return False

        count = Counter(hand)

        for card in sorted(count):
            while count[card] > 0:
                for nxt in range(card, card + groupSize):
                    if count[nxt] == 0:
                        return False
                    count[nxt] -= 1

        return True