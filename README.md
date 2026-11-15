# DB Backdrop

A toolset for Foundry Nuke. Creates grid-aligned backdrops and snaps existing backdrops to the even grid lines.

<p align="center"><img width="2400" height="1500" alt="db_backdrop_example" src="https://github.com/user-attachments/assets/a5f52b50-bbfa-43f3-8d50-3690036d7abe" /></p>

---

## Core Features

- **Grid-Aligned Creation:** Spawns new backdrops that automatically snap their dimensions and positions to the even grid lines with smart padding based on node tiles.
- **Existing Backdrop Alignment:** Aligns already created backdrops to the nearest even grid lines in a single click. Works with multiple selected backdrops at once while filtering out internal nodes.

---

## Installation

1. Download the latest version from the **[Releases page](https://github.com/baramov/DB_Backdrop/releases)**.
2. Place the entire `DB_Backdrop` folder (containing `db_backdrop.py` and `menu.py`) into your `.nuke` directory.
3. Add the line below to your **`~/.nuke/init.py`**:

```python
nuke.pluginAddPath('./DB_Backdrop')
```

---

## Usage & Hotkeys

After restarting Nuke, a new **`DB Tools`** menu will appear in the top menu bar. Under **`DB Tools -> DB Backdrop`**, you will find the following commands and their registered hotkeys:

### 1. Create new (`Alt + B`)
- **With Selection:** Select a couple of nodes and press `Alt + B` to wrap them in a grid-aligned backdrop.
- **Without Selection:** Press `Alt + B` over an empty area to drop an empty aligned backdrop.

### 2. Align to grid (`Alt + Shift + B`)
- Select one or multiple backdrops.
- Press `Alt + Shift + B`. 
- The script automatically filters out regular nodes and snaps the boundaries of all selected backdrops to the nearest even grid lines.

---

## Compatibility
- Supported Versions: **Nuke 13.0 or later**.
- OS Compatibility: Windows, Linux, macOS.
