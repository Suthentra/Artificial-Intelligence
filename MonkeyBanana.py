from collections import deque

# Define possible actions
actions = [
    ("Move to Box", lambda s: (s[1], s[1], s[2], s[3]) if s[0] != s[1] else s),
    ("Push Box", lambda s: (s[1], 'under_banana', s[2], s[3]) if s[1] != 'under_banana' else s),
    ("Climb Box", lambda s: (s[0], s[1], True, s[3]) if s[1] == 'under_banana' else s),
    ("Grab Banana", lambda s: (s[0], s[1], s[2], True) if s[2] else s)
]

# BFS function to find the solution
def solve_monkey_problem():
    initial_state = ("corner", "middle", False, False)
    goal_state = (None, None, None, True)  # Has banana

    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        if state[3]:  # Check if monkey has banana
            return path

        for action, transition in actions:
            new_state = transition(state)
            if new_state not in visited:
                queue.append((new_state, path + [action]))

    return None

solution = solve_monkey_problem()
print("Steps to get banana:", solution)
