import math
import os

CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
MAGENTA = '\033[95m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Exact 10th class trig table mapping (with roots)
exact_values = {
    0:  {"sin": "0",      "cos": "1",      "tan": "0",      "cosec": "Not Defined (∞)", "sec": "1",      "cot": "Not Defined (∞)"},
    30: {"sin": "1/2",    "cos": "√3/2",   "tan": "1/√3",   "cosec": "2",               "sec": "2/√3",   "cot": "√3"},
    45: {"sin": "1/√2",   "cos": "1/√2",   "tan": "1",      "cosec": "√2",              "sec": "√2",     "cot": "1"},
    60: {"sin": "√3/2",   "cos": "1/2",    "tan": "√3",     "cosec": "2/√3",            "sec": "2",      "cot": "1/√3"},
    90: {"sin": "1",      "cos": "0",      "tan": "Not Defined (∞)", "cosec": "1",               "sec": "Not Defined (∞)", "cot": "0"}
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(f"\n{BOLD}{MAGENTA}╔══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{MAGENTA}║{RESET} {BOLD}{CYAN}                 📐 T-CALCULATOR V3 PRO                 {RESET} {BOLD}{MAGENTA}║{RESET}")
    print(f"{BOLD}{MAGENTA}╚══════════════════════════════════════════════════════════╝{RESET}\n")

# Program Start
clear_screen()
print_header()

while True:
    try:
        print(f"{BOLD}{YELLOW}👉 Enter angle in degrees {RESET}{CYAN}(or type 'q' to quit): {RESET}", end="")
        user_input = input().strip()
        
        if user_input.lower() == 'q':
            print(f"\n{BOLD}{GREEN}👋 Thanks for using T-Calculator Pro!{RESET}\n")
            break
            
        a = int(user_input)
        angle = math.radians(a)

        # --- MATH LOGIC ---
        sin_dec = round(math.sin(angle), 4)
        cos_dec = round(math.cos(angle), 4)
        
        tan_dec = "Not Defined (∞)" if a % 180 == 90 else round(math.tan(angle), 4)
        cosec_dec = "Not Defined (∞)" if sin_dec == 0.0 else round(1 / sin_dec, 4)
        sec_dec = "Not Defined (∞)" if cos_dec == 0.0 else round(1 / cos_dec, 4)
        
        if tan_dec == "Not Defined (∞)": cot_dec = 0.0
        elif tan_dec == 0.0: cot_dec = "Not Defined (∞)"
        else: cot_dec = round(1 / tan_dec, 4)

        if a in exact_values:
            exact = exact_values[a]
        else:
            exact = {"sin": "-", "cos": "-", "tan": "-", "cosec": "-", "sec": "-", "cot": "-"}

        # --- PREMIUM TABLE UI ---
        clear_screen()
        print_header()
        
        print(f"{BOLD}{CYAN}╔══════════════════════════════════════════════════════════╗{RESET}")
        print(f"{BOLD}{CYAN}║{RESET}                 {BOLD}{YELLOW}🎯 RESULTS FOR {a}°{RESET}                        {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}╠═════════════╦══════════════════════╦═════════════════════╣{RESET}")
        print(f"{BOLD}{CYAN}║{RESET} {BOLD}Ratio{RESET}       {BOLD}{CYAN}║{RESET}  {BOLD}Decimal Value{RESET}       {BOLD}{CYAN}║{RESET}  {BOLD}Exact Fraction{RESET}     {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}╠═════════════╬══════════════════════╬═════════════════════╣{RESET}")
        
        # Rows
        print(f"{BOLD}{CYAN}║{RESET} {GREEN}Sin({a:<2}°){RESET}    {BOLD}{CYAN}║{RESET}  {str(sin_dec):<19} {BOLD}{CYAN}║{RESET}  {MAGENTA}{exact['sin']:<18}{RESET} {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}║{RESET} {GREEN}Cos({a:<2}°){RESET}    {BOLD}{CYAN}║{RESET}  {str(cos_dec):<19} {BOLD}{CYAN}║{RESET}  {MAGENTA}{exact['cos']:<18}{RESET} {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}║{RESET} {GREEN}Tan({a:<2}°){RESET}    {BOLD}{CYAN}║{RESET}  {str(tan_dec):<19} {BOLD}{CYAN}║{RESET}  {MAGENTA}{exact['tan']:<18}{RESET} {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}║{RESET} {GREEN}Cosec({a:<2}°){RESET}  {BOLD}{CYAN}║{RESET}  {str(cosec_dec):<19} {BOLD}{CYAN}║{RESET}  {MAGENTA}{exact['cosec']:<18}{RESET} {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}║{RESET} {GREEN}Sec({a:<2}°){RESET}    {BOLD}{CYAN}║{RESET}  {str(sec_dec):<19} {BOLD}{CYAN}║{RESET}  {MAGENTA}{exact['sec']:<18}{RESET} {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}║{RESET} {GREEN}Cot({a:<2}°){RESET}    {BOLD}{CYAN}║{RESET}  {str(cot_dec):<19} {BOLD}{CYAN}║{RESET}  {MAGENTA}{exact['cot']:<18}{RESET} {BOLD}{CYAN}║{RESET}")
        print(f"{BOLD}{CYAN}╚═════════════╩══════════════════════╩═════════════════════╝{RESET}\n")

    except ValueError:
        print(f"\n{BOLD}{RED}[!] ERROR: Please enter a valid number!{RESET}\n")
