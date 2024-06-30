from cmath import phase

if __name__ == "__main__":
    z = complex(input())
    r = abs(z)
    angle = phase(z)
    print(f"{r:.3f}\n{angle:.3f}")
