n, t = 5, 10
w = list(range(n+1))
slots = [w[i % len(w)] for i in range(t)]
print(f"Window size = {n} -> {slots}\n")

for i in range(0, t, n):
    s = slots[i:i+n]
    a = slots[i+n] if i+n < t else s[-1]
    print("Sender frames:", s)
    print("Receiver ACK:", a, "\n")
