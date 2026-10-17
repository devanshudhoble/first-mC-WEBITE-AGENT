"""A minimal sample agent: reads a goal, picks a tool, acts, and reports.

No external dependencies. Run with:  python agent.py
"""
import datetime


def tool_time(_: str) -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def tool_calc(expr: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if not set(expr) <= allowed:
        return "Only basic arithmetic is supported."
    return str(eval(expr))


def tool_echo(text: str) -> str:
    return text


TOOLS = {"time": tool_time, "calc": tool_calc, "echo": tool_echo}


def choose_tool(message: str):
    msg = message.lower()
    if "time" in msg or "date" in msg:
        return "time", ""
    if msg.startswith("calc "):
        return "calc", message[5:]
    return "echo", message


def run(message: str) -> str:
    name, arg = choose_tool(message)
    result = TOOLS[name](arg)
    return f"[agent used '{name}'] {result}"


if __name__ == "__main__":
    print("Sample agent ready. Try: 'what time is it', 'calc 2*(3+4)', or anything. Type 'exit' to quit.")
    while True:
        try:
            msg = input("> ").strip()
        except EOFError:
            break
        if msg.lower() in {"exit", "quit"}:
            break
        print(run(msg))
