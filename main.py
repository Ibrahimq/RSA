from RSA import RSA
# For message Conversion
from utils import *
# For GUI
from tkinter import *
from tkinter.font import Font
from datetime import datetime


class GUI(object):
    def __init__(self, root, rsa_init):
        self.rsa_init = rsa_init
        self.reset_RSA()
        self.root = root
        self.bold_font = Font(family="Helvetica", size=14, weight="bold")
        self.root.title('Encryption & Decryption RSA')
        self.text_label = Label(self.root, text='Text').grid(row=0, column=1)
        self.stringVIn = StringVar()
        self.input_string = Entry(self.root, font=self.bold_font, textvariable=self.stringVIn)
        self.stringVIn.trace("w", lambda name, index, mode, sv=self.stringVIn: self.callback())
        self.input_string.grid(row=1, column=1, padx=5, pady=3)
        self.stringVOut = StringVar()
        self.output_label = Label(self.root, text='Output').grid(row=0, column=4)
        self.output = Entry(self.root, font=self.bold_font,
                            textvariable=self.stringVOut).grid(row=1, column=4, padx=5, pady=3)
        self.encrypt_button = Button(self.root, text='Encrypt',
                                     command=lambda: self.get_encrypt(self.input_string.get())
                                     ).grid(row=3, column=1, pady=4)
        self.reset_button = Button(self.root, text='Reset',
                                   command=lambda: self.reset_RSA()
                                     ).grid(row=4, column=2, pady=3)
        # , state='disabled'
        self.decrypt_button = Button(self.root, text='Decrypt',
                                     command=lambda: self.get_decrypt(self.input_string.get(), rsa_init)
                                     ).grid(row=3, column=4, pady=4)

    def callback(self):
        self.stringVIn.set(self.stringVIn.get()[:512])

    def set_output(self, out):
        self.stringVOut.set(out)

    def reset_RSA(self):
        self.rsa = RSA(self.rsa_init)

    def get_encrypt(self, plain_text):
        # do encryption
        t1 = datetime.now()
        plain_text = convert_m2i(plain_text)
        cypher_text = self.rsa.encryption(plain_text)
        t2 = datetime.now()
        d = t2-t1
        self.set_output(cypher_text)
        print("Encryption Done in: "+str(d.seconds)+"."+str(d.microseconds))
        print("Encryption Result is: "+str(cypher_text))
        return

    def get_decrypt(self, cypher_text, rsa_init):
        # do decryption
        t1 = datetime.now()
        cypher_text = int(cypher_text)
        plain_text = self.rsa.decryption(cypher_text)
        t2 = datetime.now()
        d = t2-t1
        self.set_output(convert_i2m(plain_text))
        print("Decryption Done in: "+str(d.seconds)+"."+str(d.microseconds))
        print("Decryption Result is: "+convert_i2m(plain_text))
        return


if __name__ == "__main__":
    interface = Tk()
    GUI(interface, 512)
    interface.mainloop()
