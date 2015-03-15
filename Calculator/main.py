from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.properties import ListProperty

import random
from math import sin,cos,tan
textCalc = ''



flag = True
class Calculator(BoxLayout):
	def calc(self,text):
		global flag
		global textCalc
		label =  self.ids['my_text']
		try:
			if text == 'C':
				label.text = '0'
				textCalc =''
				flag = True
				return
			if text == '=':
				if flag:
					textCalc = str(eval(textCalc))
					flag = False
			elif text in ['sin','cos','tan','cot']:
				ans = eval(textCalc)
				if text == 'sin':
					textCalc = str(sin(ans))
				if text == 'cos':
					textCalc = str(cos(ans))
				if text == 'tan':
					textCalc = str(tan(ans))
				flag = True
			else:
				if text in ['+','*','/','-']:
					if textCalc=='':
						return
					if not flag :
						flag = True
				if flag:
					if text not in ['+','*','/','-'] or label.text[-1] not in ['+','*','/','-']:
						textCalc = textCalc + text
			#print flag
			label.text = textCalc
		except:
			pass
class CalcApp(App):
	def build(self):
		return Calculator()


if __name__ == '__main__':
	CalcApp().run()
