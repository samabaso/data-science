import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to draw a positional play pitch with players and updated divisions
def draw_positional_play_pitch_with_custom_lines():
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 7))

    # Set pitch dimensions
    pitch_length = 105  # in meters
    pitch_width = 68    # in meters

    # Penalty area distance from goal line
    penalty_box_y = 22.3

    # Add pitch outer boundary
    ax.plot([0, 0, pitch_length, pitch_length, 0], [0, pitch_width, pitch_width, 0, 0], color="black")
    
    # Vertical zones
    outer_vertical_line_x = [16.5, pitch_length - 16.5]  # Align with penalty box
    inner_vertical_line_x = [
        pitch_length * 0.375,  # 50% between outer vertical line and centerline
        pitch_length * 0.625
    ]
    
    vertical_lines_x = outer_vertical_line_x + inner_vertical_line_x
    for x in vertical_lines_x:
        ax.plot([x, x], [0, pitch_width], color="black", linestyle='--')

    # Horizontal zones
    # Horizontal lines 50% away from the outer edge and inner edge
    outer_horizontal_line_y = [pitch_width * 0.125, pitch_width * 0.875]  # 50% from outer edge
    inner_horizontal_line_y = [penalty_box_y, pitch_width - penalty_box_y]  # Align with penalty box
    
    horizontal_lines_y = outer_horizontal_line_y + inner_horizontal_line_y
    for y in horizontal_lines_y:
        # Skip drawing horizontal line between LB and CM1
        if y == 30.3:  # This is the line at LB's y-coordinate
            continue
        ax.plot([0, pitch_length], [y, y], color="black", linestyle='--')

    # Highlight the half-spaces
    ax.add_patch(patches.Rectangle((pitch_length * 0.125, 0), pitch_length * 0.25, pitch_width, fill=True, color='lightblue', alpha=0.3))
    ax.add_patch(patches.Rectangle((pitch_length * 0.625, 0), pitch_length * 0.25, pitch_width, fill=True, color='lightblue', alpha=0.3))

    # Add the halfway line
    ax.plot([pitch_length / 2, pitch_length / 2], [0, pitch_width], color="black")

    # Add center circle and kickoff spot (making center circle black)
    center_circle = plt.Circle((pitch_length / 2, pitch_width / 2), 9.15, color="black", fill=False)
    ax.add_patch(center_circle)
    ax.plot(pitch_length / 2, pitch_width / 2, 'bo')

    # Add penalty areas
    # Left penalty area
    ax.plot([0, 16.5, 16.5, 0], [22.3, 22.3, pitch_width - 22.3, pitch_width - 22.3], color="black")
    # Right penalty area
    ax.plot([pitch_length, pitch_length - 16.5, pitch_length - 16.5, pitch_length],
            [22.3, 22.3, pitch_width - 22.3, pitch_width - 22.3], color="black")
    
    # Add 6-yard boxes
    # Left 6-yard box
    ax.plot([0, 5.5, 5.5, 0], [30.3, 30.3, pitch_width - 30.3, pitch_width - 30.3], color="black")
    # Right 6-yard box
    ax.plot([pitch_length, pitch_length - 5.5, pitch_length - 5.5, pitch_length],
            [30.3, 30.3, pitch_width - 30.3, pitch_width - 30.3], color="black")

    # Add goals
    # Left goal
    ax.plot([-2.44, 0], [pitch_width / 2 - 3.66, pitch_width / 2 - 3.66], color="black")
    ax.plot([-2.44, 0], [pitch_width / 2 + 3.66, pitch_width / 2 + 3.66], color="black")
    ax.plot([-2.44, -2.44], [pitch_width / 2 - 3.66, pitch_width / 2 + 3.66], color="black")
    
    # Right goal
    ax.plot([pitch_length, pitch_length + 2.44], [pitch_width / 2 - 3.66, pitch_width / 2 - 3.66], color="black")
    ax.plot([pitch_length, pitch_length + 2.44], [pitch_width / 2 + 3.66, pitch_width / 2 + 3.66], color="black")
    ax.plot([pitch_length + 2.44, pitch_length + 2.44], [pitch_width / 2 - 3.66, pitch_width / 2 + 3.66], color="black")

    # Add corner arcs
    corner_radius = 1
    # Bottom left corner
    corner_arc_bl = patches.Arc((0, 0), corner_radius * 2, corner_radius * 2, angle=0, theta1=0, theta2=90, color='black')
    ax.add_patch(corner_arc_bl)
    # Bottom right corner
    corner_arc_br = patches.Arc((pitch_length, 0), corner_radius * 2, corner_radius * 2, angle=0, theta1=90, theta2=180, color='black')
    ax.add_patch(corner_arc_br)
    # Top left corner
    corner_arc_tl = patches.Arc((0, pitch_width), corner_radius * 2, corner_radius * 2, angle=0, theta1=270, theta2=360, color='black')
    ax.add_patch(corner_arc_tl)
    # Top right corner
    corner_arc_tr = patches.Arc((pitch_length, pitch_width), corner_radius * 2, corner_radius * 2, angle=0, theta1=180, theta2=270, color='black')
    ax.add_patch(corner_arc_tr)

    # Set the pitch background color to green
    ax.set_facecolor('green')

    # Set axis limits and remove labels
    ax.set_xlim(-3, pitch_length + 3)
    ax.set_ylim(-3, pitch_width + 3)
    ax.set_xticks([])
    ax.set_yticks([])

    # Add players for both teams in 4-2-3-1 formation
    # Team 1 (left to right)
    team1_positions = [
        (8, 34),    # GK
        (20, 55),   # LB
        (20, 13),   # RB
        (30, 44),   # CB1
        (30, 24),   # CB2
        (45, 48),   # CM1
        (45, 20),   # CM2
        (65, 55),   # LW
        (65, 13),   # RW
        (55, 34),   # CAM
        (80, 34)    # ST
    ]
    team1_labels = ['GK', 'LB', 'RB', 'CB1', 'CB2', 'CM1', 'CM2', 'LW', 'RW', 'CAM', 'ST']

    for pos, label in zip(team1_positions, team1_labels):
        ax.plot(pos[0], pos[1], 'ro')
        ax.text(pos[0], pos[1]-2, label, ha='center', va='center', color='white', fontsize=8)

    # Team 2 (right to left)
    team2_positions = [
        (97, 34),   # GK
        (85, 55),   # LB
        (85, 13),   # RB
        (75, 44),   # CB1
        (75, 24),   # CB2
        (60, 48),   # CM1
        (60, 20),   # CM2
        (40, 55),   # LW
        (40, 13),   # RW
        (50, 34),   # CAM
        (25, 34)    # ST
    ]
    team2_labels = ['GK', 'LB', 'RB', 'CB1', 'CB2', 'CM1', 'CM2', 'LW', 'RW', 'CAM', 'ST']

    for pos, label in zip(team2_positions, team2_labels):
        ax.plot(pos[0], pos[1], 'bo')
        ax.text(pos[0], pos[1]-2, label, ha='center', va='center', color='white', fontsize=8)

    # Show plot
    plt.show()

# Call the function to draw the pitch with custom lines
draw_positional_play_pitch_with_custom_lines()
