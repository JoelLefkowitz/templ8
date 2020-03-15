class MissingConfig(Exception):
    def __init__(self, key: str) -> None:
        super().__init__(f"\n\nMissing config: {key} not found in config file")


class OutputDirInvalid(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"\n\nInvalid output directory: {path}")


class InvalidCommand(Exception):
    def __init__(self, command: str, cli: str) -> None:
        super().__init__(f"\n\nInvalid command: {command}\n\n{cli}")


class ConfigPathInvalid(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"\n\nInvalid configuration path: {path}")
