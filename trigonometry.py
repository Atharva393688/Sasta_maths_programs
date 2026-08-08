import time
import os

# --- PREMIUM TERMINAL COLORS (ANSI ESCAPE CODES) ---
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
MAGENTA = '\033[95m'
BOLD = '\033[1m'
RESET = '\033[0m'

def clear_screen():
    # Yeh Windows aur Mac/Linux dono pe screen clean kar dega
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print(f"\n{BOLD}{MAGENTA}╔══════════════════════════════════════════════════════════╗{RESET}")
    # Title ko center mein set karne ke liye
    padded_title = title.upper().center(56, ' ')
    print(f"{BOLD}{MAGENTA}║{RESET} {BOLD}{CYAN}{padded_title}{RESET} {BOLD}{MAGENTA}║{RESET}")
    print(f"{BOLD}{MAGENTA}╚══════════════════════════════════════════════════════════╝{RESET}\n")


def measuresinp():
    clear_screen()
    print_header("📐 T-CALCULATOR: MEASUREMENTS")
    while True:
        try:
            hypotenutsinp = int(input(f"{BOLD}{YELLOW}👉 Enter the measurement of HYPOTENUSE (in cm)    : {RESET}"))
            perpendicularinp = int(input(f"{BOLD}{YELLOW}👉 Enter the measurement of PERPENDICULAR (in cm): {RESET}"))
            baseinp = int(input(f"{BOLD}{YELLOW}👉 Enter the measurement of BASE (in cm)         : {RESET}"))
            
            print(f"{MAGENTA}" + "-" * 60 + f"{RESET}") 

            # Tumhara original error handling logic (with RED colors)
            if hypotenutsinp <= perpendicularinp:
                print(f"{BOLD}{RED}[!] ERROR: Hypotenuse cannot be smaller than or equal to Perpendicular.\n{RESET}")
                continue

            elif hypotenutsinp <= baseinp:
                print(f"{BOLD}{RED}[!] ERROR: Hypotenuse cannot be smaller than or equal to Base.\n{RESET}")
                continue    

            elif hypotenutsinp == 0 or baseinp == 0 or perpendicularinp == 0:
                print(f"{BOLD}{RED}[!] ERROR: Please enter real values (greater than 0).\n{RESET}")
                continue
            
            else:
                return hypotenutsinp, perpendicularinp, baseinp
                
        except ValueError:
            print(f"{BOLD}{RED}[!] ERROR: Please enter valid numbers only!\n{RESET}")
            continue

# Values input lena
hypotenus, pependicular, base = measuresinp()

def format_output(ratio_name, decimal_val, fraction_val):
    clear_screen()
    print_header(f"🎯 {ratio_name} THETA RESULT")
    
    print(f"{BOLD}{CYAN}╔══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║{RESET}  {BOLD}{YELLOW}Decimal Value :{RESET} {GREEN}{decimal_val:<40.4f}{RESET} {BOLD}{CYAN}║{RESET}")
    print(f"{BOLD}{CYAN}║{RESET}  {BOLD}{YELLOW}Fraction Value:{RESET} {GREEN}{fraction_val:<40}{RESET} {BOLD}{CYAN}║{RESET}")
    print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════════════════╝{RESET}\n")
    
    print(f"{MAGENTA}⏳ Returning to Main Menu in 3 seconds...{RESET}")
    time.sleep(3) 

# --- TRIGONOMETRY FUNCTIONS ---
def sine():
    sinetheta = pependicular / hypotenus
    sinetheta2 = f"{pependicular}/{hypotenus}"
    format_output("SINE", sinetheta, sinetheta2)

def cos():
    costheta = base / hypotenus
    costheta2 = f"{base}/{hypotenus}"
    format_output("COS", costheta, costheta2)

def tan():
    tantheta = pependicular / base
    tantheta2 = f"{pependicular}/{base}"
    format_output("TAN", tantheta, tantheta2)    

def cosec():
    cosectheta = hypotenus / pependicular
    cosectheta2 = f"{hypotenus}/{pependicular}"
    format_output("COSEC", cosectheta, cosectheta2)

def sec():
    sectheta = hypotenus / base
    sectheta2 = f"{hypotenus}/{base}"
    format_output("SEC", sectheta, sectheta2)

def cot():
    cottheta = base / pependicular
    cottheta2 = f"{base}/{pependicular}"
    format_output("COT", cottheta, cottheta2)    


# --- MAIN MENU LOOP ---
while True:
    clear_screen()
    print_header("MAIN MENU")
    print(f"{BOLD}{YELLOW}Which ratio do you want to find?{RESET}")
    print(f"  {CYAN}[1]{RESET} {GREEN}Sine{RESET}")
    print(f"  {CYAN}[2]{RESET} {GREEN}Cos{RESET}")
    print(f"  {CYAN}[3]{RESET} {GREEN}Tan{RESET}")
    print(f"  {CYAN}[4]{RESET} {GREEN}Cosec{RESET}")
    print(f"  {CYAN}[5]{RESET} {GREEN}Sec{RESET}")
    print(f"  {CYAN}[6]{RESET} {GREEN}Cot{RESET}")
    print(f"  {CYAN}[0]{RESET} {RED}Exit Calculator{RESET}")
    print(f"{MAGENTA}" + "-" * 30 + f"{RESET}")
    
    try:
        ratio_finder = int(input(f"{BOLD}{YELLOW}Enter your choice (0-6): {RESET}"))
        
        if ratio_finder == 1: sine()
        elif ratio_finder == 2: cos()
        elif ratio_finder == 3: tan()
        elif ratio_finder == 4: cosec()
        elif ratio_finder == 5: sec()
        elif ratio_finder == 6: cot()
        elif ratio_finder == 0:
            clear_screen()
            print(f"\n{BOLD}{GREEN}👋 Thank you for using T-Calculator! Goodbye.{RESET}\n")
            break 
        else:
            print(f"\n{BOLD}{RED}[!] Invalid choice. Please try again.{RESET}\n")
            time.sleep(1)
            continue
            
    except ValueError:
        print(f"\n{BOLD}{RED}[!] ERROR: Please enter a valid number!{RESET}\n")
        time.sleep(1)
