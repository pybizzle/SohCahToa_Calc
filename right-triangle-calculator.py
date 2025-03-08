import tkinter as tk
from tkinter import ttk, messagebox
import math
from PIL import Image, ImageTk, ImageDraw
import numpy as np

class RightTriangleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Right Triangle Calculator")
        self.geometry("1000x700")
        self.configure(bg="#f0f0f0")
        
        # Set app icon and styling
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', background='#007bff', foreground='white', font=('Arial', 10, 'bold'))
        self.style.map('TButton', background=[('active', '#0069d9')])
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 16, 'bold'))
        self.style.configure('Result.TLabel', font=('Arial', 12), background='#f0f0f0')
        
        # Main container
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create header
        header_label = ttk.Label(self.main_frame, text="Right Triangle Calculator", style='Header.TLabel')
        header_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Create left panel for inputs and right panel for visualization
        self.input_frame = ttk.Frame(self.main_frame)
        self.input_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 10))
        
        self.visual_frame = ttk.Frame(self.main_frame)
        self.visual_frame.grid(row=1, column=1, sticky="nsew")
        
        # Configure grid weights
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        
        # Input variables
        self.calculation_mode = tk.StringVar(value="sides")
        self.known_values = tk.StringVar(value="angle_side")
        
        self.side_a = tk.DoubleVar()  # Opposite
        self.side_b = tk.DoubleVar()  # Adjacent
        self.side_c = tk.DoubleVar()  # Hypotenuse
        self.angle_A = tk.DoubleVar()  # Opposite to side a
        self.angle_B = tk.DoubleVar()  # Opposite to side b
        
        # Create input controls
        self._create_input_controls()
        
        # Create visualization
        self._create_visualization()
        
        # Result section
        self.result_frame = ttk.Frame(self.main_frame)
        self.result_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(20, 0))
        
        # Result labels
        self.results = {
            "side_a": ttk.Label(self.result_frame, text="Side a (opposite): ", style='Result.TLabel'),
            "side_b": ttk.Label(self.result_frame, text="Side b (adjacent): ", style='Result.TLabel'),
            "side_c": ttk.Label(self.result_frame, text="Side c (hypotenuse): ", style='Result.TLabel'),
            "angle_A": ttk.Label(self.result_frame, text="Angle A (degrees): ", style='Result.TLabel'),
            "angle_B": ttk.Label(self.result_frame, text="Angle B (degrees): ", style='Result.TLabel'),
            "area": ttk.Label(self.result_frame, text="Area: ", style='Result.TLabel'),
            "perimeter": ttk.Label(self.result_frame, text="Perimeter: ", style='Result.TLabel')
        }
        
        for i, (key, label) in enumerate(self.results.items()):
            label.grid(row=i // 4, column=i % 4, padx=10, pady=5, sticky="w")
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        self.status_bar = ttk.Label(self, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def _create_input_controls(self):
        # Mode selection
        mode_frame = ttk.LabelFrame(self.input_frame, text="Calculation Mode")
        mode_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Radiobutton(mode_frame, text="Find missing sides and angles", 
                         variable=self.calculation_mode, value="sides").pack(anchor=tk.W, padx=5, pady=2)
        ttk.Radiobutton(mode_frame, text="Verify triangle", 
                         variable=self.calculation_mode, value="verify").pack(anchor=tk.W, padx=5, pady=2)
        
        # Known values selection
        known_frame = ttk.LabelFrame(self.input_frame, text="Known Values")
        known_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Radiobutton(known_frame, text="One angle and one side", 
                         variable=self.known_values, value="angle_side").pack(anchor=tk.W, padx=5, pady=2)
        ttk.Radiobutton(known_frame, text="Two sides", 
                         variable=self.known_values, value="two_sides").pack(anchor=tk.W, padx=5, pady=2)
        
        # Input values frame
        values_frame = ttk.LabelFrame(self.input_frame, text="Input Values")
        values_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Side inputs
        sides_frame = ttk.Frame(values_frame)
        sides_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(sides_frame, text="Side a (opposite):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Entry(sides_frame, textvariable=self.side_a, width=10).grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(sides_frame, text="Side b (adjacent):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Entry(sides_frame, textvariable=self.side_b, width=10).grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(sides_frame, text="Side c (hypotenuse):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Entry(sides_frame, textvariable=self.side_c, width=10).grid(row=2, column=1, padx=5, pady=2)
        
        # Angle inputs
        angles_frame = ttk.Frame(values_frame)
        angles_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(angles_frame, text="Angle A (degrees):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Entry(angles_frame, textvariable=self.angle_A, width=10).grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(angles_frame, text="Angle B (degrees):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Entry(angles_frame, textvariable=self.angle_B, width=10).grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(angles_frame, text="Angle C: 90°").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        
        # Buttons
        buttons_frame = ttk.Frame(values_frame)
        buttons_frame.pack(fill=tk.X, padx=5, pady=10)
        
        ttk.Button(buttons_frame, text="Calculate", command=self.calculate).grid(row=0, column=0, padx=5, pady=2)
        ttk.Button(buttons_frame, text="Clear", command=self.clear_inputs).grid(row=0, column=1, padx=5, pady=2)
        ttk.Button(buttons_frame, text="Show Example", command=self.show_example).grid(row=0, column=2, padx=5, pady=2)
    
    def _create_visualization(self):
        # Canvas for triangle visualization
        self.canvas_frame = ttk.LabelFrame(self.visual_frame, text="Triangle Visualization")
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.canvas = tk.Canvas(self.canvas_frame, bg="white", width=450, height=450)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create initial triangle image
        self.update_triangle()
    
    def update_triangle(self):
        """Update the triangle visualization based on current values."""
        # Clear canvas
        self.canvas.delete("all")
        
        # Create a base triangle image
        canvas_width = self.canvas.winfo_width() or 450
        canvas_height = self.canvas.winfo_height() or 450
        
        # Set default coordinates if not enough valid inputs
        try:
            # Try to calculate a triangle based on inputs
            sides = self._get_valid_sides()
            if sides:
                a, b, c = sides
                # Scale the triangle to fit the canvas
                scale = min(canvas_width, canvas_height) * 0.7 / max(a, b, c)
                
                # Triangle coordinates
                x1, y1 = 50, canvas_height - 50  # Bottom left (right angle)
                x2, y2 = x1 + b * scale, y1  # Bottom right
                x3, y3 = x1, y1 - a * scale  # Top left
                
                # Compute angles
                angle_A = math.degrees(math.asin(a / c))
                angle_B = math.degrees(math.acos(a / c))
            else:
                # Default triangle
                x1, y1 = 50, canvas_height - 50  # Bottom left (right angle)
                x2, y2 = x1 + 200, y1  # Bottom right
                x3, y3 = x1, y1 - 150  # Top left
                
                # Default values for display
                a, b, c = 150, 200, 250
                angle_A = 37  # Approximately asin(150/250)
                angle_B = 53  # Approximately acos(150/250)
        except Exception as e:
            # Fallback to default triangle if calculation fails
            x1, y1 = 50, canvas_height - 50  # Bottom left (right angle)
            x2, y2 = x1 + 200, y1  # Bottom right
            x3, y3 = x1, y1 - 150  # Top left
            
            # Default values for display
            a, b, c = 150, 200, 250
            angle_A = 37  # Approximately asin(150/250)
            angle_B = 53  # Approximately acos(150/250)
            self.status_var.set(f"Error calculating triangle: {str(e)}")
        
        # Draw triangle
        self.canvas.create_line(x1, y1, x2, y2, width=2)  # Bottom line (b)
        self.canvas.create_line(x1, y1, x3, y3, width=2)  # Left line (a)
        self.canvas.create_line(x3, y3, x2, y2, width=2)  # Hypotenuse (c)
        
        # Draw right angle symbol
        right_angle_size = 20
        self.canvas.create_line(x1, y1, x1 + right_angle_size, y1, width=1)
        self.canvas.create_line(x1, y1, x1, y1 - right_angle_size, width=1)
        self.canvas.create_line(x1 + right_angle_size, y1, x1 + right_angle_size, y1 - right_angle_size, width=1)
        self.canvas.create_line(x1, y1 - right_angle_size, x1 + right_angle_size, y1 - right_angle_size, width=1)
        
        # Draw labels
        # Sides
        self.canvas.create_text((x1 + x3) / 2 - 20, (y1 + y3) / 2, text=f"a = {a:.2f}", font=("Arial", 10, "bold"))
        self.canvas.create_text((x1 + x2) / 2, y1 + 20, text=f"b = {b:.2f}", font=("Arial", 10, "bold"))
        self.canvas.create_text((x2 + x3) / 2 + 20, (y2 + y3) / 2, text=f"c = {c:.2f}", font=("Arial", 10, "bold"))
        
        # Angles
        self.canvas.create_text(x2 - 30, y2 - 30, text=f"A = {angle_A:.1f}°", font=("Arial", 10, "bold"))
        self.canvas.create_text(x3 + 30, y3 + 30, text=f"B = {angle_B:.1f}°", font=("Arial", 10, "bold"))
        self.canvas.create_text(x1 - 30, y1 - 30, text="C = 90°", font=("Arial", 10, "bold"))
    
    def _get_valid_sides(self):
        """Get a valid set of sides for the triangle if possible."""
        a = self.side_a.get() if self.side_a.get() > 0 else 0
        b = self.side_b.get() if self.side_b.get() > 0 else 0
        c = self.side_c.get() if self.side_c.get() > 0 else 0
        
        # If we have enough information to determine the triangle
        if a > 0 and b > 0:
            c = math.sqrt(a**2 + b**2)
            return a, b, c
        elif a > 0 and c > 0 and c > a:
            b = math.sqrt(c**2 - a**2)
            return a, b, c
        elif b > 0 and c > 0 and c > b:
            a = math.sqrt(c**2 - b**2)
            return a, b, c
        
        # If we have angle A and one side
        angle_A_rad = math.radians(self.angle_A.get()) if self.angle_A.get() > 0 else 0
        if angle_A_rad > 0 and angle_A_rad < math.pi/2:
            if a > 0:
                c = a / math.sin(angle_A_rad)
                b = a / math.tan(angle_A_rad)
                return a, b, c
            elif b > 0:
                c = b / math.cos(angle_A_rad)
                a = b * math.tan(angle_A_rad)
                return a, b, c
            elif c > 0:
                a = c * math.sin(angle_A_rad)
                b = c * math.cos(angle_A_rad)
                return a, b, c
                
        # If we have angle B and one side
        angle_B_rad = math.radians(self.angle_B.get()) if self.angle_B.get() > 0 else 0
        if angle_B_rad > 0 and angle_B_rad < math.pi/2:
            if a > 0:
                c = a / math.cos(angle_B_rad)
                b = a * math.tan(angle_B_rad)
                return a, b, c
            elif b > 0:
                c = b / math.sin(angle_B_rad)
                a = b / math.tan(angle_B_rad)
                return a, b, c
            elif c > 0:
                a = c * math.cos(angle_B_rad)
                b = c * math.sin(angle_B_rad)
                return a, b, c
        
        return None
    
    def calculate(self):
        """Calculate missing values based on inputs."""
        try:
            # Collect input values
            a = self.side_a.get() if self.side_a.get() > 0 else None
            b = self.side_b.get() if self.side_b.get() > 0 else None
            c = self.side_c.get() if self.side_c.get() > 0 else None
            angle_A = self.angle_A.get() if self.angle_A.get() > 0 else None
            angle_B = self.angle_B.get() if self.angle_B.get() > 0 else None
            
            # Count valid inputs
            valid_inputs = sum(x is not None for x in [a, b, c, angle_A, angle_B])
            
            if valid_inputs < 2:
                self.status_var.set("Please enter at least two values to calculate.")
                return
            
            # Calculate missing values
            # If we have two sides, we can calculate everything
            if a is not None and b is not None:
                c = math.sqrt(a**2 + b**2)
                angle_A = math.degrees(math.atan(a/b))
                angle_B = 90 - angle_A
            elif a is not None and c is not None:
                if a > c:
                    self.status_var.set("Error: Side a cannot be greater than hypotenuse c.")
                    return
                b = math.sqrt(c**2 - a**2)
                angle_A = math.degrees(math.asin(a/c))
                angle_B = 90 - angle_A
            elif b is not None and c is not None:
                if b > c:
                    self.status_var.set("Error: Side b cannot be greater than hypotenuse c.")
                    return
                a = math.sqrt(c**2 - b**2)
                angle_B = math.degrees(math.asin(b/c))
                angle_A = 90 - angle_B
            
            # If we have one side and one angle
            elif a is not None and angle_A is not None:
                angle_B = 90 - angle_A
                c = a / math.sin(math.radians(angle_A))
                b = a / math.tan(math.radians(angle_A))
            elif a is not None and angle_B is not None:
                angle_A = 90 - angle_B
                c = a / math.cos(math.radians(angle_B))
                b = a * math.tan(math.radians(angle_B))
            elif b is not None and angle_A is not None:
                angle_B = 90 - angle_A
                c = b / math.cos(math.radians(angle_A))
                a = b * math.tan(math.radians(angle_A))
            elif b is not None and angle_B is not None:
                angle_A = 90 - angle_B
                c = b / math.sin(math.radians(angle_B))
                a = b / math.tan(math.radians(angle_B))
            elif c is not None and angle_A is not None:
                angle_B = 90 - angle_A
                a = c * math.sin(math.radians(angle_A))
                b = c * math.cos(math.radians(angle_A))
            elif c is not None and angle_B is not None:
                angle_A = 90 - angle_B
                a = c * math.cos(math.radians(angle_B))
                b = c * math.sin(math.radians(angle_B))
            else:
                self.status_var.set("Invalid combination of inputs.")
                return
            
            # Update inputs with calculated values
            self.side_a.set(a)
            self.side_b.set(b)
            self.side_c.set(c)
            self.angle_A.set(angle_A)
            self.angle_B.set(angle_B)
            
            # Calculate additional properties
            area = 0.5 * a * b
            perimeter = a + b + c
            
            # Update result labels
            self.results["side_a"].config(text=f"Side a (opposite): {a:.4f}")
            self.results["side_b"].config(text=f"Side b (adjacent): {b:.4f}")
            self.results["side_c"].config(text=f"Side c (hypotenuse): {c:.4f}")
            self.results["angle_A"].config(text=f"Angle A (deg): {angle_A:.4f}°")
            self.results["angle_B"].config(text=f"Angle B (deg): {angle_B:.4f}°")
            self.results["area"].config(text=f"Area: {area:.4f}")
            self.results["perimeter"].config(text=f"Perimeter: {perimeter:.4f}")
            
            # Update the triangle visualization
            self.update_triangle()
            
            # Verify Pythagorean theorem
            pythag_diff = abs(c**2 - (a**2 + b**2))
            if pythag_diff > 1e-10:
                self.status_var.set(f"Warning: Triangle does not satisfy Pythagorean theorem. Difference: {pythag_diff:.10f}")
            else:
                self.status_var.set("Calculation complete. Triangle is valid.")
                
        except Exception as e:
            self.status_var.set(f"Error during calculation: {str(e)}")
    
    def clear_inputs(self):
        """Clear all input fields."""
        self.side_a.set(0)
        self.side_b.set(0)
        self.side_c.set(0)
        self.angle_A.set(0)
        self.angle_B.set(0)
        
        # Clear results
        for label in self.results.values():
            label.config(text=label.cget("text").split(":")[0] + ": ")
        
        # Reset triangle visualization
        self.update_triangle()
        self.status_var.set("Ready")
    
    def show_example(self):
        """Load example values."""
        self.side_a.set(3)
        self.side_b.set(4)
        self.side_c.set(5)
        self.angle_A.set(0)  # Will be calculated
        self.angle_B.set(0)  # Will be calculated
        self.calculate()
        self.status_var.set("Example loaded: 3-4-5 right triangle")

    def to_dms(self, decimal_degrees):
        """Convert decimal degrees to degrees, minutes, seconds format."""
        degrees = int(decimal_degrees)
        minutes_decimal = (decimal_degrees - degrees) * 60
        minutes = int(minutes_decimal)
        seconds = (minutes_decimal - minutes) * 60
        return f"{degrees}° {minutes}' {seconds:.2f}\""


if __name__ == "__main__":
    app = RightTriangleCalculator()
    app.mainloop()
