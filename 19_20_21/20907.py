def solution(left_heap: int, right_heap: int, remaining_moves: int) -> bool | int:
    if left_heap + right_heap >= 81:
        return remaining_moves % 2 == 0
    if remaining_moves == 0:
        return 0

    possible_steps = [
        solution(left_heap + 1, right_heap, remaining_moves - 1),
        solution(left_heap * 2, right_heap, remaining_moves - 1),
        solution(left_heap, right_heap + 1, remaining_moves - 1),
        solution(left_heap, right_heap * 2, remaining_moves - 1),
    ]

    return (
        any(possible_steps) if remaining_moves % 2 != 0 else all(possible_steps)
    )  # Нужно заменить all() на any() чтобы получить ответ на №19.


print(f"19) {[s for s in range(1, 74) if solution(7,s,2)]}")
print(f"20) {[s for s in range(1, 74) if not solution(7,s,1) and solution(7,s,3)]}")
print(f"21) {[s for s in range(1, 74) if not solution(7,s,2) and solution(7,s,4)]}")
