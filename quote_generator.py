import random
import json
import tkinter as tk
from quotes_areas import AREAS

def load_quotes(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def generate_quote(quotes):
    return random.choice(quotes)

def get_quotes_by_area(quotes, area):
    return [quote for quote in quotes if quote.get('area') == area]

def show_quote(quotes):
    root = tk.Tk()
    root.title("Quote")
    quote = random.choice(quotes)
    label = tk.Label(root, text=f'"{quote["quote"]}"\n\n- {quote["author"]}')
    label.pack(padx=10, pady=10)
    root.mainloop()

def main():
    areas = list(AREAS.keys())
    current_area_index = 0
    while True:
        area = areas[current_area_index]
        area_filename = AREAS.get(area)
        if not area_filename:
            raise ValueError(f"Invalid area '{area}'")
        area_quotes = load_quotes(area_filename)
        if not area_quotes:
            raise ValueError(f"No quotes found for area '{area}'")
        show_quote(area_quotes)
        current_area_index = (current_area_index + 1) % len(areas)

if __name__ == '__main__':
    main()