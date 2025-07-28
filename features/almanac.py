import tkinter as tk
from PIL import Image, ImageTk
import os

class AlmanacFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg="#ffeaf5")

        moon_phase_name = "Waxing Gibbous"
        moon_emoji = "🌔"

        tk.Label(self, text="★ Almanac ★", font=("Press Start 2P", 14), bg="#ffeaf5", fg="#ff69b4").pack(pady=(10, 5))

        # Sparkles
        self.sparkle_label = tk.Label(self, text="", font=("Arial", 14), bg="#ffeaf5", fg="#ffb3da")
        self.sparkle_label.pack()

        # Moon phase chart
        tk.Label(self, text="🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘", font=("Arial", 18), bg="#ffeaf5").pack(pady=(20, 5))
        tk.Label(self, text=f"Today’s phase: {moon_emoji} {moon_phase_name}", font=("Arial", 12, "bold"), bg="#ffeaf5", fg="#333").pack()

        # Banner
        try:
            banner_path = os.path.join("assets", "almanac.png")
            moon_banner = Image.open(banner_path)
            moon_banner.thumbnail((280, 100), Image.LANCZOS)
            self.banner_img = ImageTk.PhotoImage(moon_banner)
            tk.Label(self, image=self.banner_img, bg="#ffeaf5").pack(pady=(20, 5))
        except:
            tk.Label(self, text="(Moon banner missing)", bg="#ffeaf5").pack()

        # Cute footer
        tk.Label(self, text="✧ ✦ Stay lunar ✦ ✧", font=("Arial", 11), bg="#ffeaf5", fg="#999").pack(pady=(10, 2))

        # Moon friend character
        try:
            friend_path = os.path.join("assets", "its_just_a_phase.png")
            friend_img = Image.open(friend_path).resize((70, 70), Image.LANCZOS)
            self.friend_img = ImageTk.PhotoImage(friend_img)
            self.friend = tk.Label(self, image=self.friend_img, bg="#ffeaf5", bd=0)
            self.friend.place(x=200, y=312)  # adjust x/y if needed
        except Exception as e:
            print("🚫 Moon friend failed to load:", e)
            self.friend = None

        self.has_animated = False
        self.jump_up = True
        self.sparkles = ["✦", "✧", "✦", "✧", "✦"]
        self.sparkle_index = 0

    def on_show(self):
        if not self.has_animated:
            self.has_animated = True
            self.animate_sparkles()
            self.animate_friend()

    def animate_sparkles(self):
        if self.sparkle_index <= len(self.sparkles):
            sparkle_text = " ".join(self.sparkles[:self.sparkle_index])
            self.sparkle_label.config(text=sparkle_text)
            self.sparkle_index += 1
            self.after(300, self.animate_sparkles)

    def animate_friend(self):
        if self.friend:
            x = self.friend.winfo_x()
            y = self.friend.winfo_y()
            new_y = y - 3 if self.jump_up else y + 3
            self.friend.place(x=x, y=new_y)
            self.jump_up = not self.jump_up
            self.after(300, self.animate_friend)
