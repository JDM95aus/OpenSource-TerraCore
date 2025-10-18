# Assembly Guide: Terracore Alpha Stationary Appliance

## Overview
This guide covers assembly of the wall-powered Terracore Alpha prototype. This is a stationary unit designed for laboratory and kitchen countertop use, focusing on core technology validation.

## Required Tools
- Phillips head screwdrivers (#1, #2)
- Hex key set (metric)
- Wire strippers and cutters
- Soldering iron and solder
- Multimeter
- 3D printer (for custom parts)
- Calipers for verification

## Assembly Steps

### Step 1: Chassis Preparation
1. Print all 3D components from `/cad/alpha_v1/`
2. Verify print dimensions match CAD specifications
3. Clean all printed parts with isopropyl alcohol
4. Install acrylic viewing window using silicone gasket
5. Mount aluminum thermal mass plate to chassis base

### Step 2: Thermal System Assembly
1. Install cartridge heaters into aluminum thermal mass
2. Route heater wires to power relay module
3. Mount DS18B20 temperature sensors at three points:
   - Center of thermal mass
   - Bio-chamber center
   - Bio-chamber edge
4. Apply ceramic insulation around heating assembly
5. Secure all wiring with cable ties

### Step 3: Deposition System Installation
1. Assemble 2-axis gantry frame
2. Install NEMA 17 stepper motors
3. Mount peristaltic pump to chassis side panel
4. Install food-grade tubing from reservoir to nozzle
5. Calibrate nozzle height to 5mm above substrate surface

### Step 4: Bio-Chamber Setup
1. Install ultrasonic mister in designated compartment
2. Mount 5V PC fans for air circulation
3. Place HEPA filter over air intake
4. Install LED grow light strip on chamber ceiling
5. Position removable substrate tray on thermal plate

### Step 5: Electronics Integration
1. Mount Arduino Mega to main control panel
2. Install motor drivers with adequate heat sinking
3. Connect all sensors to designated ports:
   - Temperature sensors: Digital pins 2-4
   - Humidity sensor: Digital pin 5
   - CO2 sensor: Serial port
4. Wire relay module for heater and mister control
5. Connect 12V power supply to distribution board

### Step 6: Power and Safety
1. Install 5A fuse on main power input
2. Verify all grounds are connected to common point
3. Secure all wiring away from moving parts
4. Test emergency stop circuit
5. Apply silicone sealant to all external wire passages

### Step 7: Software Installation
1. Upload firmware from `/firmware/terracore_alpha/`
2. Calibrate temperature PID values
3. Test deposition system with water
4. Verify sensor readings in serial monitor
5. Run system diagnostic routine

## Calibration Procedures

### Thermal Calibration
1. Heat system to 25°C and stabilize for 1 hour
2. Verify all three temperature sensors read within 0.2°C
3. Adjust PID values in firmware if oscillation occurs
4. Test recovery from door opening event

### Deposition Calibration
1. Prime system with nutrient solution
2. Program deposition pattern for 10ml total volume
3. Measure actual deposited volume
4. Adjust pump steps per ml in firmware
5. Verify pattern accuracy on test substrate

## Safety Verification Checklist
- [ ] All high-voltage connections insulated
- [ ] Emergency stop functional
- [ ] No water exposure to electronics
- [ ] Thermal fuses installed and tested
- [ ] Ground continuity verified
- [ ] Moving parts guarded
- [ ] Bio-seal integrity confirmed

## First Power-On Sequence
1. Connect 12V power supply
2. Monitor serial output for errors
3. Verify all sensors initializing
4. Test heater activation
5. Check deposition system homing
6. Validate mister operation
7. Confirm LED lighting function

## Troubleshooting
Common issues and solutions documented in `troubleshooting.md`

## Next Steps
After successful assembly, proceed to biological integration and growth trials as outlined in `bio-protocols.md`
