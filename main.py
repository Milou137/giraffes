DEFAULT_NECK_LENGTH = 100

class Giraffe():

    def __init__(self, neck_length = DEFAULT_NECK_LENGTH):

        self.neck_length = neck_length
def main():
    giraffes = []
    for i in range(3):
        giraffes.append(Giraffe())
main()
