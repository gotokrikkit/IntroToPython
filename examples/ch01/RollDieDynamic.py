# RollDieDynamic.py
"""Dynamically graphing frequencies of die rolls."""
from matplotlib import animation
import matplotlib.pyplot as plt
import random 
import seaborn as sns
import sys

# Check if the required number of command-line arguments are provided
if len(sys.argv) == 3:
    try:
        number_of_frames = int(sys.argv[1])
        rolls_per_frame = int(sys.argv[2])
    except ValueError:
        print("Arguments must be integers.")
        sys.exit(1)
    if number_of_frames <= 0 or rolls_per_frame <= 0:
        print("Arguments must be positive integers.")
        sys.exit(1)
else:
    print("You didn't provide the arguments at start.")
    try:
        number_of_frames = int(input("Enter the number of frames: "))
        rolls_per_frame = int(input("Enter the number of rolls per frame: "))
        if number_of_frames <= 0 or rolls_per_frame <= 0:
            print("Both numbers must be positive integers.")
            sys.exit(1)
    except ValueError:
        print("Both inputs must be integers.")
        sys.exit(1)

def update(frame_number, rolls, faces, frequencies):
    """Configures bar plot contents for each animation frame."""
    # roll die and update frequencies
    for i in range(rolls):
        frequencies[random.randrange(1, 7) - 1] += 1 

    # reconfigure plot for updated die frequencies
    plt.cla()  # clear old contents contents of current Figure
    axes = sns.barplot(x=faces, y=frequencies, palette='bright')  # new bars
    axes.set_title(f'Die Frequencies for {sum(frequencies):,} Rolls')
    axes.set(xlabel='Die Value', ylabel='Frequency')  
    axes.set_ylim(top=max(frequencies) * 1.10)  # scale y-axis by 10%

    # display frequency & percentage above each patch (bar)
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0  
        text_y = bar.get_height() 
        text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')

sns.set_style('whitegrid')  # white backround with gray grid lines
figure = plt.figure('Rolling a Six-Sided Die')  # Figure for animation
values = list(range(1, 7))  # die faces for display on x-axis
frequencies = [0] * 6  # six-element list of die frequencies

# configure and start animation that calls function update
die_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames - 1, interval=33,
    fargs=(rolls_per_frame, values, frequencies))
plt.show()  # display window
