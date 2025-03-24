# command_parser.py
from commands import CommandSchema, NavigateCommand, ClickCommand, FillCommand, ScreenshotCommand


def parse_command(command_json: dict):
    schema = CommandSchema.parse_obj(command_json)
    action = schema.action.lower()

    if action == "navigate":
        return NavigateCommand(schema)
    elif action == "click":
        return ClickCommand(schema)
    elif action == "fill":
        return FillCommand(schema)
    elif action == "screenshot":
        return ScreenshotCommand(schema)
    else:
        raise ValueError(f"Unknown command action: {action}")
