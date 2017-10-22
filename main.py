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
		self.root.title("AnyPay Test POS")
		self.root.focus_set()
		self.root.wm_iconbitmap(bitmap="anypay_icon_o.ico")

		self.root.configure(background="#3366CC")
		Tkinter.Label(self.root, text="Card Data ", background="#3366CC", font=("Courier", 44), anchor="e").grid(row=0, column=0, sticky="E")

		Tkinter.Label(self.root, text="PAN: ", background="#3366CC", font=("Courier", 44), anchor="e").grid(row=1, column=0, sticky="E")
		self.pan_field = Tkinter.Label(self.root, text="", background="#3366CC", font=("Courier", 44), anchor="w")
		self.pan_field.grid(row=1, column=1, sticky="W")

		Tkinter.Label(self.root, text="First Name: ", background="#3366CC", font=("Courier", 44), anchor="e").grid(row=2, column=0, sticky="E")
		self.first_name_field = Tkinter.Label(self.root, text="", background="#3366CC", font=("Courier", 44), anchor="e")
		self.first_name_field .grid(row=2, column=1, sticky="W")

		Tkinter.Label(self.root, text="Last Name: ", background="#3366CC", font=("Courier", 44), anchor="e").grid(row=3, column=0, sticky="E")
		self.last_name_field = Tkinter.Label(self.root, text="", background="#3366CC", font=("Courier", 44), anchor="w")
		self.last_name_field.grid(row=3, column=1, sticky="W")

		Tkinter.Label(self.root, text="Exp Date: ", background="#3366CC", font=("Courier", 44), anchor="e").grid(row=4, column=0, sticky="E")
		self.exp_name_field = Tkinter.Label(self.root, text="", background="#3366CC", font=("Courier", 44), anchor="w")
		self.exp_name_field.grid(row=4, column=1, sticky="W")

		self.mag_string = Tkinter.StringVar()
		self.card_data = MagCard("")
		self.e1 = Tkinter.Entry(self.root, textvariable=self.mag_string, font=("Courier", 44))

		self.e1.grid(row=0, column=1)
		self.e1.bind('<Return>', self.update_card)

		Tkinter.Button(self.root, text="Clear", command=self.clear_text, font=("Courier", 44)).grid(row=5, column=0, columnspan=2, sticky="NESW")

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

	def clear_text(self):
		self.pan_field.config(text="")
		self.first_name_field.config(text="")
		self.last_name_field.config(text="")
		self.exp_name_field.config(text="")
		self.e1.delete(0, 'end')

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
