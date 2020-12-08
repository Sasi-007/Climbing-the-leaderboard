#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    rankings = createRankings(ranked)
    i = len(ranked) - 1
    for score in player:
        flag = True
        while flag:
            if i == -1:
                print(1)
                flag = False
            elif score < ranked[i]:
                print(rankings[i] + 1)
                flag = False
            elif score == ranked[i]:
                print(rankings[i])
                flag = False
            elif score > ranked[i]:
                i -= 1
    return


def createRankings(ranked):
    rankings = [1]
    rank = 1
    for i in range(1, len(ranked)):
        if ranked[i] < ranked[i - 1]:
            rank += 1
        rankings.append(rank)
    return rankings

lenOfLeaderboard = int(input())
ranked = list(map(int, input().rstrip().split()))
lenOfAliceScores = int(input())
player = list(map(int, input().rstrip().split()))
climbingLeaderboard(ranked, player)
