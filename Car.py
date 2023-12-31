from jetbot import Robot
import time
from jetbot import Camera
.145
from jetbot import bgr8_to_jpeg
import traitlets
import ipywidgets.widgets as widgets
from curtsies import Input



robot = Robot()


button_layout = widgets.Layout(width='100px', height='80px', align_self='center')
stop_button = widgets.Button(description='stop', button_style='danger', layout=button_layout)
forward_button = widgets.Button(description='forward', layout=button_layout)
backward_button = widgets.Button(description='backward', layout=button_layout)
left_button = widgets.Button(description='left', layout=button_layout)
right_button = widgets.Button(description='right', layout=button_layout)

# display buttons
middle_box = widgets.HBox([left_button, stop_button, right_button], layout=widgets.Layout(align_self='center'))
controls_box = widgets.VBox([forward_button, middle_box, backward_button])
display(controls_box)
def stop(change):
    robot.stop()
    
def step_forward(change):
    robot.forward(0.6)


def step_backward(change):
    robot.backward(0.9)

def step_left(change):
    robot.right(0.5)


def step_right(change):
    robot.left(0.5)

# link buttons to actions
stop_button.on_click(stop)
forward_button.on_click(step_forward)
backward_button.on_click(step_backward)
left_button.on_click(step_left)
right_button.on_click(step_right)

#makes camera

image = widgets.Image(format='jpeg', width=300, height=300)

display(image)

camera = Camera.instance()

camera_link = traitlets.dlink((camera, 'value'), (image, 'value'), transform=bgr8_to_jpeg)
