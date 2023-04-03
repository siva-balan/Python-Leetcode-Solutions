class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        '''people.sort()
        output = 0
        while len(people) > 0:
            l,r = 0,len(people) -1
            if l ==r:
                output+=1
                people.pop()
            x = output
            while x +1 != output and len(people)>0 and r >=0:
                if l ==r:
                    output+=1
                    people.pop()
                if people[l] + people[r] <= limit:
                    people.pop()
                    people.pop(0)
                    output +=1
                elif people[r] > limit - people[l]:
                    r -=1
        return output'''

        people.sort()
        output = 0
        l,r = 0 ,len(people)-1

        while l <=r:
            if people[l] + people[r] <= limit:
                l +=1
                r -=1
            else:
                r -=1
            output +=1
        return output
