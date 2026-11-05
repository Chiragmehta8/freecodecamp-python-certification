
def hanoi_solver(n):
    rod1 = list(range(n, 0, -1))
    rod2 = []
    rod3 = []

    moves = []

    def record():
        moves.append(f"{rod1} {rod2} {rod3}")

    def move_disks(count, source, auxiliary, destination):
        if count == 1:
            destination.append(source.pop())
            record()
            return

        move_disks(count - 1, source, destination, auxiliary)

        destination.append(source.pop())
        record()

        move_disks(count - 1, auxiliary, source, destination)

    record()

    move_disks(n, rod1, rod2, rod3)

    return "\n".join(moves)
