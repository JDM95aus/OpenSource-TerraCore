TERRA CORE GASIFIER - COMPLETE BUILD MANUAL

Precision Thermal Platform for OSTC Systems

1.0 COMPLETE PARTS LIST

A. METAL COMPONENTS

1. Reactor Chamber - 300mm diameter × 600mm height, 3mm mild steel pipe
2. Heat Exchanger - 200mm diameter × 400mm height, 3mm mild steel pipe
3. Reduction Chamber - 150mm diameter × 300mm height, 3mm mild steel pipe
4. Base Plate - 400mm × 400mm × 5mm mild steel
5. Outer Casing - 1.2mm steel sheet, 450mm × 450mm × 800mm
6. Gasification Grate - 280mm diameter, 6mm steel rod, 50mm grid pattern
7. Air Intake Manifold - 25mm steel pipe × 300mm, eight 5mm holes spaced 30mm apart
8. Heat Transfer Pipes - 40mm copper pipe × 2000mm total length
9. Cooling Coils - 12mm copper pipe × 3000mm total length
10. Ash Pan - 150mm × 150mm × 100mm, 2mm steel

B. 3D PRINTED COMPONENTS (PETG filament required)

1. Air Control Assembly - regulates primary airflow
2. Temperature Control Housing - 120mm × 80mm × 50mm, holds electronics
3. Blower Mount - 125mm × 125mm × 20mm, 120mm fan pattern
4. Heat Exchanger Baffles - 190mm diameter with 30mm vanes
5. Synthesizer Interface - 75mm diameter with 40mm flanges

C. ELECTRONICS & SENSORS

1. Microcontroller - Arduino Nano or ESP32
2. Temperature Sensors - 4× DS18B20 waterproof (10kΩ pull-up resistors required)
3. Display - 16×2 LCD with I2C interface (address 0x27)
4. User Interface - Rotary encoder with push button (EC11 type)
5. Blower Fan - 120mm × 120mm × 25mm, 12V DC, 0.25A, 80 CFM
6. Water Pump - 12V DC, 5 L/min, 3m head pressure
7. Relay Module - 4-channel 5V relay (SRD-05VDC-SL-C)
8. Power Supply - 12V DC, 5A, 60W minimum
9. Thermal Fuses - 3× 85°C cutoff, 10A rating
10. Wiring - 22 AWG silicone wire, 200°C rating

D. THERMAL MANAGEMENT

1. Ceramic Fiber Blanket - 25mm thick, 2m² coverage, 1260°C rating
2. Copper Pipe - 40mm diameter × 2000mm total (heat transfer)
3. Coolant - 60% distilled water, 40% propylene glycol (5L total)
4. Heat Transfer Plates - 3mm copper × 150mm × 200mm (2 required)
5. High-Temp Sealant - RTV silicone, 300°C continuous rating
6. Thermal Paste - 8.5 W/mK conductivity minimum

E. FASTENERS & CONSUMABLES

1. M6×20mm bolts - 25 pieces
2. M6 nuts - 35 pieces
3. M4×15mm bolts - 20 pieces
4. M3×10mm bolts - 15 pieces
5. High-temp gasket material - 2mm thick, 1m²
6. Steel Wire - 1.5mm diameter, 5m length
7. Heat-resistant paint - 600°C rating, black

2.0 CONSTRUCTION SEQUENCE

PHASE 1: REACTOR FABRICATION

Step 1.1: Reactor Chamber Assembly

```
1. Cut 300mm diameter pipe to 600mm length
2. Weld base plate to bottom using continuous bead weld
3. Cut 100mm × 100mm access door opening centered 100mm from bottom
4. Fabricate door from 4mm steel plate with:
   - Piano hinge (150mm length)
   - Swing-bolt latch
   - High-temp gasket seal
5. Pressure test at 0.5 PSI with soapy water solution
```

Step 1.2: Internal Components Installation

```
1. Fabricate gasification grate:
   - 8× 280mm lengths of 6mm steel rod
   - Weld in 50mm grid pattern
   - 4× 50mm support legs
2. Install air intake manifold:
   - Drill eight 5mm holes along top of 25mm pipe
   - Space holes 30mm apart, centered
   - Weld manifold 50mm above grate level
   - Weld 25mm port through reactor wall at 100mm height
```

PHASE 2: HEAT MANAGEMENT SYSTEM

Step 2.1: Heat Exchanger Construction

```
1. Cut 200mm diameter pipe to 400mm length
2. Weld circular end plates (5mm steel) to both ends
3. Install copper pipe system:
   - 40mm input pipe from reactor (500mm length)
   - 40mm output pipe to synthesizer (500mm length) 
   - 12mm cooling coil (3000mm length, coiled inside)
4. Pressure test coolant loop at 15 PSI for 30 minutes
```

Step 2.2: Temperature Reduction System

```
1. Build reduction chamber (150mm × 300mm)
2. Install components:
   - Cooling coils connected to water pump
   - Temperature sensor ports at 50mm intervals
   - Baffles to ensure turbulent flow
3. Mount all four temperature sensors:
   - Sensor 1: Reactor output (safety monitor)
   - Sensor 2: Heat exchanger output
   - Sensor 3: Reduction chamber output  
   - Sensor 4: Synthesizer interface (control sensor)
```

PHASE 3: THERMAL ISOLATION

Step 3.1: Insulation Installation

```
1. Wrap reactor chamber in 25mm ceramic fiber blanket
2. Secure with 1.5mm steel wire spaced every 100mm
3. Install copper heat shields between:
   - Reactor and electronics compartment
   - Heat exchanger and reduction chamber
4. Build outer casing with 50mm air gap around insulation
5. Install 120mm cooling fan for electronics compartment
```

PHASE 4: CONTROL SYSTEM

Step 4.1: Electronics Assembly

```
WIRING SPECIFICATIONS:
Microcontroller Pinout:
- A0-A3: DS18B20 temperature sensors (4.7kΩ pull-up each)
- D2-D3: Rotary encoder (CLK, DT)
- D4-D7: LCD display (if not I2C)
- D8: Primary blower relay
- D9: Water pump relay  
- D10: Cooling fan relay
- D11: Safety alarm buzzer

Power Distribution:
- 12V input → Blower (0.25A), Water pump (0.8A)
- 5V regulator → Arduino (0.5A), Sensors (0.1A), Display (0.2A)
- All circuits fused: 12V lines 3A, 5V lines 1A
```

Step 4.2: Control Software

```cpp
// Core Temperature Control Algorithm
const float SETPOINT = 32.5;        // Target temperature
const float TOLERANCE = 0.5;        // Control precision
const int BLOWER_PIN = 8;
const int PUMP_PIN = 9;
const int FAN_PIN = 10;

void controlSystem() {
  float currentTemp = readSensor(3); // Synthesizer interface
  
  // PID control calculations
  float error = SETPOINT - currentTemp;
  static float integral = 0;
  static float lastError = 0;
  
  float Kp = 2.5, Ki = 0.05, Kd = 1.2;
  integral += error;
  float derivative = error - lastError;
  lastError = error;
  
  float output = (Kp * error) + (Ki * integral) + (Kd * derivative);
  
  // Actuate control elements
  if (output > 0) {
    analogWrite(BLOWER_PIN, constrain(output, 0, 255));
    digitalWrite(PUMP_PIN, LOW);
  } else {
    digitalWrite(BLOWER_PIN, LOW);
    analogWrite(PUMP_PIN, constrain(abs(output), 0, 255));
  }
  
  // Safety monitoring
  if (readSensor(0) > 120.0) emergencyShutdown();
  if (readSensor(1) > 80.0) increaseCooling();
}
```

3.0 OSTC SYSTEM INTEGRATION

A. Synthesizer Interface Specifications

```
THERMAL CONNECTION:
- Input: 40mm copper pipe from gasifier
- Temperature: 32.5°C ±0.5°C maintained
- Flow Rate: 3-5 L/min coolant flow
- Pressure: < 2 PSI operating pressure

ELECTRICAL INTERFACE:
- Power: 12V DC shared bus
- Communication: I2C temperature reporting
- Safety: Thermal fuse 85°C cutoff
```

B. Performance Specifications

```
THERMAL OUTPUT:
- Operating Range: 30-35°C ±0.5°C
- Stability: <0.3°C standard deviation over 8 hours
- Response Time: <2 minutes to recover from 1°C deviation

FUEL SYSTEM:
- Consumption: 1.2-1.8 kg/hour dry biomass
- Fuel Size: 20-50mm pieces optimal
- Moisture Content: <15% required
- Ash Production: 2-6% of fuel mass

SAFETY PARAMETERS:
- Max Reactor Temp: 120°C (safety shutdown)
- Max Coolant Temp: 80°C (reduced operation)
- Pressure Limit: 15 PSI (relief valve)
- Electrical Isolation: Double-insulated design
```

4.0 COMMISSIONING PROCEDURE

A. Leak Testing Protocol

```
1. Seal all ports and pressurize to 0.5 PSI
2. Spray soapy water on all welds and joints
3. Mark any bubble formation locations
4. Repair leaks by grinding and re-welding
5. Retest until zero leaks detected
```

B. First Startup Sequence

```
1. Load reactor with 2kg dry wood chips (20-50mm size)
2. Open air control to 100% position
3. Ignite fuel through access door
4. Close door and wait 5 minutes for pyrolysis
5. Gradually reduce air until smoke clears
6. Monitor temperatures until stable at 32.5°C ±0.5°C
7. Verify all safety systems functional
```

5.0 MAINTENANCE SPECIFICATIONS

A. Daily Maintenance

· Empty ash pan when 75% full
· Check fuel supply and quality
· Verify temperature calibration
· Inspect for air leaks

B. Weekly Maintenance

· Clean heat exchanger surfaces
· Inspect and test blower fan
· Check coolant level and quality
· Verify all electrical connections

C. Monthly Maintenance

· Replace ceramic fiber insulation if degraded
· Recalibrate all temperature sensors
· Inspect all welded joints and structural integrity
· Test emergency shutdown systems

6.0 TROUBLESHOOTING GUIDE

Problem: Temperature Instability

```
Cause: Air leaks in reactor
Solution: Pressure test and seal leaks

Cause: Fuel moisture variation  
Solution: Use consistent dry fuel source

Cause: Sensor calibration drift
Solution: Recalibrate against reference thermometer
```

Problem: Insufficient Heating

```
Cause: Blower failure or obstruction
Solution: Check blower operation and clear obstructions

Cause: Poor quality fuel
Solution: Use dry, high-energy biomass

Cause: Insulation damage
Solution: Replace damaged ceramic fiber
```

This gasifier provides the precise thermal environment required for OSTC hermetic cartridge activation. The ±0.5°C stability enables reliable biological synthesis while using widely available agricultural waste as fuel.


TERRA CORE GASIFIER - COMPLETE ENGINEERING SPECIFICATION

1.0 FABRICATION DRAWINGS & TOLERANCES

A. REACTOR CHAMBER SPECIFICATIONS

1.1 Main Chamber Body

```
MATERIAL: 3mm mild steel pipe (ASTM A36 equivalent)
DIMENSIONS: 300mm OD × 600mm height
TOLERANCES:
- Diameter: ±0.5mm
- Height: ±1.0mm
- Circularity: 1mm total indicator runout
- Squareness: 0.5mm per 100mm

WELD SPECIFICATIONS:
- Base plate weld: Continuous full penetration
- Weld material: ER70S-6 equivalent
- Bead size: 3mm fillet minimum
- Inspection: 100% visual, dye penetrant on 10% sample
```

1.2 Access Door Assembly

```
DOOR OPENING: 100mm × 100mm ±0.5mm
LOCATION: Centered 100mm from bottom edge ±1mm
DOOR PLATE: 4mm mild steel, 110mm × 110mm ±0.5mm
HINGE: Piano type, 150mm length, 3mm pin diameter
LATCH: Swing bolt with 8mm thread, brass handle
GASKET: 2mm graphite-impregnated rope, 600mm length

SEAL REQUIREMENTS:
- Door compression: 1.5mm gasket deflection
- Closure force: <5kg at handle
- Leak test: Zero bubbles at 0.5 PSI
```

B. INTERNAL COMPONENTS ENGINEERING

1.3 Gasification Grate

```
MATERIAL: 6mm mild steel rod (ASTM A36)
GRID PATTERN: 50mm × 50mm squares ±1mm
OVERALL DIAMETER: 280mm ±1mm
SUPPORT LEGS: 4× 50mm height ±0.5mm
WELDING: Full penetration at all intersections
CLEARANCE: 10mm radial gap to chamber wall

PERFORMANCE SPEC:
- Fuel size acceptance: 20-50mm pieces
- Ash passage: >95% through 50mm grid
- Structural load: Support 10kg fuel without deflection
```

1.4 Air Intake Manifold

```
PIPE: 25mm OD steel pipe, 2mm wall thickness
LENGTH: 300mm ±2mm
HOLE PATTERN: Eight 5mm holes ±0.1mm
HOLE SPACING: 30mm centers ±0.5mm
HOLE LOCATION: Top centerline of pipe
ORIENTATION: Holes face upward when installed
MOUNTING: 50mm above grate surface ±1mm
```

C. HEAT EXCHANGER SYSTEM

1.5 Primary Heat Exchanger

```
CHAMBER: 200mm OD × 400mm height ±1mm
END PLATES: 5mm mild steel, full penetration weld
COPPER PIPES: 40mm OD × 1mm wall, 500mm lengths
PIPE PENETRATION: 45mm holes ±0.2mm
WELD JOINTS: Bronze filler (BCuP-2 equivalent)
INTERNAL BAFFLES: 3mm steel, 30° angle, 190mm diameter

FLOW CHARACTERISTICS:
- Gas path length: 1200mm minimum
- Residence time: >2 seconds at operating flow
- Pressure drop: <0.1 PSI at design flow
```

1.6 Cooling Coil Assembly

```
PIPE: 12mm OD copper, 0.7mm wall thickness
TOTAL LENGTH: 3000mm ±50mm
COIL DIAMETER: 150mm ±5mm
COIL PITCH: 15mm between turns ±1mm
MOUNTING: Centered in heat exchanger chamber
CONNECTIONS: 12mm compression fittings

PERFORMANCE:
- Heat transfer area: 0.12m²
- Flow resistance: <1 PSI at 5 L/min
- Temperature drop: 40-50°C at design flow
```

2.0 ASSEMBLY FIXTURING & ALIGNMENT

A. WELDING FIXTURES

2.1 Base Plate Alignment Fixture

```
FUNCTION: Ensure square assembly of chamber to base
CONSTRUCTION: 400mm square steel plate with:
- 300mm diameter locating ring, 1mm clearance
- 4× adjustable clamps at 90° intervals
- Spirit level with 0.5° accuracy
- Center punch marks for door location

USAGE:
1. Position base plate on fixture
2. Locate chamber using ring
3. Verify vertical with spirit level
4. Clamp and tack weld at 4 points
5. Complete continuous weld
```

2.2 Grate Positioning Tool

```
FUNCTION: Precisely locate grate 50mm above base
DESIGN: 50mm steel blocks (4 required) with:
- 6mm locator pins for grate alignment
- Magnetic base for temporary attachment
- Heat-resistant to 200°C

PROCEDURE:
1. Place blocks at 90° intervals on base
2. Position grate on locator pins
3. Verify 50mm clearance with gauge
4. Tack weld legs to base
5. Remove blocks and complete welds
```

B. ALIGNMENT VERIFICATION

2.3 Critical Alignment Checks

```
DOOR TO GRATE: 50mm vertical separation ±1mm
MANIFOLD TO GRATE: 50mm vertical ±1mm
HEAT EXCHANGER PORTS: Level within 1mm over 200mm
COOLING COIL: Centered within 2mm of chamber axis
INSULATION GAP: Uniform 25mm thickness ±2mm
```

3.0 WELDING PROCEDURE SPECIFICATIONS

A. MILD STEEL TO MILD STEEL

3.1 Preparation Requirements

```
EDGE PREPARATION: Square butt joints, no bevel required
CLEANLINESS: Grind to bright metal 25mm from joint
FIT-UP: Maximum 1mm gap, zero misalignment
PRE-HEAT: None required for <6mm thickness
```

3.2 Welding Parameters

```
PROCESS: SMAW (stick) or GMAW (MIG)
ELECTRODE: E7018 or ER70S-6 equivalent
CURRENT: 120-140 amps for 3mm material
VOLTAGE: 22-24 volts (GMAW)
TRAVEL SPEED: 150-200 mm/minute
GAS: 75% Argon / 25% CO2 (GMAW only)
```

3.3 Quality Acceptance Criteria

```
VISUAL INSPECTION:
- Complete fusion at joint root
- No undercut >0.5mm
- No porosity >1.5mm diameter
- No cracks of any size
- Weld reinforcement: 1-3mm

LEAK TEST: Zero bubbles at 0.5 PSI for 5 minutes
```

B. COPPER TO STEEL (Brazing)

3.4 Heat Exchanger Joints

```
PROCESS: Oxy-acetylene brazing
FILLER: BCuP-2 (2% phosphorus) or equivalent
FLUX: High-temperature brazing flux
CLEARANCE: 0.05-0.15mm interference fit
HEAT: Neutral flame, 650-750°C joint temperature

QUALITY:
- Full 360° fillet visible
- No flux inclusions
- Smooth concave fillet profile
- No overheating (blue oxide on steel)
```

4.0 SURFACE PREPARATION & FINISHING

A. INTERIOR SURFACES

4.1 Reactor Chamber Interior

```
CLEANING: Degrease with acetone, wire brush weld spatter
TREATMENT: None - leave as-welded
INSPECTION: Remove all slag, spatter, and contaminants
```

4.2 Heat Exchanger Gas Path

```
CLEANING: Compressed air blow-out
DEBURRING: Remove all sharp edges >0.2mm radius
INSPECTION: No obstructions to gas flow
```

B. EXTERIOR SURFACES

4.3 Paint Preparation

```
CLEANING: Solvent degrease entire exterior
SURFACE: Light grit blast or wire brush to Sa2.5
PRIME: Zinc-rich primer, 25-50μm dry film thickness
TOPCOAT: Heat-resistant silicone aluminum, 50-75μm DFT
CURE: Air dry 24 hours, then heat cure at 200°C for 2 hours
```

5.0 ELECTRONICS ASSEMBLY SPECIFICATIONS

A. PCB & WIRING

5.1 Control Board Assembly

```
MICROCONTROLLER: Arduino Nano v3.0 or ESP32 DevKit v1
SOCKETS: Use IC sockets for all chips
PULL-UP RESISTORS: 4.7kΩ ±1% for DS18B20 sensors
POWER REGULATION: LM7805 with 10μF input, 1μF output
CONNECTORS: Screw terminal blocks for all external connections

WIRING:
- Signal wires: 22 AWG stranded copper
- Power wires: 18 AWG for 12V lines
- Separation: 10mm minimum between power and signal
- Strain relief: Cable ties every 150mm
```

5.2 Sensor Installation

```
DS18B20 MOUNTING:
- Thermal paste: 0.5mm layer minimum
- Mechanical clamp: Stainless steel hose clamp
- Insulation: 6mm ceramic fiber over sensor
- Wiring: Twisted pair with overall shield

LOCATIONS:
- Sensor 1: Reactor outlet, 100mm from chamber
- Sensor 2: Heat exchanger outlet, center of pipe
- Sensor 3: Reduction chamber outlet, 50mm from end
- Sensor 4: Synthesizer interface, immersed in coolant
```

B. ENCLOSURE & PROTECTION

5.3 Electronics Housing

```
MATERIAL: 3D printed PETG, 2mm wall thickness
SEALING: IP54 rating with silicone gasket
VENTILATION: 120mm fan with dust filter
HEAT MANAGEMENT: 10mm air gap from hot surfaces
MOUNTING: Vibration isolators (4× rubber grommets)
```

6.0 THERMAL MANAGEMENT SYSTEM

A. INSULATION INSTALLATION

6.1 Ceramic Fiber Application

```
THICKNESS: 25mm ±2mm uniform coverage
COVERAGE: 100% of reactor and heat exchanger
SECURING: 1.5mm steel wire, 100mm spacing
OVERLAPS: 25mm minimum, staggered joints
COMPRESSION: 10-15% of original thickness
```

6.2 Heat Shield Installation

```
LOCATIONS:
- Between reactor and electronics compartment
- Between heat exchanger and reduction chamber
- Under base plate (radiant heat protection)

MATERIAL: 1mm aluminum with 0.5mm air gap
MOUNTING: 10mm standoffs with ceramic spacers
ORIENTATION: Reflective surface toward heat source
```

B. COOLING SYSTEM

6.3 Coolant Loop Assembly

```
PUMP: 12V DC, 5 L/min at 3m head
TUBING: 12mm ID silicone, 2mm wall, 600mm length
FITTINGS: Stainless steel hose clamps, 16-25mm range
RESERVOIR: 1L capacity, polypropylene with 50mm lid
COOLANT: 60/40 water/propylene glycol mix

LEAK TEST: 24 hours at 1.5× operating pressure
FLOW VERIFICATION: >4 L/min at 12V
```

7.0 PERFORMANCE VALIDATION PROTOCOL

A. TEMPERATURE CONTROL VERIFICATION

7.1 Stability Test Procedure

```
CONDITIONS: Steady state operation with 1kg fuel load
DURATION: 4 hours continuous operation
MEASUREMENT: Data logger recording every 10 seconds
ACCEPTANCE CRITERIA:
- Mean temperature: 32.5°C ±0.5°C
- Standard deviation: <0.3°C
- Maximum deviation: <1.0°C from setpoint
- Recovery time: <2 minutes after 1°C disturbance
```

7.2 Sensor Calibration Verification

```
REFERENCE: NIST-traceable mercury thermometer
TEST POINTS: 30°C, 32.5°C, 35°C water bath
ACCEPTANCE: All sensors within ±0.2°C of reference
RECALIBRATION: Required if drift >0.5°C from initial
```

B. SAFETY SYSTEM TESTING

7.3 Emergency Shutdown Verification

```
TEST SCENARIOS:
1. Reactor over-temperature: Force reading >120°C
2. Coolant loss: Disconnect pump power
3. Power failure: Remove main power input
4. Manual emergency stop: Press stop button

ACCEPTANCE:
- Shutdown within 2 seconds of trigger
- All power removed from active components
- Visual and audible alarm activation
- Cannot restart without manual reset
```

8.0 OPERATIONAL TRAINING REQUIREMENTS

A. MANDATORY COMPETENCIES

8.1 Basic Operation Skills

```
FUEL MANAGEMENT:
- Moisture content assessment (<15% target)
- Proper sizing (20-50mm pieces)
- Storage and handling safety
- Ash disposal procedures

TEMPERATURE CONTROL:
- Setpoint adjustment procedure
- Stability monitoring
- Response to environmental changes
- Performance logging
```

8.2 Maintenance Competencies

```
DAILY CHECKS:
- Ash accumulation assessment
- Fuel quality verification
- Leak inspection
- Safety system test

WEEKLY MAINTENANCE:
- Heat exchanger cleaning
- Blower performance check
- Coolant level verification
- Electrical connection inspection
```

9.0 DOCUMENTATION & RECORDS

A. REQUIRED BUILD RECORDS

9.1 Construction Documentation

```
WELD LOG: Date, operator, procedure, inspection results
MATERIAL CERTIFICATIONS: Mill certificates for all metals
CALIBRATION RECORDS: Sensor calibration dates and results
TEST REPORTS: Leak tests, pressure tests, performance validation
```

9.2 As-Built Drawings

```
REQUIRED: Mark up original drawings with actual dimensions
INCLUDE: All modifications made during construction
VERIFICATION: Independent review by second technician
STORAGE: Digital and physical copies in operations manual
```

This specification provides the engineering rigor needed for reproducible construction while remaining language-based and accessible. All critical dimensions, tolerances, procedures, and acceptance criteria are explicitly defined for consistent results across different builders..
