import math

if __name__ == "__main__":
    AB = int(input())
    BC = int(input())
    angle = math.atan(AB / BC)
    print(f"{round(math.degrees(angle))}{chr(176)}")
