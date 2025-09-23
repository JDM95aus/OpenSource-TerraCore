"""
TerraCore Sensor Simulator
Originally contributed by moneyish69 via GitHub Issues

Simulates temperature/humidity sensors for development and testing.
Designed to be easily swapped with real hardware sensors later.
"""

import logging
from logging.handlers import RotatingFileHandler
import random
import time
from datetime import datetime

# Configuration
LOG_FILE = "sensor.log"
READ_INTERVAL_SEC = 5  # seconds between reads

# Acceptable ranges (adjust to match real-world needs)
TEMP_C_MIN = 15.0
TEMP_C_MAX = 30.0
HUM_MIN = 30.0
HUM_MAX = 70.0

# Simulated sensor ranges for generation
SIM_TEMP_MEAN = 24.0
SIM_TEMP_SPREAD = 4.0
SIM_HUM_MEAN = 50.0
SIM_HUM_SPREAD = 12.0

def setup_logger() -> logging.Logger:
    """Set up logging with file rotation and console output."""
    logger = logging.getLogger("sensor_logger")
    logger.setLevel(logging.INFO)

    # File handler with rotation (max ~1MB, keep 3 backups)
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=3)
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

logger = setup_logger()

def read_temperature_c() -> float:
    """Simulate temperature reading with normal distribution."""
    return round(random.normalvariate(SIM_TEMP_MEAN, SIM_TEMP_SPREAD), 2)

def read_humidity_pct() -> float:
    """Simulate humidity reading with normal distribution (clamped 0-100%)."""
    val = random.normalvariate(SIM_HUM_MEAN, SIM_HUM_SPREAD)
    return round(max(0.0, min(100.0, val)), 2)

def check_alerts(temp_c: float, hum: float) -> None:
    """Check readings against acceptable ranges and log alerts."""
    alerts = []
    if temp_c < TEMP_C_MIN:
        alerts.append(f"Temperature low: {temp_c} °C < {TEMP_C_MIN} °C")
    if temp_c > TEMP_C_MAX:
        alerts.append(f"Temperature high: {temp_c} °C > {TEMP_C_MAX} °C")
    if hum < HUM_MIN:
        alerts.append(f"Humidity low: {hum} % < {HUM_MIN} %")
    if hum > HUM_MAX:
        alerts.append(f"Humidity high: {hum} % > {HUM_MAX} %")

    for msg in alerts:
        logger.warning(f"ALERT - {msg}")

def main():
    """Main sensor reading loop."""
    logger.info("Sensor logger started (simulated sensors). Press Ctrl+C to stop.")
    logger.info(f"Ranges -> Temp: {TEMP_C_MIN}..{TEMP_C_MAX} °C | Humidity: {HUM_MIN}..{HUM_MAX} %")

    try:
        while True:
            ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            temp_c = read_temperature_c()
            hum = read_humidity_pct()

            # Structured message suitable for later parsing
            logger.info(f"reading ts={ts} temp_c={temp_c:.2f} humidity_pct={hum:.2f}")
            check_alerts(temp_c, hum)
            time.sleep(READ_INTERVAL_SEC)
            
    except KeyboardInterrupt:
        logger.info("Sensor logger stopped by user.")
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")

## 🤝 Contributor
- **moneyish69**
