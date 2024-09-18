class LuhnsAlgorithm:
    def __init__(self):
        self.__card_num = [int(x) for x in input("Enter your card number: ")]

    def luhns(self):
        temp = []
        for i in range(len(self.__card_num)):
            if (i % 2 == 0):
                self.__card_num[i] *= 2
            temp.append(self.__card_num[i])
        total = 0
        for j in range(len(temp)):
            if (temp[j] > 9):
                temp[j] = int(str(temp[j])[-1]) + int(str(temp[j])[-2])
            total += temp[j]
        if (str(total)[-1] == "0"):
            return True
        else:
            return False

    def is_valid_card(self):
        if (self.luhns()):
            print("The card is valid.")
        else:
            print("The card is NOT valid.")


sample = LuhnsAlgorithm()
sample.is_valid_card()
