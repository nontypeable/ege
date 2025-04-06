def solution(heap: int, remaining_moves: int) -> bool | int:
    if heap <= 19:
        return remaining_moves % 2 == 0
    if remaining_moves == 0:
        return 0

    possible_steps = [
        solution(heap - 5, remaining_moves - 1),
    ]

    if heap % 2 == 0:
        possible_steps.append(solution(heap // 2, remaining_moves - 1))
    if heap % 3 == 0:
        possible_steps.append(solution(heap // 3, remaining_moves - 1))
    if heap % 2 == 1 and heap % 3 != 0:
        possible_steps.append(solution(heap + 1, remaining_moves - 1))

    return any(possible_steps) if remaining_moves % 2 != 0 else all(possible_steps)


print(f"19) {[s for s in range(20, 100) if not solution(s,1) and solution(s, 2)]}")
print(f"20) {[s for s in range(20, 100) if not solution(s,1) and solution(s, 3)]}")
print(
    f"21) {[s for s in range(20,100) if not solution(s,2) and solution(s,4)]}"
)
