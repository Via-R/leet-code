class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ['Fizz'[i%3*4:(i%3+1)*4] + 'Buzz'[i%5*4:(i%5+1)*4] if i%3==0 or i%5==0 else str(i) for i in range(1, n+1)]