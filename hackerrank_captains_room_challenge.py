# hackerrank_captains_room_idlegood.py
def main():
    try:
        k = int(input().strip())                  # group size
    except Exception:
        return                                    # no input in IDLE
    rooms = list(map(int, input().strip().split()))
    captain = (k * sum(set(rooms)) - sum(rooms)) // (k - 1)
    print(captain)

if __name__ == "__main__":
    main()
