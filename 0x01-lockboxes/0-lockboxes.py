#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    keys = [0]  # Start with the key to the first box
    visited = set(keys)

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                keys.append(key)
                visited.add(key)

    return len(visited) == len(boxes)

# Testing with provided examples
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Expected output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Expected output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Expected output: False
