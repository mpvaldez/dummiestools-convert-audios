# -*- coding: utf-8 -*-
"""
###########
This is a mini program that will help you convert your audios from one format to another.
You just have to answer the following questions
###########
"""

import os
import pydub
import glob

class HandleConvert():

	DEFAULT_AUDIO_FROM_FORMAT = "wav"
	DEFAULT_AUDIO_TO_FORMAT = "mp3"
	collected_audios = []

	def __init__(self):
		print(__doc__)

	def request_from_format(self):
		self.from_format = input("Please tell me the source format: ") or self.DEFAULT_AUDIO_FROM_FORMAT
		
	def request_to_format(self):
		self.to_format = input("Please tell me the destination format: ") or self.DEFAULT_AUDIO_TO_FORMAT

	def get_files(self):
		self.collected_audios = glob.glob('./*.{}'.format(self.from_format))
		return self.collected_audios

	def exec_convert(self):
		for filename in self.get_files():
			name_output = os.path.basename(filename)
			print("... Converting '{}' ...".format(name_output))
			to_filename = './output/{}.{}'.format(name_output.split(".{}".format(self.from_format))[0], self.to_format)
			sound = pydub.AudioSegment.from_file(filename, self.from_format)
			sound.export(to_filename, format=self.to_format)
			print("Conversion complete!")
			
	def say_goodbye(self):
		print("All done. Bye Bye!!")


if __name__ == "__main__":
	
	hc = HandleConvert()
	hc.request_from_format()
	hc.request_to_format()
	hc.exec_convert()
	hc.say_goodbye()




