from kivy.app import App
# from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
# from kivy.uix.behaviors import DragBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, BooleanProperty, NumericProperty
# import numpy as np
# from kivy.core.window import Window
# from kivy.clock import Clock
from kivy.graphics import Line, Rectangle, Color, Ellipse
from kivy.vector import Vector
# from random import randint



class LineGeneral():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.points = [x1, y1, x2, y2]

class Obstacle(LineGeneral):
    def __init__(self, x1,y1,x2,y2):
        super().__init__(x1,y1,x2,y2)

class Ray(LineGeneral):
    def __init__(self, x1,y1,x2,y2):
        super().__init__(x1,y1,x2,y2)

class Particle(Widget):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Movable = BooleanProperty(False)

    def on_touch_move(self, touch):
        self.center = [touch.x, touch.y]
    pass

class TelaPrincipal(FloatLayout):

    particle = ObjectProperty(None)
    rayQty = NumericProperty(4)

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Tick()
        
    def Tick(self):
        # Create rays
        for i in range(self.rayQty):
            direction = 200*Vector(1,1).rotate(i*360/self.rayQty)
            ray = Ray(self.center_x,self.center_y,self.center_x+direction[0],self.center_y+direction[1])
            with self.canvas:
                Line(points=ray.points, width=2)
        
        obst = Obstacle(450,200,500,400)

        interPoint = self.LineIntersection(ray.points, obst.points)
        print(interPoint)

        with self.canvas:
            Line(points=ray.points, width=2)
            Line(points=obst.points, width=2)

    def LineIntersection(self, line1, line2):
        x1,y1,x2,y2 = line1
        x3,y3,x4,y4 = line2

        numX = (x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)
        denX = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
        Px = numX/denX

        numY = (x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)
        denY = denX
        Py = numY/denY

        interPoint = [Px, Py]
        return interPoint
    

class RT2D_App(App):
    def build(self):
        tela = TelaPrincipal()
        #Clock.schedule_interval(tela.update,1.0/60.0)
        return tela

app = RT2D_App()
app.run()
        
    