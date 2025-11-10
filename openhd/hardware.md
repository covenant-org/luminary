# OpenHD Hardware Requirements

---

## 1) Core Components

### Air Unit (On Drone)
- Single Board Computer (SBC)
  - Raspberry Pi 4B
  - Raspberry Pi Compute Module 4 (CM4) + carrier board (recommended)
- Supported camera (CSI or USB)
- Supported WiFi adapter (USB)
- Power supply / BEC (regulated 5 V with good current handling)
- Micro-SD card (16–32 GB recommended)

### Ground Unit
- Laptop **or**
- SBC (e.g. Raspberry Pi 4B)
- Supported WiFi adapter (USB)
- Display (monitor, goggles, etc.)
- Optional: Antenna upgrades

---

## 2) Supported / Recommended SBC Options

### Air (Preferred → Alternative)
1. **Raspberry Pi CM4 + carrier board**
   - Best performance
   - Small + lightweight
2. **Raspberry Pi 4B**
   - Budget-friendly
   - Good enough for most setups

### Ground
- Laptop (best performance)
- Raspberry Pi 4B

---

## 3) Camera Options

> **Most stable option:** Raspberry Pi Foundation CSI cameras  
> HD → best latency + stability  

### Recommended CSI Cameras
- Raspberry Pi Camera Module V1
- Raspberry Pi Camera Module V2
- Raspberry Pi HQ Camera (IMX477)
- Arducam IMX Camera Modules (e.g., IMX519) — compatible clones that include authentication chip

### Notes
- Must support the Raspberry Pi camera interface + security chip
- Latency + resolution depend on sensor + Pi performance

### Special / USB Camera Options
- Some USB cameras supported
- USB thermal camera examples:
  - Hti-301
  - Infiray T2

> USB = higher latency. Only recommended for special use cases.

### HDMI Input (via HDMI-to-CSI)
- Some HDMI → CSI boards supported
- Latency increases
- Useful for external HDMI cameras

---

## 4) WiFi Adapter Options

> Only specific WiFi chipsets work reliably (must support monitor mode and oversampling).

### Recommended Chipsets
- RTL8812AU
- RTL8812BU
- RTL8811AU
- RTL8814AU
- RTL8822EU

### Good Adapters
| Adapter | Notes |
|--------|-------|
| ASUS USB-AC56 | Very popular, stable |
| ALFA AWUS036AC | Long-range option |
| Alfa AWUS036ACH | Alternative long-range |
| EDUP adapters with RTL8812AU | Budget |
| Generic RTL8812AU dongles | Can work; verify quality |

> Good power supply is critical

---

## 5) Storage
- microSD card
  - 16 GB minimum
  - 32 GB recommended
- CM4 models with eMMC also supported

---

## 6) Antennas
- Standard dipoles work
- For long range:
  - Directional antennas
  - High-gain antennas
  - Matching antennas → better RSSI / SNR

---

## 7) Power / Wiring
- 5 V regulated BEC required
- Must supply:
  - SBC
  - WiFi USB device (may pull >1A)
- Good connectors + wiring recommended

---
# OpenHD Performance Build (High-End)

---

## 1) Air Unit (On Drone)

### SBC
- **Raspberry Pi Compute Module 4 (CM4)**
  - Recommended: 4–8 GB RAM, eMMC


### Carrier Board
- Any CM4 carrier board with:
  - CSI socket
  - USB port (for WiFi dongle)
  - Good power input
- Examples:
  - Waveshare CM4 IO Board
  - BIGTREETECH CB1/CM4 board
  - ArduCam CM4 carrier

### Camera
- **Raspberry Pi HQ Camera (IMX477)**
- Lens recommendation:
  - 6–12 mm lenses (good FOV + sharpness)

Optional upgrade:
- Arducam IMX519 or IMX462 (low-light)

### WiFi Adapter (Air)
- **ASUS USB-AC56**
- **Alternative upgrades**
  - Alfa AWUS036AC / AWUS036ACH

### Power
- **5V BEC, 3A minimum (continuous)**
  - Recommended: 4–6A peak
- Noise-filtered preferred

### Cooling
- Passive + optional micro-fan

### Storage
- 32 GB microSD or CM4 eMMC

---

## 2) Ground Unit

### Device
- **Laptop** (recommended)
  - i5 / Ryzen 5 or better
or
- **Raspberry Pi 4B**

### WiFi Adapter (Ground)
- **Alfa AWUS036AC / AWUS036ACH**

Optional:
- Second adapter for diversity reception

### Antennas
- Directional for long range:
  - Patch
  - Helical
  - Yagi
- Omnis for short range
  - Dipoles or pagodas

---

## 3) Antennas (Both Sides)

### Air Unit
- Lightweight dipole (RHCP/LHCP pair)

### Ground Station
- **Long-Range Pair**
  - Directional (helical / patch / yagi)
  - Omnidirectional diversity

---

## 4) Optional Upgrades

### OSD / Telemetry
- MAVLink telemetry embedded into video

### Diversity Receiving
- Multiple WiFi adapters improves stability and distance

### DVR (Ground)
- Record HD feed to disk
- Recommended: laptop → ffmpeg / OpenHD receiver

---

## 5) Complete Shopping List

| Component | Recommended |
|----------|-------------|
| Air SBC | CM4 |
| Carrier | Waveshare / ArduCam |
| Camera | Pi HQ (IMX477) |
| Air WiFi | ASUS USB-AC56 |
| Air Antenna | Lightweight dipole |
| Ground Device | Laptop |
| Ground WiFi | Alfa AWUS036AC / ACH |
| Ground Antenna | Patch / Helical |
| Storage | CM4 eMMC / 32GB SD |
| Power | 5V BEC 3–6A |
| Cooling | CM4 heatsink |

---

## 6) Notes

- CSI camera → lowest latency
- CM4 handles encoding more reliably than Pi 4B
- High-gain antennas dramatically increase range
- Long-range performance depends on:
  - Antenna choice
  - Fresnel zone clearance
  - Ground station placement
- Use short cables + keep RF hardware away from ESC noise

---



