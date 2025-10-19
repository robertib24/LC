class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add_operation(string):
            result = list(string)
            for i in range(1, len(result), 2):
                result[i] = str((int(result[i]) + a) % 10)
            return ''.join(result)
        
        def rotate_operation(string):
            n = len(string)
            return string[n-b:] + string[:n-b]
        
        visited = set()
        queue = [s]
        visited.add(s)
        min_string = s
        
        while queue:
            current = queue.pop(0)
            
            if current < min_string:
                min_string = current
            
            added = add_operation(current)
            if added not in visited:
                visited.add(added)
                queue.append(added)
            
            rotated = rotate_operation(current)
            if rotated not in visited:
                visited.add(rotated)
                queue.append(rotated)
        
        return min_string
