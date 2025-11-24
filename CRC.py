def xor(a, b):
    return "".join("0" if a[i] == b[i] else "1" for i in range(1, len(b)))


def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[:pick]

    while pick < len(dividend):
        tmp = xor(divisor if tmp[0] == "1" else "0" * pick, tmp) + dividend[pick]
        pick += 1

    return xor(divisor, tmp) if tmp[0] == "1" else xor("0" * pick, tmp)


def encode(data, key):
    appended = data + "0" * (len(key) - 1)
    crc = mod2div(appended, key)
    codeword = data + crc

    print("Message Length:", len(data))
    print("Polynomial Length:", len(key))
    print("Computed CRC Bits:", crc)

    return codeword


def verify(codeword, key, received):
    remainder = mod2div(received, key)

    print("Transmitted Codeword:", codeword)
    print("Received Bits:", received)
    print("CRC Remainder at Receiver:", remainder)
    print("Error Detection Result:",
          "No Error Detected" if remainder == "0" * (len(key) - 1) else "Error Detected")


def main():
    data = input("Enter Dataword (binary): ").strip()
    key = input("Enter Polynomial Key (binary): ").strip()

    print("\n=== Sender Side ===")
    codeword = encode(data, key)

    print("\n=== Receiver Side ===")
    received = input("Enter Received Codeword (Enter for same): ").strip() or codeword
    verify(codeword, key, received)


if __name__ == "__main__":
    main()
