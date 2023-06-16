from user_input import get_lanes
from blot import draw_blot_with_lanes

def main():
    lanes = get_lanes()
    draw_blot_with_lanes(lanes)

if __name__ == "__main__":
    main()

