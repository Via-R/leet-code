class SnapshotArray:

    def __init__(self, length: int):
        self.snapshots = [[{"val": 0}] * length]
        self.length = length
        self.snapshot_count = 0

    def set(self, index: int, val: int) -> None:
        snapshots_length = len(self.snapshots)
        while self.snapshot_count >= snapshots_length:
            new_snapshot = [n for n in self.snapshots[-1]]
            self.snapshots.append(new_snapshot)
            snapshots_length = len(self.snapshots)

        if snapshots_length > 1 and val != self.snapshots[-2][index]["val"]:
            self.snapshots[-1][index] = {"val": val}
        elif snapshots_length == 1:
            self.snapshots[-1][index]["val"] = val
        else:
            self.snapshots[-1][index] = self.snapshots[-2][index]

    def snap(self) -> int:
        self.snapshot_count += 1

        return self.snapshot_count - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id > len(self.snapshots) - 1:
            return self.snapshots[-1][index]["val"]

        return self.snapshots[snap_id][index]["val"]


def main():
    obj = SnapshotArray(3)
    obj.set(0, 5)
    obj.snap()
    obj.set(0, 6)
    print('Get array[0] (snap=0): ', obj.get(0, 0))

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


if __name__ == "__main__":
    main()
