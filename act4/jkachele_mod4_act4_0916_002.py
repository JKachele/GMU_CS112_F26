#=======================================================================
# Title: The Space Cargo Validator 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Summary: To automatically screen incoming cargo spaceships, evaluate
#          manifests, and enforce strict customs regulations.
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Rules:
# 1) Data Types: int, float, string, and bool
# 2) Operators: Arithmetic, relational, and logical operators only.
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Computations:
# 1) Branch to Decide 
# 2) Use Boolean expressions
# 3) Use single condition and compund conditions
# 4) Use ifs and nested ifs
#=======================================================================



#++++++++++++++++++Monolithic Program W/Branching++++++++++++++++++++++


# =====================================================================
# STEP 1: CHARGE HEAVY PAYLOAD
# =====================================================================
container_weight = 542.5

# Step 1 Code:
is_heavy = container_weight > 500
print("Is heavy cargo:", is_heavy)


# =====================================================================
# STEP 2: DOCKING SAFELY
# =====================================================================
crew_name = "Alex"
is_registered = True
radiation_level = 12.4

# Step 2 Code:
allow_docking = is_registered and radiation_level <= 15
print("Clearance granted:", allow_docking)


# =====================================================================
# STEP 3: TRIGGER ALARM 
# =====================================================================
oxygen_percent = 18.2
alarm_system = "OFF"

# Step 3 Code:
if oxygen_percent < 19.5:
    alarm_system = "ALARM TRIPPED"

print("System Status:", alarm_system)


# =====================================================================
# STEP 4: PAY BOARDING TAX
# =====================================================================
home_planet = "Mars"
tax_owed = 0

# Step 4 Code:
if home_planet == "Earth":
    tax_owed = 50
else:
    tax_owed = 20

print("Total entry tax: $" + str(tax_owed))

# =====================================================================
# STEP 5: PRIORATIZE SHIPS
# =====================================================================
fuel_left = 25.4
has_medical_supplies = True
assigned_lane = "Unassigned"

# Step 5 Code:
if fuel_left < 10:
    assigned_lane = "Alpha"
elif has_medical_supplies:
    assigned_lane = "Beta"
else:
    assigned_lane = "Gamma"

print("Proceed to landing lane:", assigned_lane)

# =====================================================================
# STEP 6: BYPASS QUEUE
# =====================================================================
has_vip_badge = True
docking_credits = 0
bypass_status = "PENDING"

# Step 6 Code:
if has_vip_badge:
    if docking_credits > 0:
        bypass_status = "APPROVED"
    else:
        bypass_status = "DENIED"
else:
    bypass_status = "DENIED"

print("Queue Bypass Status:", bypass_status)

#++++++++++++++++++++++ Modularity W/ ++Branching++++++++++++++++++++++
# =====================================================================
# STEP 7: Modularize TO CREATE FUNCTIONS
# =====================================================================

#write your code here 
def prioratize_ships(fuel_left, has_medical_supplies):
    assigned_lane = "Unassigned"
    if fuel_left < 10:
        assigned_lane = "Alpha"
    elif has_medical_supplies:
        assigned_lane = "Beta"
    else:
        assigned_lane = "Gamma"
    return assigned_lane


