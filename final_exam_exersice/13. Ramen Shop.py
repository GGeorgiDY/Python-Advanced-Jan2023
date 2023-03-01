from collections import deque

bowls_of_ramen = deque(map(int, input().split(', ')))
customers = deque(map(int, input().split(', ')))

while len(bowls_of_ramen) > 0 and len(customers) > 0:
    current_ramen = bowls_of_ramen.pop()
    current_customer = customers.popleft()

    if current_ramen == current_customer:
        pass

    elif current_ramen > current_customer:
        current_ramen -= current_customer
        bowls_of_ramen.append(current_ramen)

    elif current_ramen < current_customer:
        current_customer -= current_ramen
        customers.appendleft(current_customer)

if len(customers) == 0:
    print("Great job! You served all the customers.")
    if len(bowls_of_ramen) > 0:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls_of_ramen))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if len(customers) > 0:
        print(f"Customers left: {', '.join(map(str, customers))}")


# 14, 25, 37, 43, 19
# 58, 23, 37

# 30, 13, 45
# 70, 25, 55, 15
