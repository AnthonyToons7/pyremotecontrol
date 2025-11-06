import logging
import sys
import os
import threading
import pyautogui
from flask import Flask, request

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask('app')

moving = False
drag = False
type_data = ''
old_data = ''
coords = (0, 0)
previous_mouse_coordinates = (0, 0)
previous_scroll_coordinates = (0, 0)
coordinates = [(0, 0)]

def start_server(port=8000, print_msg=True):
    if print_msg:
        print('Server started')
    app.run(host='0.0.0.0', port=port, debug=False)

@app.route('/', methods=['GET'])
def get_content():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, 'core', 'content.html')

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    if content != '':
        return content
    return 'No content found.'

@app.route('/handler', methods=['POST'])
def handle():
    global moving, previous_mouse_coordinates
    x_axis = float(request.form['x_axis'])
    y_axis = float(request.form['y_axis'])
    moving = True
    coordinates = (x_axis, y_axis)
    lx, ly = previous_mouse_coordinates
    cx, cy = coordinates
    threading.Thread(target=lambda: pyautogui.moveRel((cx - lx) * 4, (cy - ly) * 4)).start()
    previous_mouse_coordinates = coordinates
    return ''


@app.route('/scroller', methods=['POST'])
def scroll():
    global moving, previous_scroll_coordinates
    x_axis = float(request.form['x_axis'])
    y_axis = float(request.form['y_axis'])
    coordinates = (x_axis, y_axis)
    lx, ly = previous_scroll_coordinates
    cx, cy = coordinates
    if cy < ly:
        threading.Thread(target=lambda: pyautogui.scroll(50)).start()
    elif cy > ly:
        threading.Thread(target=lambda: pyautogui.scroll(-50)).start()
    previous_scroll_coordinates = coordinates
    return ''

@app.route('/tstart', methods=['POST'])
def start():
    global previous_mouse_coordinates, previous_scroll_coordinates
    x_axis = float(request.form['x_axis'])
    y_axis = float(request.form['y_axis'])
    previous_mouse_coordinates = (x_axis, y_axis)
    previous_scroll_coordinates = (x_axis, y_axis)
    return ''

@app.route('/click', methods=['POST'])
def click():
    global moving
    if not moving:
        print(request.form)
        x_axis = request.form['x_axis']
        x_axis = float(x_axis)
        if x_axis < 400:
            pyautogui.click()
        if x_axis >= 400:
            pyautogui.rightClick()

    moving = False
    return ''

@app.route('/typed', methods=['POST'])
def typing():
    global type_data, old_data
    data = request.form['data']
    type_data = str(data)
    if len(type_data) > len(old_data):
        pyautogui.typewrite(type_data[len(type_data) - 1])
    else:
        pyautogui.press('backspace', len(old_data) - len(type_data))
    old_data = type_data
    return ''

@app.route('/enter', methods=['POST'])
def enter():
    pyautogui.press('enter')
    return ''

@app.route('/drag', methods=['POST'])
def toggle_mouse_drag():
    global drag
    drag = not drag

    if drag:
        pyautogui.mouseDown()
    else:
        pyautogui.mouseUp()
    return ''