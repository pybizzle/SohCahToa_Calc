# SohCahToa Right Triangle Calculator

![SohCahToa](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Right_triangle_with_sine_and_cosine.svg/240px-Right_triangle_with_sine_and_cosine.svg.png)

An interactive right triangle calculator with visualization, built in Python using Tkinter. This application helps students, engineers, and anyone working with geometry to quickly calculate and visualize right triangle properties.

## Features

- **Interactive Calculation**: Find missing sides and angles by entering just two known values
- **Real-time Visualization**: See a dynamically rendered triangle that updates as you input values
- **Multiple Calculation Modes**:
  - Find missing sides and angles
  - Verify if a triangle is valid (checks Pythagorean theorem)
- **Various Input Combinations**:
  - Two sides
  - One angle and one side
- **Comprehensive Results**:
  - All sides and angles
  - Area and perimeter
  - DMS (Degrees, Minutes, Seconds) conversion
- **User-Friendly Interface**:
  - Clear input sections
  - Result displays
  - Status notifications
  - Example loading

## Requirements

- Python 3.x
- Tkinter (included in standard Python installation)
- PIL (Python Imaging Library) / Pillow
- NumPy

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/SohCahToa_Calc.git
   cd SohCahToa_Calc
   ```

2. Install required dependencies:
   ```bash
   pip install pillow numpy
   ```

## Usage

Run the application from the command line:

```bash
python right-triangle-calculator.py
```

### How to Use

1. **Input Values**: Enter any two values (sides or angles) in the appropriate fields
2. **Calculate**: Click the "Calculate" button to compute all missing values
3. **View Results**: See the calculated values and the visualized triangle
4. **Clear**: Reset all inputs and results with the "Clear" button
5. **Example**: Load a 3-4-5 example triangle with the "Show Example" button

## How It Works

The calculator uses trigonometric principles and the Pythagorean theorem to solve right triangles:

- **SOH**: Sine = Opposite / Hypotenuse
- **CAH**: Cosine = Adjacent / Hypotenuse
- **TOA**: Tangent = Opposite / Adjacent
- **Pythagorean Theorem**: a² + b² = c² (where c is the hypotenuse)

## Mathematical Formulas

### Side Calculations
- If sides a and b are known: c = √(a² + b²)
- If side a and hypotenuse c are known: b = √(c² - a²)
- If side b and hypotenuse c are known: a = √(c² - b²)

### Angle Calculations
- If sides a and b are known: angle A = arctan(a/b)
- If side a and hypotenuse c are known: angle A = arcsin(a/c)
- If side b and hypotenuse c are known: angle B = arcsin(b/c)

### Additional Properties
- Area = (1/2) × a × b
- Perimeter = a + b + c

## Screenshots

*[Add screenshots of your application here]*

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/SohCahToa_Calc/issues).

## Acknowledgements

- This calculator was originally created as a weekend challenge and learning project
- Special thanks to the Python and Tkinter communities for their excellent documentation
