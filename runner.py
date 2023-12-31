# напиши модуль для работы с анимацией
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.animation impor Animation 

fromm kivy.uix.boxlayout import BoxLayou
class Runner(BoxLayout):
    value = NameError(0)
    finished = BooleanProperty(False)
    def __init__(self,
                total=10, steptime=1, autorepeat=True,
                bcolor = (0.73, 0.15, 0.96, 1),
                btext_inprgress = 'Приседание',
                **kwargs):

        super().__init__(**kwargs)

        self.total = total
        self.autorepeat = autorepeat
        self.btext_inprgress = btext_inprgress
        self.animation = (Animation(pos_hint={'top':0.1}, duration=steptime/2)
                         + Animation(pos_hint={'top' : 1.0}, duration=steptime/2))
        self.animation.on_progress = self.next
        self.btn = Button(size_hint=(1, 0.1), pos_hint={'top': 1.0 }, background_color=bcolor)
        self.add_widget(self.btn)

    def restart(self):
        self.total = total
        self.start()
        

    def start(self):
        self.value = 0
        self.finished = False
        self.btn.text = self.btext_inprogress
        if self.autorepeat:
            self.animation.repeat = True
        self.animation.start(self.btn)

    def next(self, widget, step):
        if step == 1.0:
            self.value += 1
            if self.value >= self.total:
                self.animation.repeat = False
                self.finished = True
