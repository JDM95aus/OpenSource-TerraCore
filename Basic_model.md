
SCHEMATIC PACKAGE: MYCOFORGE BASIC-LEVEL SYNTHESIS SYSTEM

System Principle: A 3D-Printed, Modular Food Synthesis Cell. Uses local biomass (mushrooms) & open-source nutrient/flavor cartridges to synthesize basic, nutritious food shapes.

1. MECHANICAL SCHEMATIC: The "Core" Frame & Motion

Frame:

· Material: 2020 Aluminum Extrusion (or square-section wood).
· Design: Cubic frame, 60cm x 60cm x 60cm.
· Key Features:
  · Modular Panels: Sides can be acrylic, wood, or food-safe plastic.
  · Tool-Free Fasteners: Use of snap-in brackets or hand-tightened bolts.

Motion System (Gantry):

· Type: CoreXY configuration.
· Why CoreXY? Keeps motors fixed to the frame, reducing moving mass. Faster, more precise.
· Belts: GT2 Timing Belts.
· Motors: 4x NEMA 17 Stepper Motors.

Schematic Detail:

```
[FRONT VIEW]
    [MOTOR A] ======[IDLER]=====
                    |          |
                    |          |
    [MOTOR B] ======[IDLER]=====
                    |          |
                    | (TOOL HEAD)
```

The belts are crossed in an X-Y pattern, allowing two motors to control X and Y movement collaboratively.

2. EXTRUSION SYSTEM SCHEMATIC: The "Multi-Material" Print Head

This is the heart of the synthesizer.

Design: A modular "Cold Extrusion" system.

Components per Extruder:

1. Syringe Reservoir: 50ml-100ml medical syringe (food-grade).
2. Plunger Driver: A threaded rod (lead screw) driven by a small NEMA 14 stepper motor.
3. Nozzle: Standard 3D printer nozzle (0.8mm - 1.2mm) for pastes.
4. Quick-Connect Coupling: Allows for fast syringe swapping.

Schematic Detail:

```
[EXTRUDER ASSEMBLY]
    [NEMA 14 Motor]
          |
    [Lead Screw]
          |
    [Plunger Plate] -> [Pushes Syringe Plunger]
                            |
                    [Syringe Body (Holds Paste)]
                            |
                    [Nozzle Tip (0.8mm)]
```

Multi-Head Setup: The gantry holds 3-4 of these extruders in parallel:

· Extruder 1: Base Mushroom Paste.
· Extruder 2: Nutrient/Fortification Paste.
· Extruder 3: Flavor/Color Paste.
· Extruder 4: Binding/Structure Paste (e.g., starch gel).

3. ELECTRONICS & CONTROL SCHEMATIC

Central Brain:

· Main Controller: Raspberry Pi 4 (or Pi 3B+).
· Real-Time Motor Driver: Arduino Mega 2560 + RAMPS 1.4 Shield.
  This is a standard, robust, and well-documented 3D printer control setup.

Wiring Schematic:

```
[POWER SUPPLY - 12V/20A]
        |
    [RAMPS 1.4 Shield]
        |
    [Arduino Mega] <-USB-> [Raspberry Pi]
        |
        |---- [X & Y Stepper Motor Drivers (A4988)]
        |---- [Z Stepper Motor Driver] *For future lift mechanism
        |---- [Extruder Stepper Drivers (E0, E1, E2, E3)]
        |---- [Heated Bed Output] *For cooking plate
        |---- [Thermistor Inputs] *For temp monitoring
        |---- [12V Fan Outputs] *For cooling electronics
```

Sensors:

· DHT22: Chamber ambient temperature/humidity.
· DS18B20: Bed temperature (for cooking surface).
· Limit Switches: X, Y, Z axis homing.

4. BIOLOGICAL & CHEMICAL SCHEMATICS

This is the "secret sauce" – the open-source formulations.

A. "Base Ink" - Mushroom Paste Formulation

· Ingredient: 100g Harvested Oyster Mushrooms (steamed & blended).
· Binder: 5g Food-Grade Sodium Alginate.
· Water: 50ml (for consistency).
· Process: Blend into a smooth, toothpaste-like consistency.

B. "Flavor/Nutrient Cartridge" Formulations
These are dry powder mixes to be combined with the base ink or water.

1. "Savory Chicken-Style" Sachet:
   · Nutritional Yeast (10g)
   · Soy Protein Isolate (5g)
   · Garlic Powder (2g)
   · Onion Powder (1g)
   · Turmeric (0.5g, for color)
   · Salt (1g)
2. "Iron-Fortified" Sachet:
   · Spinach Powder (10g)
   · Lentil Flour (5g)
   · Citrus Powder (1g, for Vitamin C to aid iron absorption)

Users mix a sachet with 50ml of base ink before loading into a syringe.

5. ASSEMBLY INSTRUCTIONS (Summary)

1. Print Parts: Use the "Seed" 3D printer to create all custom components (motor mounts, syringe holders, fan shrouds).
2. Build Frame: Assemble the aluminum extrusion cube.
3. Install Gantry: Mount the CoreXY belt system and motors.
4. Wire Electronics: Follow the wiring diagram to connect Pi, Arduino, RAMPS, motors, and sensors.
5. Mount Extruders: Snap the syringe-based extruders onto the gantry plate.
6. Load Firmware: Flash the custom Mycoforge Marlin firmware to the Arduino.
7. Calibrate: Run standard 3D printer calibration routines (bed leveling, extrusion steps/mm).

