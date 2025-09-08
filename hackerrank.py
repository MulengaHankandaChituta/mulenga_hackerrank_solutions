# HackerRank Runner-Up Score Problem Solution
# Author: Mulenga Chituta

if __name__ == '__main__':
    n = int(input("Enter number of scores: "))  # total number of scores
    arr = list(map(int, input("Enter the scores separated by spaces: ").split()))

    # Get unique scores, sort in descending order
    unique_scores = sorted(set(arr), reverse=True)

    if len(unique_scores) > 1:
        print("Runner-up score:", unique_scores[1])
    else:
        print("No runner-up score available (all scores are the same).")
