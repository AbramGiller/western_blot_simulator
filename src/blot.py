import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the dimensions of a single lane
LANE_WIDTH = 1
LANE_HEIGHT = 20

# Define the colors for the ladder bands
BAND_COLORS = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow']

# Define the positions for the ladder bands
BAND_POSITIONS = [2, 4, 6, 8, 10, 12]

def draw_blot_with_lanes(lanes):
    fig, ax = plt.subplots()

    # Calculate the total width of the blot based on the number of lanes
    blot_width = LANE_WIDTH * lanes

    # Draw the blot as a rectangle
    blot = patches.Rectangle((0, 0), blot_width, LANE_HEIGHT, fill=True, color='grey')
    ax.add_patch(blot)

    # Draw the lanes
    for i in range(1, lanes):
        ax.vlines(i * LANE_WIDTH, 0, LANE_HEIGHT, colors='white')

    # Draw the ladder in the first lane
    draw_ladder(ax)  # We only pass 'ax' as argument

    # Set the limits of the plot
    plt.xlim([-5, blot_width + 5])
    plt.ylim([-5, LANE_HEIGHT + 5])

    # Show the blot with the lanes and the ladder
    plt.show()

def draw_ladder(ax):
    # Draw each band of the ladder in the first lane
    for color, position in zip(BAND_COLORS, BAND_POSITIONS):
        ax.hlines(position, 0, LANE_WIDTH, colors=color, linestyles='solid', linewidth=2)

    return ax
