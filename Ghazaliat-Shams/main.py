# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from bidi.algorithm import get_display
from kivy.uix.listview import ListItemButton
from kivy.factory import Factory
from Beits import beits
from Beits import Poems
from Beits import extract_poem

import arabic_reshaper
Builder.load_string(
'''
#:import la kivy.adapters.listadapter 
#:import lbl kivy.uix.label

<Persian>:
    id: namus
    title: title
    search: search
    beit_list: beit_list
    adding: adding
    BoxLayout:
        size_hint_x: 1
        orientation: 'vertical'
        Label:
            id: title
            font_name: 'BNAZANIN.TTF'
            font_size: '45dp'
            size_hint_y: 5
        Button:
            id: search
            font_name: 'BNAZANIN.TTF'
            size_hint_y: 1
            on_press: root.gonew()
        Button:
            id: adding
            font_name: 'BNAZANIN.TTF'
            size_hint_y: 1
    ListView:
        size_hint_x: 2
        id: beit_list 
        adapter: la.ListAdapter(data=[], cls=lbl.Label)
<Poetry>:
    orientation: 'vertical'
    back: back
    beit_list: beit_list
    Button:
        id: back
        font_name: 'BNAZANIN.TTF'
        size_hint_y:1
        text: 'Back'
        on_press: root.goback()
    ListView:
        size_hint_y: 7
        id: beit_list 
        adapter: la.ListAdapter(data=[], cls=lbl.Label)

<MyLabel>:
    font_name: 'BNAZANIN.TTF'
    height: 60
    on_press: self.set_index()
    selected_color: [1,0,0,0]
    deselected_color: [0,1,1,1]
    halign: 'center'
''')





beit_index =-1
def pars(str):
    return get_display(arabic_reshaper.reshape(str))

class MyLabel(ListItemButton):
    #def __init__(self,index):
    #    super(MyLabel,self).__init__()
    #    self.index = index   
    def set_index(self):
        global beit_index
        beit_index=self.index
class Persian(BoxLayout):
    def __init__(self):
        super(Persian, self).__init__()
        self.title.text = get_display(arabic_reshaper.reshape(u'غزلیات \n شمس \n تبریزی'))
        self.search.text = pars(u'برو به شعر')
        self.adding.text = pars(u'افزودن')
        self.beit_list.adapter.data = [pars(u'ناموس شعر')]
        for i in beits:
            self.beit_list.adapter.data.extend([pars(i)])
        self.beit_list.adapter.cls = MyLabel

    def gonew(self):
        global beit_index
        #print 'beit_index is',beit_index
        self.clear_widgets()
        tmp = Poetry(beit_index)
        self.add_widget(tmp)

class Poetry(BoxLayout):
    def __init__(self,poemNum):
        super(Poetry, self).__init__()
        self.back.text = pars(u'برگشت')
        self.beit_list.adapter.data = []
        poem = extract_poem(poemNum)
        for i in poem:
            self.beit_list.adapter.data.extend([pars(i[1])+'      '+pars(i[0])])
        self.beit_list.adapter.cls = MyLabel
    def goback(self):
        self.clear_widgets()
        tmp = Persian()
        self.add_widget(tmp)

class PersianApp(App):

    def build(self):
        return Persian()


if __name__ == '__main__':
    PersianApp().run()
