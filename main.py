from magcard import MagCard
import Tkinter


month_string = ["",
	"January",
	"Febuary",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December"]

class simpleapp_tk:
	def __init__(self):
		self.root = Tkinter.Tk()
		self.root.title("Skynet Watches")
		self.root.focus_set()
		self.root.wm_iconbitmap(bitmap="anypay_icon_o.ico")

		self.root.configure(background="#555")
		Tkinter.Label(self.root, text="Card Data", background="#555", font=("Courier", 44)).grid(row=0, column=0)

		Tkinter.Label(self.root, text="PAN", background="#555", font=("Courier", 44)).grid(row=1, column=0)
		self.pan_field = Tkinter.Label(self.root, text="", background="#555", font=("Courier", 44))
		self.pan_field.grid(row=1, column=1)

		Tkinter.Label(self.root, text="First Name", background="#555", font=("Courier", 44)).grid(row=2, column=0)
		self.first_name_field = Tkinter.Label(self.root, text="", background="#555", font=("Courier", 44))
		self.first_name_field .grid(row=2, column=1)

		Tkinter.Label(self.root, text="Last Name", background="#555", font=("Courier", 44)).grid(row=3, column=0)
		self.last_name_field = Tkinter.Label(self.root, text="", background="#555", font=("Courier", 44))
		self.last_name_field.grid(row=3, column=1)

		Tkinter.Label(self.root, text="Exp Date", background="#555", font=("Courier", 44)).grid(row=4, column=0)
		self.exp_name_field = Tkinter.Label(self.root, text="", background="#555", font=("Courier", 44))
		self.exp_name_field.grid(row=4, column=1)

		self.mag_string = Tkinter.StringVar()
		self.card_data = MagCard("")
		self.e1 = Tkinter.Entry(self.root, textvariable=self.mag_string, font=("Courier", 44))

		self.e1.grid(row=0, column=1)
		self.e1.bind('<Return>', self.update_card)

		for i in range(10):
			self.root.columnconfigure(i, weight=1)

	def update_card_display(self):
		self.pan_field.config(text=str(self.card_data.data["PAN"]))
		self.first_name_field.config(text=str(self.card_data.data["First"].title()))
		self.last_name_field.config(text=str(self.card_data.data["Last"].title()))
		try:
			exp = "{} 20{}".format(month_string[int(self.card_data.data["Expiration"][1])], self.card_data.data["Expiration"][0])
		# Can't index nonetype
		except TypeError:
			exp = "None"
		self.exp_name_field.config(text=exp)

	def update_card(self, data):
		print "Typed Text"
		temp_card = MagCard(self.mag_string.get())
		if temp_card.populated:
			self.card_data = temp_card
			self.update_card_display()

	def run(self):
		self.root.mainloop()


if __name__ == "__main__":
	app = simpleapp_tk()
	app.run()
