# creating quad equation

import math
import os

# --- PREMIUM TERMINAL COLORS (ANSI ESCAPE CODES) ---
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
MAGENTA = '\033[95m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Screen clear karne ke liye
os.system('cls' if os.name == 'nt' else 'clear')

print(f"\n{BOLD}{MAGENTA}╔══════════════════════════════════════════════════════════╗{RESET}")
print(f"{BOLD}{MAGENTA}║{RESET} {BOLD}{CYAN}            🎯 DYNAMIC QUADRATIC GENERATOR            {RESET} {BOLD}{MAGENTA}║{RESET}")
print(f"{BOLD}{MAGENTA}╚══════════════════════════════════════════════════════════╝{RESET}\n")

try:
    # Tera original input logic (Bas UI colors ke sath)
    num = int(input(f"{BOLD}{YELLOW}👉 Enter a number: {RESET}"))
   
    a = num
    b = 2 * num
    c = num ** 2

    quadequation = f"{a}x² + {b}x + {c} = 0"
    
    # Equation display karne ka premium divider
    print(f"\n{CYAN}" + "═"*60 + f"{RESET}")
    print(f"{BOLD}{GREEN}✨ The quadratic equation is : {quadequation}{RESET}")
    print(f"{CYAN}" + "═"*60 + f"{RESET}\n")

    # Discriminant ka calculation
    d = b ** 2 - 4 * a * c
    
    print(f"{BOLD}{YELLOW}🔹 Discriminant (D) = {d}{RESET}\n")

    # --- TERA EXACT IF-ELSE LOGIC WITH PREMIUM BOXES ---
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        
        print(f"{BOLD}{CYAN}╔══════════════════════════════════════════════════════╗{RESET}")
        print(f"{BOLD}{CYAN}║{RESET} {BOLD}{GREEN}The roots of the quadratic equation are:{RESET}             {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}║{RESET}  ✅ Root 1 (Alpha) = {root1:<30} {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}║{RESET}  ✅ Root 2 (Beta)  = {root2:<30} {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════════════╝{RESET}\n")
        
    elif d == 0:
        root = -b / (2 * a)
        
        print(f"{BOLD}{CYAN}╔══════════════════════════════════════════════════════╗{RESET}")
        print(f"{BOLD}{CYAN}║{RESET} {BOLD}{MAGENTA}THE ROOTS ARE REAL AND EQUAL!{RESET}                        {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}║{RESET}  ✅ The root of the quadratic equation is: {root:<9} {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════════════╝{RESET}\n")
        
    else:
        print(f"{BOLD}{RED}╔══════════════════════════════════════════════════════╗{RESET}")
        print(f"{BOLD}{RED}║{RESET} ❌ The quadratic equation has no real roots.         {BOLD}{RED}║{RESET}")
        print(f"{BOLD}{RED}╚══════════════════════════════════════════════════════╝{RESET}\n")

except ValueError:
    print(f"\n{BOLD}{RED}[!] ERROR: Please enter a valid number!{RESET}\n")
