import nuke
import math

# Add a new backdrop function
def db_backdrop_add():
    
    # Get tile and grid sizes from Nuke preferences
    nuke_preferences = nuke.toNode('preferences')
    grid_w = nuke_preferences['GridWidth'].getValue()
    grid_h = nuke_preferences['GridHeight'].getValue()
    tile_w = nuke_preferences['TileWidth'].getValue()
    tile_h = nuke_preferences['TileHeight'].getValue()
    
    # Set padding
    pad_top = 8
    pad_bottom = 5
    pad_side = 1

    # Set align step
    step_x = grid_w * 2
    step_y = grid_h * 2

    # Set font size
    font_size = tile_h * 2

    # Setup backdrop
    selected_nodes = nuke.selectedNodes()
    if selected_nodes:
        # Backdrop around selected nodes

        # Get center positions
        x_positions = [node.xpos() + (node.screenWidth() / 2) for node in selected_nodes]
        y_positions = [node.ypos() + (node.screenHeight() / 2) for node in selected_nodes]

        # Set boundaries
        min_x = min(x_positions) - (tile_w * pad_side)
        min_y = min(y_positions) - (tile_h * pad_top)
        max_x = max(x_positions) + (tile_w * pad_side)
        max_y = max(y_positions) + (tile_h * pad_bottom)
        raw_width = max_x - min_x
        raw_height = max_y - min_y

    else:
        # Lonely backdrop sized for 1 node

        # Get mouse position
        temp_node = nuke.createNode('NoOp', inPanel=False)
        m_x = temp_node.xpos()
        m_y = temp_node.ypos()
        nuke.delete(temp_node)

        # Set boundaries
        min_x = m_x - (tile_w * pad_side)
        min_y = m_y - (tile_h * pad_top)
        max_x = m_x + (tile_w * pad_side)
        max_y = m_y + (tile_h * pad_bottom)
        raw_width = max_x - min_x
        raw_height = max_y - min_y

    # Set backdrop size
    bd_width = int(math.ceil(raw_width / step_x) * step_x)
    bd_height = int(math.ceil(raw_height / step_y) * step_y)

    # Align backdrop to grid
    bd_x = int(math.floor(min_x / grid_w) * grid_w)
    bd_y = int(math.floor(min_y / grid_h) * grid_h)

    # Create Backdrop aligned to grid
    backdrop = nuke.nodes.BackdropNode(
        xpos=bd_x,
        ypos=bd_y,
        bdwidth=bd_width,
        bdheight=bd_height,
        tile_color=int(0x7f7f7fff),
        note_font_size=font_size
    )

# Align all selected backdrops to grid function
def db_backdrop_align():

    # Check selection exist
    selection = nuke.selectedNodes()
    if not selection:
        return

    # Check backdrops in selection exist
    selected_backdrops = [n for n in selection if n.Class() == 'BackdropNode']
    if not selected_backdrops:
        return

    # Deselect others
    for node in selection:
        if node.Class() != 'BackdropNode':
            node['selected'].setValue(False)
  
    # Get grid size from Nuke preferences
    nuke_preferences = nuke.toNode('preferences')
    grid_w = nuke_preferences['GridWidth'].getValue()
    grid_h = nuke_preferences['GridHeight'].getValue()

    # Set align step
    step_x = grid_w * 2
    step_y = grid_h * 2

    # Align all selected backdrops one by one
    for backdrop in selected_backdrops:

        # Get position and size
        x_min_pos = backdrop.xpos()
        y_min_pos = backdrop.ypos()

        if backdrop.knob('bdwidth') and backdrop.knob('bdheight'):
            raw_width = backdrop['bdwidth'].getValue()
            raw_height = backdrop['bdheight'].getValue()
        else:
            raw_width = backdrop.screenWidth()
            raw_height = backdrop.screenHeight()

        # Set backdrop size
        bd_width = int(round(raw_width / step_x) * step_x)
        bd_height = int(round(raw_height / step_y) * step_y)

        # Align backdrop to grid
        bd_x = int(round(x_min_pos / grid_w) * grid_w)
        bd_y = int(round(y_min_pos / grid_h) * grid_h)

        # Apply new size and position
        backdrop['xpos'].setValue(bd_x)
        backdrop['ypos'].setValue(bd_y)
        backdrop['bdwidth'].setValue(bd_width)
        backdrop['bdheight'].setValue(bd_height)