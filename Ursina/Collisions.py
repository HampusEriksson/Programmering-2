# https://www.ursinaengine.org/collision.html

from UrsinaClasses import *

app = Ursina()
window.size=(1600,1000)

window.fps_counter.enabled = True
window.exit_button.enabled = False

updatecount = 0

def update():
    destroylist = []
    print(len(obstacles))
    global updatecount
    updatecount += 1

    direction = Vec3(
        player.forward * (held_keys['w'] - held_keys['s'])
        + player.right * (held_keys['d'] - held_keys['a'])
    ).normalized()  # get the direction we're trying to walk in.

    origin = player.world_position + (
                player.up * .5)  # the ray should start slightly up from the ground so we can walk up slopes or walk over small objects.
    hit_info = boxcast(origin, direction, thickness = (3,3), ignore=(player,), distance=0.55, debug=True)
    print("Träff" if hit_info.hit else "Ingen träff")
    if not hit_info.hit:
        player.position += direction * 5 * time.dt

    player.x += held_keys["d"] * 5 * time.dt - held_keys["a"] * 5 * time.dt
    #player.z += held_keys["s"] * -2 * time.dt + held_keys["w"] * 5 * time.dt

    if updatecount % 60 == 0:
        obstacles.append(Ground(position = (player.x+random.randint(-5,5),player.y,player.z + random.randint(8,13))))

    #if all(not player.intersects(obstacle).hit for obstacle in obstacles):
    #    player.z += 5 * time.dt

    for obstacle in obstacles:

        #if player.intersects(obstacle).hit:
        #    player.z -= 5 * time.dt

        if obstacle.z < player.z:
            destroylist.append(obstacle)

    for o in destroylist:
        o.disabled = True

player = Entity(parent=scene,
            position=(10,0,20),
            model="cube",
            texture="white_cube",
            color=color.red,
            collider='box')

#sky = Sky()
camera.parent = player
camera.position = (0, 11, -15)
camera.rotation = (30, 0, 0)
obstacles = []
#Startar appen
app.run()
