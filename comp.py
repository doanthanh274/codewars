def comp(array1, array2):
    if (array2==None or array1==None or len(array1)!=len(array2)):
        return False
    len_a1 = len(array1)
    count = 0
    while True:
        for a2 in array2:
            if (a2 == array1[0]**2):
                array2.remove(a2)
                array1.pop(0)
        count+=1
        if (array1==array2==[]):
            return True
        if (count == 10000):
            return False

def community_solution(array1,array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(community_solution(a1,a2))