class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            stack.append(a)
            while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:
                collider = stack.pop()
                collidee = stack.pop()
                if abs(collider) > collidee:
                    stack.append(collider)
                elif abs(collider) < collidee:
                    stack.append(collidee)
                else:
                    continue 
        return stack  

        