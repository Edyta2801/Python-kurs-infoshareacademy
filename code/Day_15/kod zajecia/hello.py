import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# wiadomosc wyswietlana
message = "Welcome"

# handler - funkcja wywołana na skutek jakiegos zdarzenia (eventu)
def click():
    """Handler for mouse click"""
    global message
    message = "Good job!"

def draw(canvas):
    """Handler przerysowujący okno"""
    # wypisujemy wiadomosc na ekranie
    canvas.draw_text(message, [50,112], 48, "Red")


# tworzymy okno
frame = simplegui.create_frame("Home", 300, 200)

# dodajemy przycisk do naszego okna, podajemy:
# napis na przycisku, oraz handler, który będzie uruchomiony po naci-
# snieciu przycisku
frame.add_button("Click me", click)

# ustawiamy handler, ktory bedzie wykonywany podczas każdego
# odświeżenia okna (w zalezności od sprzętu od 60 do 120 MHz)
frame.set_draw_handler(draw)

# uruchamiamy okno
frame.start()
