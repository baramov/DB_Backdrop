# DB Backdrop

A toolset for **Foundry Nuke**. Creates smart, grid-aligned backdrops and snaps existing backdrops to the even grid lines.

## Core Features

- **Grid-Aligned Creation:** Spawns new backdrops that automatically snap their dimensions and positions to the even grid lines with smart padding based on node tiles.
- **Existing Backdrop Alignment:** Aligns already created backdrops to the nearest even grid lines in a single click. Works with multiple selected backdrops at once while filtering out internal nodes.

---

## Installation & Setup

### 1. Copy the Directory
Place the entire `DB_Backdrop` folder (containing `db_backdrop.py` and `menu.py`) into your `.nuke` directory.

### 2. Configure `init.py`
Add the line below to your **`~/.nuke/init.py`**:

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
- Supported Versions: **Nuke 13, 14, 15, and 16+**.
- OS Compatibility: Windows, Linux, macOS.
