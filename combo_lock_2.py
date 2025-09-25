import tkinter as tk
import math


class CombinationLock:
    def __init__(self, root):
        self.root = root
        self.root.title("Combination Lock Simulator")
        self.root.geometry("500x600")
        self.root.configure(bg="#2c3e50")

        # Lock settings
        self.combination = [15, 35, 8]  # The correct combination
        self.current_sequence = []
        self.dial_angle = 0  # Current angle of the dial
        self.is_dragging = False
        self.last_mouse_angle = 0
        self.latch_open = False

        # Colors
        self.bg_color = "#2c3e50"
        self.dial_color = "#34495e"
        self.number_color = "#ecf0f1"
        self.pointer_color = "#e74c3c"
        self.latch_color = "#95a5a6"
        self.open_latch_color = "#27ae60"

        self.setup_ui()

    def setup_ui(self):
        # Title and combination display
        title_frame = tk.Frame(self.root, bg=self.bg_color)
        title_frame.pack(pady=5)

        tk.Label(
            title_frame,
            text="Combination Lock",
            font=("Arial", 20, "bold"),
            fg=self.number_color,
            bg=self.bg_color,
        ).pack()

        tk.Label(
            title_frame,
            text=f"Combination: {'-'.join(map(str, self.combination))}",
            font=("Arial", 14),
            fg="#f39c12",
            bg=self.bg_color,
        ).pack(pady=5)

        # Current sequence display
        self.sequence_label = tk.Label(
            title_frame,
            text="Entered: []",
            font=("Arial", 12),
            fg=self.number_color,
            bg=self.bg_color,
        )
        self.sequence_label.pack(pady=5)

        # Instructions
        instructions = tk.Label(
            title_frame,
            text="Drag the dial to enter numbers, then click the latch to open",
            font=("Arial", 10),
            fg="#bdc3c7",
            bg=self.bg_color,
        )
        instructions.pack(pady=5)

        # Main canvas for the lock
        self.canvas = tk.Canvas(
            self.root, width=400, height=400, bg=self.bg_color, highlightthickness=0
        )
        self.canvas.pack(pady=5)

        # Reset button
        reset_btn = tk.Button(
            self.root,
            text="Reset",
            command=self.reset_lock,
            font=("Arial", 12),
            bg="#e67e22",
            fg="white",
            activebackground="#d35400",
            relief="flat",
            pady=5,
        )
        reset_btn.pack(pady=5)

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

        self.draw_lock()

    def draw_lock(self):
        self.canvas.delete("all")

        center_x, center_y = 200, 165
        dial_radius = 120

        # Draw outer ring of lock
        self.canvas.create_oval(
            center_x - dial_radius - 20,
            center_y - dial_radius - 20,
            center_x + dial_radius + 20,
            center_y + dial_radius + 20,
            fill="#34495e",
            outline="#2c3e50",
            width=3,
        )

        # Draw main dial
        self.canvas.create_oval(
            center_x - dial_radius,
            center_y - dial_radius,
            center_x + dial_radius,
            center_y + dial_radius,
            fill=self.dial_color,
            outline="#2c3e50",
            width=2,
        )

        # Draw numbers around the dial
        for i in range(40):  # 0-39 numbers
            angle = math.radians(i * 9 - self.dial_angle)  # 9 degrees per number
            number_radius = dial_radius # - 5

            x = center_x + number_radius * math.cos(angle)
            y = center_y + number_radius * math.sin(angle)

            # Highlight every 5th number
            if i % 5 == 0:
                font_size = 12
                color = "#f39c12"
            else:
                font_size = 10
                color = self.number_color

            self.canvas.create_text(
                x, y, text=str(i), fill=color, font=("Arial", font_size, "bold")
            )

        # Draw center hub
        self.canvas.create_oval(
            center_x - 15,
            center_y - 15,
            center_x + 15,
            center_y + 15,
            fill="#2c3e50",
            outline="#34495e",
            width=2,
        )

        # Draw pointer at top (fixed position)
        pointer_y = center_y - dial_radius - 35
        self.canvas.create_polygon(
            center_x + 8,
            pointer_y - 15,
            center_x - 8,
            pointer_y - 15,
            center_x,
            pointer_y + 8,
            fill=self.pointer_color,
            outline="#d13423",
            width=2,
        )

        # Draw latch
        latch_color = self.open_latch_color if self.latch_open else self.latch_color
        latch_y = center_y + dial_radius + 40

        if self.latch_open:
            # Draw open latch (moved down)
            self.canvas.create_rectangle(
                center_x - 20,
                latch_y + 10,
                center_x + 20,
                latch_y + 30,
                fill=latch_color,
                outline="#27ae60",
                width=2,
                tags="latch",
            )
            self.canvas.create_text(
                center_x,
                latch_y + 20,
                text="OPEN",
                fill="white",
                font=("Arial", 8, "bold"),
            )
        else:
            # Draw closed latch
            self.canvas.create_rectangle(
                center_x - 20,
                latch_y + 10,
                center_x + 20,
                latch_y + 30,
                fill=latch_color,
                outline="#7f8c8d",
                width=2,
                tags="latch",
            )
            self.canvas.create_text(
                center_x,
                latch_y + 20,
                text="CLOSE",
                fill="white",
                font=("Arial", 8, "bold"),
            )

    def get_mouse_angle(self, event):
        center_x, center_y = 200, 200
        dx = event.x - center_x
        dy = event.y - center_y
        return math.degrees(math.atan2(dy, dx))

    def on_mouse_down(self, event):
        # Check if clicking on latch
        if self.canvas.find_closest(event.x, event.y)[0] in self.canvas.find_withtag(
            "latch"
        ):
            self.try_open_latch()
            return

        # Check if clicking on dial area
        center_x, center_y = 200, 200
        distance = math.sqrt((event.x - center_x) ** 2 + (event.y - center_y) ** 2)

        if distance <= 120:  # Within dial radius
            self.is_dragging = True
            self.last_mouse_angle = self.get_mouse_angle(event)

    def on_mouse_drag(self, event):
        if not self.is_dragging:
            return

        current_angle = self.get_mouse_angle(event)
        angle_diff = current_angle - self.last_mouse_angle

        # Handle angle wrap-around
        if angle_diff > 180:
            angle_diff -= 360
        elif angle_diff < -180:
            angle_diff += 360

        self.dial_angle += angle_diff
        self.dial_angle = self.dial_angle % 360

        self.last_mouse_angle = current_angle
        self.draw_lock()

    def on_mouse_up(self, event):
        if self.is_dragging:
            self.is_dragging = False
            # Record the number the pointer is pointing to
            self.record_current_number()

    def record_current_number(self):
        # Calculate which number the pointer is currently pointing to
        # The pointer is at the top, so we need to find which number is at angle 270 degrees (top)
        pointer_angle = 270  # Top position
        adjusted_angle = (pointer_angle + self.dial_angle) % 360

        # Each number is 9 degrees apart
        number = int((adjusted_angle / 9) + 0.5) % 40

        self.current_sequence.append(number)

        # Keep only the last 3 numbers (length of combination)
        if len(self.current_sequence) > len(self.combination):
            self.current_sequence = self.current_sequence[-len(self.combination) :]

        # Update display
        self.sequence_label.config(text=f"Entered: {self.current_sequence}")

    def try_open_latch(self):
        if len(self.current_sequence) == len(self.combination):
            if self.current_sequence == self.combination:
                self.latch_open = True
                self.sequence_label.config(text=" UNLOCKED! ", fg="#27ae60")
            else:
                self.sequence_label.config(text=" Wrong combination! ", fg="#e74c3c")
                # Reset after wrong attempt
                self.root.after(1500, self.reset_sequence)
        else:
            self.sequence_label.config(
                text="Enter complete combination first!", fg="#f39c12"
            )

        self.draw_lock()

    def reset_sequence(self):
        self.current_sequence = []
        self.sequence_label.config(text="Entered: []", fg=self.number_color)

    def reset_lock(self):
        self.current_sequence = []
        self.dial_angle = 0
        self.latch_open = False
        self.sequence_label.config(text="Entered: []", fg=self.number_color)
        self.draw_lock()


def main():
    root = tk.Tk()
    # app = 
    CombinationLock(root)
    root.mainloop()


if __name__ == "__main__":
    main()
