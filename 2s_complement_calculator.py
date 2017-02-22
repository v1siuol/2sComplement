"""
计算补数 写得好复杂 looking for a simpler way to approach
Introduction: Compute 2's complement
__author__ = visiuol
__date__ = 2017.2.22
"""


def toggle(st):
    return "1" if st == "0" else "0"


def Complement2s():
    """
    This is a calculator[V1.0] for 2's complement
    Enter the number in binary forms (e.g. 010101)
    To exit, enter 0 or any elements other than binary numbers
    """

    print("-------------------------------------------------------------------------")
    print("----          This is a calculator[V1.0] for 2's complement          ----")
    print("----         Enter the number in binary forms (e.g. 010101)          ----")
    print("----   To exit, enter 0 or any elements other than binary numbers    ----")
    print("-------------------------------------------------------------------------")

    bNum = input("Number: ")
    while "".zfill(len(bNum)) != bNum and "".zfill(len(bNum)) == bNum.replace("1", "0"):
        result = list(map(toggle, bNum))  # 1's complement
        n = -1  # end position
        while True:
            # animation of 1 + 1's complement
            if result[n] == "0":
                result[n] = toggle(result[n])
                break
            else:
                result[n] = toggle(result[n])
                n -= 1
        print("".join(result))
        bNum = input("Number: ")
    print("-------------------------------    Bye    -------------------------------")

if __name__ == "__main__":
    if False:  # test closed
        Complement2s()
