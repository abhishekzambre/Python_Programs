def compute_tower_hanoi(num_rings):
    def computer_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:

            computer_tower_hanoi_steps(num_rings_to_move-1, from_peg, use_peg, to_peg)

            pegs[to_peg].append(pegs[from_peg].pop())

            print("Move from peg", from_peg, "to peg", to_peg)

            computer_tower_hanoi_steps(num_rings_to_move-1, use_peg, to_peg, from_peg)

    NUM_PEGS = 3
    pegs = [list(reversed(range(1, num_rings +1)))] + [[] for _ in range(1, NUM_PEGS)]

    computer_tower_hanoi_steps(num_rings, 0, 1, 2)


compute_tower_hanoi(3)
