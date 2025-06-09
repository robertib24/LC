class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        fact = [0]*11
        fact[0]=fact[1]=1
        for i in range(2, 11):
            fact[i]=fact[i-1]*i
        
        number = ["-1"]*n
        permutations = 0
        dictionary = set()

        def get_freq_matrix(number):
            freq = [0]*10
            for num in number:
                freq[int(num)]+=1
            return freq

        def countAllPermutations(number, freq, n):
            ret = fact[n]
            for i in range(10):
                ret /= fact[freq[i]]
            return ret

        def isKPalindrome(number):
            ret = int(''.join(number))
            return ret%k==0

        def countValidKPalindromes(number):
            sorted_numbers = sorted(number)
            sorted_numbers_tuple = tuple(sorted_numbers)
            if sorted_numbers_tuple in dictionary:
                return 0
            dictionary.add(sorted_numbers_tuple)

            freq = get_freq_matrix(number)
            total = countAllPermutations(number, freq, n)

            invalids = 0
            if freq[0]>0:
                freq[0]-=1
                invalids = countAllPermutations(number, freq, n-1)
            
            return total-invalids

        def generate_pallindromes(pos, number):
            nonlocal permutations
            if pos>n//2:
                if isKPalindrome(number):
                    permutations+=countValidKPalindromes(number)
                return

            start = 1 if pos==0 else 0
            while start <= 9:
                number[pos]=str(start)
                number[n-pos-1]=str(start)
                generate_pallindromes(pos+1, number)
                start+=1
            number[pos]="-1"

        generate_pallindromes(0, number)
        return int(permutations)
