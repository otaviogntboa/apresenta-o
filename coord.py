from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:  
        print(f"Coordenadas capturadas: X={x}, Y={y}")


with mouse.Listener(on_click=on_click) as listener:
    print("Clique em qualquer lugar para capturar as coordenadas. Pressione Ctrl+C para sair.")
    listener.join()
