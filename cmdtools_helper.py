import cmdtools
from cmdtools.ext.command import Group

__version__ = "0.0.1"


def exec_group(group: Group, command: cmdtools.Cmd, attrs: dict | None = None):
    if attrs is None:
        attrs = {}

    for cmd in group.commands:
        if command.name == cmd.name or command.name in cmd.aliases:
            executor = cmdtools.Executor(cmd, cmd.callback, attrs=attrs)

            return executor.exec()

    raise cmdtools.NotFoundError(f"Command not found: {command.name}", command.name)
