```markdown
# Assembly Guide: TerraCrab Mk.II Mobile Platform

## Overview
Step-by-step assembly of the mobile TerraCrab prototype. This guide covers integration of mobility systems with the core Terracore technology for field operation.

## Required Tools
- Phillips head screwdrivers (#1, #2)
- Hex key set (metric 1.5mm to 6mm)
- Wire strippers and cutters
- Soldering iron and solder
- Multimeter
- Cable tie tension tool

## Assembly Steps

### Step 1: Chassis and Leg Assembly
1. Assemble main body sections using M4 bolts and lock nuts
2. Install leg servos into hip joints with vibration dampeners
3. Connect thigh segments to servo horns with steel pins
4. Attach lower leg segments with spring-loaded joints
5. Verify 30-degree leg splay for stability

### Step 2: Power System Installation
1. Mount solar panel to chassis upper surface
2. Install MPPT charge controller in waterproof compartment
3. Secure lithium battery pack with vibration isolation
4. Connect power distribution board with appropriate fusing
5. Route all power cables through cable management channels

### Step 3: Core Technology Integration
1. Install scaled Thermal Core in central chassis location
2. Mount deposition gantry above bio-core chamber
3. Connect peristaltic pump to nutrient reservoir
4. Install environmental sensors in bio-core

### Step 4: Mobility Control System
1. Mount ESP32 main controller on vibration-isolated plate
2. Install motor drivers for all leg actuators
3. Connect IMU for orientation and balance data
4. Wire GPS module for navigation capability
5. Install ultrasonic sensors for obstacle detection

### Step 5: Sealing and Weatherproofing
1. Apply silicone sealant to all chassis seams
2. Install waterproof cable glands for external wiring
3. Apply conformal coating to all PCBs
4. Test bio-core chamber for airtight seal

### Step 6: System Integration
1. Connect all subsystems to main power bus
2. Route communication cables away from power lines
3. Install cooling fans for electronics compartment
4. Mount status LED indicators for system monitoring

## Calibration Procedures

### Leg Servo Calibration
1. Power on system without load
2. Home all leg servos to zero position
3. Verify leg geometry matches design specifications
4. Test full range of motion for each joint

### Navigation System Calibration
1. Calibrate IMU on level surface
2. Test GPS acquisition time and accuracy
3. Verify ultrasonic sensor distance measurements
4. Test autonomous navigation in controlled environment

### Core System Calibration
1. Verify thermal regulation during movement
2. Test deposition accuracy while platform is mobile
3. Calibrate environmental sensor readings
4. Validate bio-core seal integrity under motion stress

## Safety Verification Checklist
- [ ] All high-voltage connections properly insulated
- [ ] Emergency stop system functional
- [ ] Battery isolation switch accessible
- [ ] No sharp edges on external surfaces
- [ ] Leg pinch points properly guarded
- [ ] Thermal overload protection active
- [ ] Waterproofing verified for all electronics

## First Power-On Sequence
1. Connect solar input with appropriate fusing
2. Verify battery voltage and charging status
3. Power up main controller and check for errors
4. Initialize leg servos one at a time
5. Test communication with all sensor systems
6. Verify thermal system activation
7. Check deposition system priming
8. Validate navigation sensor functionality

## Troubleshooting
Common issues and solutions documented in separate troubleshooting guide

## Next Steps
After successful assembly, proceed to field testing and biological integration protocols
```
