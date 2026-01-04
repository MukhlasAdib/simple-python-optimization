import os
import tkinter as tk
from tkinter import filedialog

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600


class PolygonDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Polygon Drawer")

        self.canvas = tk.Canvas(
            root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white"
        )
        self.canvas.pack()

        self.save_button = tk.Button(
            root, text="Save Last Polygon", command=self.save_polygon
        )
        self.save_button.pack(pady=5)

        self.current_points = []
        self.polygons = []  # list of polygons, each polygon is a list of (x, y)
        self.temp_line = None

        self.canvas.bind("<Button-1>", self.add_point)  # left click
        self.canvas.bind("<Button-3>", self.finish_polygon)  # right click
        self.canvas.bind("<Motion>", self.update_temp_line)

    def add_point(self, event):
        x, y = event.x, event.y
        self.current_points.append((x, y))

        r = 3
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="black")

        if len(self.current_points) > 1:
            x1, y1 = self.current_points[-2]
            self.canvas.create_line(x1, y1, x, y)

    def update_temp_line(self, event):
        if len(self.current_points) >= 1:
            if self.temp_line:
                self.canvas.delete(self.temp_line)

            x1, y1 = self.current_points[-1]
            self.temp_line = self.canvas.create_line(
                x1, y1, event.x, event.y, dash=(4, 2)
            )

    def finish_polygon(self, event=None):
        if len(self.current_points) < 3:
            self.current_points.clear()
            return

        # close polygon
        x1, y1 = self.current_points[-1]
        x0, y0 = self.current_points[0]
        self.canvas.create_line(x1, y1, x0, y0)

        self.polygons.append(self.current_points.copy())
        self.current_points.clear()

        if self.temp_line:
            self.canvas.delete(self.temp_line)
            self.temp_line = None

    def save_polygon(self):
        save_dir = "polygons"
        os.makedirs(save_dir, exist_ok=True)
        for i, polygon in enumerate(self.polygons):
            normalized = [(x / CANVAS_WIDTH, y / CANVAS_HEIGHT) for x, y in polygon]
            save_path = os.path.join(save_dir, f"polygon_{i}.txt")
            with open(save_path, "w") as f:
                for x, y in normalized:
                    f.write(f"{x:.6f} {y:.6f}\n")

            print("Polygon saved:", save_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = PolygonDrawer(root)
    root.mainloop()
