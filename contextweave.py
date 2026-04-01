# contextweave.py - Self-healing context collapse system
from rich.console import Console
import time
from datetime import datetime

console = Console()

class ContextWeave:
    def __init__(self, max_tokens: int = 8000):
        self.max_tokens = max_tokens
        self.history = []           # Raw history
        self.compact_history = []   # Collapsed / summarized entries

    def add(self, message: str):
        """Add new message to raw history"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "content": message,
            "type": "raw"
        }
        self.history.append(entry)
        console.print(f"[blue]ContextWeave:[/blue] Added message ({len(self.history)} total)")

        # Auto-collapse if getting too large
        if len(self.history) > 15:
            self.collapse()

    def collapse(self):
        """Perform context collapse - the core missed pattern"""
        console.print("[yellow]ContextWeave:[/yellow] Performing context collapse...")

        if not self.history:
            return

        # Simple but effective collapse: keep recent + summarize older
        recent = self.history[-8:]  # Keep last 8 raw messages
        older = self.history[:-8]

        if older:
            summary = {
                "timestamp": datetime.now().isoformat(),
                "content": f"SUMMARY: {len(older)} earlier interactions. Key points: " + 
                          " | ".join([e["content"][:60] for e in older[:3]]),
                "type": "collapsed"
            }
            self.compact_history.append(summary)

        # Replace old history with collapsed version
        self.history = recent
        console.print(f"[green]ContextWeave:[/green] Collapse complete. Now tracking {len(self.history)} recent + {len(self.compact_history)} collapsed entries.")

    def get_context(self) -> str:
        """Return current usable context"""
        context_parts = []

        # Add collapsed history first (high-level view)
        for entry in self.compact_history[-3:]:
            context_parts.append(entry["content"])

        # Add recent raw messages
        for entry in self.history[-10:]:
            context_parts.append(entry["content"])

        full_context = "\n".join(context_parts)
        
        # Emergency autocompact if still too large
        if len(full_context) > self.max_tokens * 4:
            full_context = full_context[-self.max_tokens*4:]

        return full_context

    def stats(self):
        return {
            "raw_entries": len(self.history),
            "collapsed_entries": len(self.compact_history),
            "estimated_tokens": len(self.get_context()) // 4
        }


# Example usage
if __name__ == "__main__":
    cw = ContextWeave()

    console.print("[bold magenta]🚀 ContextWeave Started — Self-Healing Context System[/bold magenta]\n")

    # Simulate long conversation
    messages = [
        "User asked about IBA governance",
        "Explained Intent-Bound Authorization vs prompts",
        "Discussed Anthropic leak safety failures",
        "Built grk-html-2 visual demo",
        "Integrated Dreamweave memory",
        "Added Matey companion",
        "Created Swarmcore coordinator"
    ]

    for msg in messages:
        cw.add(msg)
        time.sleep(0.5)

    console.print("\n[bold]Final Context Stats:[/bold]", cw.stats())
    console.print("\n[bold]Current Usable Context:[/bold]")
    print(cw.get_context()[:500] + "..." if len(cw.get_context()) > 500 else cw.get_context())
