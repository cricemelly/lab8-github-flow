from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
from rich.panel import Panel

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')
    console = Console()
    
    intro = Text("You wake up in a dark forest. You can go left or right.", style="magenta2")
    console.print(Panel(intro, title="Adventure Time"))

    while True:
        choice = Prompt.ask("[bright_magenta]Which direction do you choose? [/bright_magenta]", choices=["left", "right", "exit"])
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        result = (step(choice, events))
        console.print(result)
