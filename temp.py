# task3_temp_converter.py

def c_to_f(c): return (c * 9/5) + 32
def c_to_k(c): return c + 273.15

def f_to_c(f): return (f - 32) * 5/9
def f_to_k(f): return f_to_c(f) + 273.15

def k_to_c(k): return k - 273.15
def k_to_f(k): return c_to_f(k_to_c(k))

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number.")

def main():
    print("=== Temperature Converter ===")
    print("Choose input scale: 1) Celsius  2) Fahrenheit  3) Kelvin")
    choice = input("Enter 1/2/3: ").strip()

    if choice == "1":
        c = get_float("Enter °C: ")
        print(f"{c:.2f} °C = {c_to_f(c):.2f} °F")
        print(f"{c:.2f} °C = {c_to_k(c):.2f} K")
    elif choice == "2":
        f = get_float("Enter °F: ")
        print(f"{f:.2f} °F = {f_to_c(f):.2f} °C")
        print(f"{f:.2f} °F = {f_to_k(f):.2f} K")
    elif choice == "3":
        k = get_float("Enter K: ")
        if k < 0:
            print("Kelvin cannot be negative.")
            return
        print(f"{k:.2f} K = {k_to_c(k):.2f} °C")
        print(f"{k:.2f} K = {k_to_f(k):.2f} °F")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
