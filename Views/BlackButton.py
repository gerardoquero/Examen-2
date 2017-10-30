from tkinter import Label, PhotoImage

class BlackButton(Label):

    class Constants:
        black_on = "Assets/black_button_on.ppm"
        black_off = "Assets/black_button_off.ppm"
        event = "<Button-1>"

    def __init__(self, master):
        super().__init__(master)
        self.__state = False
        self.__on_image = PhotoImage(file = self.Constants.black_on)
        self.__off_image = PhotoImage(file = self.Constants.black_off)
        self.__set_image(self.__on_image)
        self.bind(self.Constants.event, self.__toggle)

    def __toggle(self, event):
        self.__state = not self.__state
        image = self.__on_image if self.__state else self.__off_image
        self.__set_image(image)

    def __set_image(self, image):
        self.configure(image = image)
        self.image = image