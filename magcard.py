import re


class MagCard(object):
	track_1 = r"\B(\d+?)\^([^\^]+?)\^(.{4})"

	def __init__(self, data):
		self._info = {
			"PAN": None,
			"First": None,
			"Last": None,
			"Expiration": None
		}
		self._data = ""
		self.data = data

	@property
	def data(self):
		return self._info

	@data.setter
	def data(self, text):
		self._data += text
		self.pharse_data(self._data)

	def pharse_data(self, text):
		track_1_regex = re.search(self.track_1, text)
		if track_1_regex is not None:
			pan = int(track_1_regex.group(1))

			last_name = track_1_regex.group(2).split("/")[0]
			first_name = track_1_regex.group(2).split("/")[1]

			year = track_1_regex.group(3)[:2]
			month = track_1_regex.group(3)[2:]

			self._info["PAN"] = pan
			self._info["First"] = first_name
			self._info["Last"] = last_name
			self._info["Expiration"] = (year, month)

	@property
	def populated(self):
		return all(self.data[i] is not None for i in self.data)

	def __repr__(self):
		try:
			exp = "{} 20{}".format(self.data["Expiration"][1], self.data["Expiration"][0])
		# Can't index nonetype
		except TypeError:
			exp = "None"
		return "PAN: {}\nName: {}, {}\nExpiration: {}".format(self.data["PAN"], self.data["Last"], self.data["First"], exp)

if __name__ == '__main__':
	card = MagCard(raw_input("Card Data: "))
	print card.populated
	print card
