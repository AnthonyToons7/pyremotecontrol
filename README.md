# Pyremotecontrol
Use case: Whenever you want to control your laptop via phone, I dont know?

How it works: Starts a local server you can go to on your phone. You get the option to move your mouse, click, type, scroll, and thats about it. Anything pyautogui can do, you can do.

# Instructions
Drag the library into your project, then:

`pip install -e ./pyremotecontrol`

This should install the library. It's better if you work in local environment files.

Now, once installed, you need to import it into your project:

```
    import pyremotecontrol
    pyremotecontrol.start_server()
```

This will start your server. It will run on your local IP. If you dont know this, open your terminal and type

`ipconfig`

You want to look for something called `IPv4 Address`. Once you have your IP, add `:8000`, and you're ready to go.

Example: `123.456.7.8:8000`