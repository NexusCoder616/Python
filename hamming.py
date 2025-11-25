def generate_hamming_code(data_bits):
    data = data_bits[::-1]  # Reverse (LSB first)
    r = 0

    # Calculate number of parity bits
    while len(data) + r + 1 > 2**r:
        r += 1

    h = ['0'] * (len(data) + r + 1)
    j = 0

    # Place data bits
    for i in range(1, len(h)):
        if i & (i - 1):  # Not power of 2
            h[i] = data[j]
            j += 1

    # Calculate parity bits
    for i in range(r):
        p = 2**i
        s = 0
        for j in range(1, len(h)):
            if j & p and h[j] == '1':
                s += 1
        h[p] = '1' if s % 2 else '0'

    return h
    
n = int(input("Enter number of data bits: "))

print("Enter data bits (LSB first):")
data_bits = ""
for _ in range(n):
    data_bits += input().strip()

# Generate Hamming code
h = generate_hamming_code(data_bits)
print("\nGenerated Hamming Codeword:", ''.join(h[::-1]))

