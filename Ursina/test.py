from ursina import *

if __name__ == '__main__':
    app = Ursina()

camera.fov = 4

bg = Entity(parent=scene, model='quad', texture='shore', scale=(16,8), z=10, color=color.light_gray)






if __name__ == '__main__':
    app.run()