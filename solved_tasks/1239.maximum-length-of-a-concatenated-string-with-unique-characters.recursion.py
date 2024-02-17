class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        
        def dfs(start_idx, local_result):
            if len(set(local_result)) < len(local_result):
                return 0

            best_result = len(local_result)
            for idx in range(start_idx, n):
                dfs_result = dfs(idx+1, local_result + arr[idx])
                best_result = max(best_result, dfs_result)

            return best_result
        
        return dfs(0, '')