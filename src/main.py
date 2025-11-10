import subprocess
from rich.console import Console
from datetime import datetime
import os

console = Console()

# Default mode
TEACHING_MODE = False

# Ensure logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "session.log")

def log_interaction(user_input: str, response: str, mode: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] Mode: {mode}\n")
        f.write(f"User: {user_input}\n")
        f.write(f"Assistant: {response}\n\n")

def llm_suggest_command(user_input: str, teaching: bool) -> str:
    if teaching:
        prompt = f"Suggest a pentest command for: {user_input}. Respond with the command AND a short explanation."
    else:
        prompt = f"Suggest a pentest command for: {user_input}. Respond ONLY with the command."

    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True, text=True
    )
    return result.stdout.strip()

def main():
    global TEACHING_MODE
    console.print(f"[bold green]RedLLM Pentest Assistant (Ollama Edition)[/bold green]")
    console.print(f"[blue]Current Mode:[/blue] {'Teaching' if TEACHING_MODE else 'Command-Only'}")

    while True:
        user_input = console.input("[cyan]>> [/cyan]")

        # Exit
        if user_input.lower() in ["exit", "quit"]:
            break


# Mode switch
        if user_input.lower().startswith("mode"):
            if "teaching" in user_input.lower():
                TEACHING_MODE = True
                console.print("[green]Switched to Teaching Mode[/green]")
            elif "command" in user_input.lower():
                TEACHING_MODE = False
                console.print("[green]Switched to Command-Only Mode[/green]")
            else:
                console.print("[red]Unknown mode. Use 'mode teaching' or 'mode command'.[/red]")
            continue

        # Normal query
        command = llm_suggest_command(user_input, TEACHING_MODE)
        console.print(f"[yellow]Suggested:[/yellow] {command}")

        # Log interaction
        mode_text = "Teaching" if TEACHING_MODE else "Command-Only"
        log_interaction(user_input, command, mode_text)

if __name__ == "__main__":
    main()


