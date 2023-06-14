import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the dimensions of the blot
BLOT_WIDTH = 10
BLOT_HEIGHT = 20

# Define the colors for the ladder bands
BAND_COLORS = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow']

# Define the positions for the ladder bands
BAND_POSITIONS = [2, 4, 6, 8, 10, 12]

def draw_blot():
    fig, ax = plt.subplots()

    # Draw the blot as a rectangle
    blot = patches.Rectangle((0, 0), BLOT_WIDTH, BLOT_HEIGHT, fill=True, color='grey')
    ax.add_patch(blot)

    # Set the limits of the plot
    plt.xlim([-5, BLOT_WIDTH + 5])
    plt.ylim([-5, BLOT_HEIGHT + 5])

    return ax

def draw_ladder(ax):
    # Draw each band of the ladder
    for color, position in zip(BAND_COLORS, BAND_POSITIONS):
        ax.hlines(position, 0, BLOT_WIDTH, colors=color, linestyles='solid')

    return ax

def main():
    # Draw the blot
    ax = draw_blot()

    # Draw the ladder
    ax = draw_ladder(ax)

    # Show the blot with the ladder
    plt.show()

if __name__ == "__main__":
    main()
