class SnapshotArray:

    def __init__(self, length: int):
        self.snapshots = []
        self.current_array = [0] * length
        self.changes_indexes = [[] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.current_array[index] = val

    def snap(self) -> int:
        snapshot = [None] * len(self.current_array)
        new_snap_id = len(self.snapshots)
        for idx, n in enumerate(self.current_array):
            if len(self.snapshots) and self.snapshots[-1][idx] == n:
                continue
            self.changes_indexes[idx].append(new_snap_id)
            snapshot[idx] = n
        self.snapshots.append(snapshot)

        return new_snap_id

    def get(self, index: int, snap_id: int) -> int:
        if self.snapshots[snap_id][index] is not None:
            return self.snapshots[snap_id][index]

        changes_indexes = self.changes_indexes[index]

        if snap_id < changes_indexes[0]:
            return 0

        bs_bounds = (0, len(changes_indexes) - 1)
        while bs_bounds[1] - bs_bounds[0] > 1:
            middle_idx = len(bs_bounds) // 2

            bs_bounds = (bs_bounds[0], middle_idx - 1) if snap_id < changes_indexes[middle_idx] else (
            middle_idx, bs_bounds[1])

        return self.snapshots[changes_indexes[bs_bounds[0]]][index]


def main():
    obj = SnapshotArray(3)
    obj.set(0, 5)
    obj.snap()
    obj.set(0, 6)
    print('Get array[0] (snap=0): ', obj.get(0, 0))

    # obj = SnapshotArray(1)
    # obj.snap()
    # obj.snap()
    # obj.set(0, 4)
    # obj.snap()
    # print('Get array[0] (snap=1): ', obj.get(0, 1))
    # obj.set(0, 12)
    # print('Get array[0] (snap=1): ', obj.get(0, 1))
    # obj.snap()
    # print('Get array[0] (snap=3): ', obj.get(0, 3))


if __name__ == "__main__":
    main()
