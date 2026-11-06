class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # If a car catches up for another it joins the car fleet. A car fleet all has the same speed i.e the speed of the car at the front. 
        # We want to create a pair the position to the speed, iterate in reverse order so we can see how fast 

        # Creating a pair by using a list comprehension, and zipping together the psoitions with the speeds 
        pair = [[p,s] for p,s in zip(position, speed)]
        # This is our stack 
        stack = []
        # We iterate through this list in reverse order because the car at the front of the fleet wee need to know 
        for p,s in sorted(pair)[::-1]: # iterate in reverse order
            # target - p / s is the time for this car to each the target unobstructed. distance / speed = time 
            stack.append((target-p)/s)
            # If the stack has 2 cars in it, the other car is ahead of it in position, so if it is is slower the current car we just added needs to join the carfleet, so we pop that value as it joined that car. The cars with greater position are in the satck first because we are iterating through the list in reverse order
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        # By the end the number of car fleets will be the length of the stack. 
        return len(stack)