from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_value = int(input())
counter = 0
initial_bullets_counter = len(bullets)

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks[0]
    if current_bullet <= current_lock:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    counter += 1
    if counter == gun_barrel_size and len(bullets) > 0:
        print("Reloading!")
        counter = 0
        continue

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value-((initial_bullets_counter-len(bullets))*bullet_price)}")

# 50
# 2
# 11 10 5 11 10 20
# 15 13 16
# 1500

# 20
# 6
# 14 13 12 11 10 5
# 13 3 11 10
# 800

# 33
# 1
# 12 11 10
# 10 20 30
# 100

