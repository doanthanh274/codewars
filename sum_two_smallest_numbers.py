def sum_two_smallest_numbers(numbers):
    return sorted(numbers)[0]+sorted(numbers)[1]

def community_solution(numbers):
    return sum(sorted(numbers)[:2])

number = [5, 8, 12, 18, 22]
print(sum_two_smallest_numbers(number))
