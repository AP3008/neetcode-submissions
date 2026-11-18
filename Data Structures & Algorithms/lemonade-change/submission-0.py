class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = twenty = 0
        for i in range(len(bills)):
            if bills[i] == 5: 
                five+=1 
            elif bills[i] == 10 and five > 0: 
                five-=1 
                ten+=1 
            elif bills[i] == 20 and five >= 3:
                twenty+=1 
                five-=3
            elif bills[i] == 20 and ten >= 1 and five >= 1:
                twenty+=1
                five-=1
                ten-=1
            else:
                return False
        return True 
            


