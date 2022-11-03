# For this assignment, optimised solutions were found through code wars top
# rated solution for each problem, as this would give the best possiblity at 
# minimising time.

# ----------------------- first problem --------------------------

def solution(number):
    multiples = []
    for num in range(1, number):
        if num % 3 == 0 or num % 5 == 0:
            multiples.append(num)
    return sum(multiples)

    # I think this would be quadratic O(n)^2 and I don't believe that there is anyway to bring 
    # down time complexity for this one. While you may be able to write more efficient 
    # code in terms of consolidation the time time complexity for O to process n would'nt 
    # be significant enough of a decrease to bring it down to O(n log n)

#--------------------------- second problem ------------------------

def make_negative(number):
    if number <= 0 :
        return number * 1
    else:
        return number * (-1)

    #I think this would've been O(n)

"""
To change time complexity, I could've solved it like this. With the use of the built in function it
# would've made it linear. 
"""

#optimised

def make_negative(number):
    return -abs(number)
    # I think this would be constant O(log n)

#--------------------------- third problem ----------------------------

def solution(number):
    
    multiples = []
    
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
        
    return sum(multiples)

    # With this one, I belive this is quartic O(n)^2 becuase of the way it traverses range, 
    # has to append to multiples and then go back and traverse through multiples to sum it.
    # it's time complexity increases similar to nested for loops because of the additional steps involved

    #optimised 

    def solution(number):
        return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

    #I believe that this might be linear as it doesn't append any of the variables, 
    # and sum and range are both built in functions. 