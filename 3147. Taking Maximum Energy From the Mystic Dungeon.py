class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        n = len(energy)
        max_energy = float('-inf')
        
        for start in range(n - k, n):
            current_energy = 0
            pos = start
            while pos >= 0:
                current_energy += energy[pos]
                max_energy = max(max_energy, current_energy)
                pos -= k
        
        return max_energy
