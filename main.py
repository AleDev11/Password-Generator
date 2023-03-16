import customtkinter
import random

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    def generate_password(self):
        # clear password label
        self.textbox_password.delete("1.0", "end")

        # get password length
        password_length = int(self.slider_length.get())

        # check if password length is between 4 and 128
        if password_length < 4 or password_length > 128:
            #self.label_password.set_text("Password length must be between 8 and 128")
            self.textbox_password.insert("end", "Password length must be between 4 and 128")
            return

        # get uppercase letters
        uppercase_letters = self.checkbox_uppercase.get()

        # get lowercase letters
        lowercase_letters = self.checkbox_lowercase.get()

        # get numbers
        numbers = self.checkbox_numbers.get()

        # get symbols
        symbols = self.checkbox_symbols.get()

        # check if at least one checkbox is checked
        if not uppercase_letters and not lowercase_letters and not numbers and not symbols:
            #self.label_password.set_text("You must select at least one option")
            self.textbox_password.insert("end", "You must select at least one option")
            return

        # create a list with all the characters
        characters = []

        # add uppercase letters
        if uppercase_letters:
            characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

        # add lowercase letters
        if lowercase_letters:
            characters.extend(list("abcdefghijklmnopqrstuvwxyz"))

        # add numbers
        if numbers:
            characters.extend(list("0123456789"))

        # add symbols
        if symbols:
            characters.extend(list("!#$%&()*+,-./:;<=>?@[\]^_`{|}~"))

        # generate password
        password = ""
        for i in range(password_length):
            password += random.choice(characters)

        # show password
        self.textbox_password.insert("end", password)

    def slider_length_changed(self, value):
        self.textbox_length.delete("1.0", "end")
        #convert value to int and then to string
        v = str(int(value))
        self.textbox_length.insert("end", v)

    def __init__(self):

        super().__init__()

        # configure window
        self.title("Password Generator - by AleDev")
        self.geometry(f"{500}x{550}")
        self.resizable(False, False)

        # create widgets
        self.label_title = customtkinter.CTkLabel(self, text="Password Generator", font=("Arial", 20))
        self.label_title.pack(pady=10, padx=10, fill="x")

        # create label for settings
        self.label_settings = customtkinter.CTkLabel(self, text="Settings", font=("Arial", 18))
        self.label_settings.pack(pady=10, padx=10, fill="x")

        # create label for password length
        self.textbox_length = customtkinter.CTkTextbox(self, width=10, height=1, font=customtkinter.CTkFont(size=12, weight="bold"))
        self.textbox_length.pack(pady=10, padx=10, fill="x")
        self.textbox_length.insert("end", "4")

        # create entry for password length
        self.slider_length = customtkinter.CTkSlider(self, from_=4, to=128, command=self.slider_length_changed)
        self.slider_length.pack(pady=10, padx=10, fill="x")
        self.slider_length.set(4)

        # create checkbox for uppercase letters
        self.checkbox_uppercase = customtkinter.CTkCheckBox(self, text="Uppercase Letters")
        self.checkbox_uppercase.pack(pady=10, padx=10, fill="x")

        # create checkbox for lowercase letters
        self.checkbox_lowercase = customtkinter.CTkCheckBox(self, text="Lowercase Letters")
        self.checkbox_lowercase.pack(pady=10, padx=10, fill="x")

        # create checkbox for numbers
        self.checkbox_numbers = customtkinter.CTkCheckBox(self, text="Numbers")
        self.checkbox_numbers.pack(pady=10, padx=10, fill="x")

        # create checkbox for symbols
        self.checkbox_symbols = customtkinter.CTkCheckBox(self, text="Symbols")
        self.checkbox_symbols.pack(pady=10, padx=10, fill="x")

        # create button to generate password
        self.button_generate = customtkinter.CTkButton(self, text="Generate Password", command=self.generate_password)
        self.button_generate.pack(pady=10, padx=10, fill="x")

        # create label to show password
        self.textbox_password = customtkinter.CTkTextbox(self, width=200, height=70, font=customtkinter.CTkFont(size=12, weight="bold"))
        self.textbox_password.pack(pady=10, padx=10, fill="x")
        self.textbox_password.insert("end", "Generated Password by AleDev")

        # create button to copy password
        self.button_copy = customtkinter.CTkButton(self, text="Copy Password", command=lambda: self.clipboard_clear() or self.clipboard_append(self.textbox_password.get("1.0", "end")))
        self.button_copy.pack(pady=9, padx=9, fill="x")

if __name__ == "__main__":
    app = App()
    app.mainloop()