class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full_lakes = {}
        dry_days = []
        result = [-1] * len(rains)
        
        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
                result[i] = 1 
            else:
                if lake in full_lakes:
                    last_rain = full_lakes[lake]
                    
                    left, right = 0, len(dry_days) - 1
                    found = -1
                    
                    while left <= right:
                        mid = (left + right) // 2
                        if dry_days[mid] > last_rain:
                            found = mid
                            right = mid - 1
                        else:
                            left = mid + 1
                    
                    if found == -1:
                        return []
                    
                    dry_day_index = dry_days[found]
                    result[dry_day_index] = lake
                    dry_days.pop(found)
                
                full_lakes[lake] = i
        
        return result
