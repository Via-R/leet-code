class SnapshotArray:

    def __init__(self, length: int):
        self.array = [0] * length
        self.snapshots = [{} for _ in range(length)]
        self.change_ids = [[] for _ in range(length)]
        self.snapshot_count = 0
        self.changed_idxs = set()

    def set(self, index: int, val: int) -> None:
        change_ids = self.change_ids[index]
        snapshots = self.snapshots[index]
        last_val = snapshots[change_ids[-1]] if len(change_ids) else 0
        if last_val != val:
            self.changed_idxs.add(index)
        else:
            self.changed_idxs.discard(index)

        self.array[index] = val

    def snap(self) -> int:
        for idx in self.changed_idxs:
            self.change_ids[idx].append(self.snapshot_count)
            self.snapshots[idx][self.change_ids[idx][-1]] = self.array[idx]

        self.snapshot_count += 1
        self.changed_idxs = set()

        return self.snapshot_count - 1

    def get(self, index: int, snap_id: int) -> int:
        change_ids = self.change_ids[index]
        if not len(change_ids):
            return 0

        snapshots = self.snapshots[index]
        if snapshots.get(snap_id) is not None:
            return snapshots[snap_id]

        left, right = 0, len(change_ids) - 1
        while left < right:
            middle = (left + right) // 2
            if snap_id < change_ids[middle]:
                right = middle - 1
            else:
                left = middle + 1

        if snap_id < change_ids[left]:
            return snapshots[change_ids[left - 1]] if left > 0 else 0

        return snapshots[change_ids[left]]


def main():
    obj = SnapshotArray(3)
    obj.set(0, 5)
    obj.snap()
    obj.set(0, 6)
    print('Get array[0] (snap=0): ', obj.get(0, 0))
    # must be 5

    print()

    obj = SnapshotArray(1)
    obj.snap()
    obj.snap()
    obj.set(0, 4)
    obj.snap()
    print('Get array[0] (snap=1): ', obj.get(0, 1))
    obj.set(0, 12)
    print('Get array[0] (snap=1): ', obj.get(0, 1))
    obj.snap()
    print('Get array[0] (snap=3): ', obj.get(0, 3))
    # must be 0 0 12

    print()

    obj = SnapshotArray(1)
    obj.snap()
    obj.snap()
    obj.set(0, 4)
    obj.snap()
    obj.snap()
    obj.set(0, 12)
    obj.snap()
    print('Get array[0] (snap=0): ', obj.get(0, 0))
    print('Get array[0] (snap=1): ', obj.get(0, 1))
    print('Get array[0] (snap=2): ', obj.get(0, 2))
    print('Get array[0] (snap=3): ', obj.get(0, 3))
    print('Get array[0] (snap=4): ', obj.get(0, 4))
    #  must be 0 0 4 4 12


if __name__ == "__main__":
    main()
