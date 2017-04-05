"""
补数计算器V2.1: 更好的封装
V2.2: 添加合适的注释；引入多线程（在特定时间内没有输入数据将会直接退出程序 *将于两天内更新
Introduction: Compute 2's complement
Undate_note: (V2.1) better encapsulation; (V2.2) import theading to kill process when input is found in certain period
__author__ = v1·每天都在修仙·siuol
__date__ = 2017.4.5
"""


class bin2complement:
    """
    This is a calculator[V2.0] for 2's complement
    Enter the number in binary forms (e.g. 010101)
    To exit, enter 0 or any elements other than binary numbers
    """

    def __init__(self):
        self.__in = None
        self.__out = None

        self.initialize()
        while True:
            self.write(input("Number: "))
            self.calculate()
            self.read()

    @staticmethod
    def initialize():
        print("-------------------------------------------------------------------------")
        print("----          This is a calculator[V2.0] for 2's complement          ----")
        print("----         Enter the number in binary forms (e.g. 010101)          ----")
        print("----   To exit, enter 0 or any elements other than binary numbers    ----")
        print("-------------------------------------------------------------------------")

    def write(self, userInput):
        if "".zfill(len(userInput)) == userInput or "".zfill(len(userInput)) != userInput.replace("1", "0"):
            self.exit()
        else:
            self.__in = userInput

    def read(self):
        print("%s ===> %s" % (self.__in, self.__out))
        print()

    def calculate(self):

        def toggle(st):
            return "1" if st == "0" else "0"

        temp = list(map(toggle, self.__in))  # 1's complement
        n = -1  # end position
        while True:
            # animation of 1 + 1's complement
            if temp[n] == "0":
                temp[n] = toggle(temp[n])
                break
            else:
                temp[n] = toggle(temp[n])
                n -= 1
        self.__out = "".join(temp)
        print("Calculation completed!")

    @staticmethod
    def exit():
        print("-------------------------------    Bye    -------------------------------")
        exit()

if __name__ == "__main__":
    if False:  # test close
        bin2complement()
