

@app.route("/", methods=["GET"])
def get_content():
    file = open("content.html", "r")
    content = file.read()
    if content not '':
        return content

@app.route("/handler", methods=["POST"])
def handle():
    global moving, cordlst, previous_coordinates
    lst = []
    x_axis = float(request.form["a"])
    y_axis = float(request.form["b"])
    moving = True
    coordinates = (x_axis, y_axis)
    lx, ly = previous_coordinates
    cx, cy = coordinates
    threading.Thread(target=lambda: p.moveRel((cx - lx) * 2, (cy - ly) * 2)).start()
    previous_coordinates = coordinates


@app.route("/scroller", methods=["POST"])
def scrollerr() -> str:
    global moving, cordlst, lastcords2
    x_axis = float(request.form["a"])
    y_axis = float(request.form["b"])
    coordinates = (a, b)
    lx, ly = lastcords2
    cx, cy = coordinates
    if cy < ly:
        threading.Thread(target=lambda: p.scroll(30)).start()
    if cy > ly:
        threading.Thread(target=lambda: p.scroll(-30)).start()
    lastcords2 = coordinates


@app.route("/tstart", methods=["POST"])
def startt() -> str:
    global previous_coordinates, lastcords2
    x_axis = float(request.form["a"])
    y_axis = float(request.form["b"])
    previous_coordinates = (x_axis, y_axis)
    lastcords2 = (x_axis, y_axis)


@app.route("/click", methods=["POST"])
def do_click() -> str:
    global moving
    if not moving:
        a = request.form["a"]
        # print(a)
        a = float(a)
        if a < 400:
            p.click()
        if a >= 400:
            p.rightClick()

    moving = False


@app.route("/typed", methods=["POST"])
def typeit() -> str:
    global type_data, old_data
    data = request.form["data"]
    type_data = str(data)
    if len(type_data) > len(old_data):
        p.typewrite(type_data[len(type_data) - 1])
    else:
        p.press("backspace", len(old_data) - len(type_data))
    old_data = type_data


@app.route("/enter", methods=["POST"])
def slashN() -> str:
    p.press("enter")


@app.route("/drag", methods=["POST"])
def toggle_mouse_drag() -> str:
    global drag
    drag = not drag

    if drag:
        p.mouseDown()
    else:
        p.mouseUp()


def start_server(port=8000, print_msg=True):
    if print_msg:
        print("Server started at local_ip_of_this_pc:%s" % port)
        print("Print Ctrl+C to exit")
    app.run(host="0.0.0.0", port=port)