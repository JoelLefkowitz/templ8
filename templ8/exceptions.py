class MissingConfig(Exception):
    def __init__(self, key: str) -> None:
        super().__init__(f"\nMissing config: {key} not found in config file")


class OutputDirInvalid(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"\nInvalid output directory: {path}")


class InvalidCommand(Exception):
    def __init__(self, command: str, cli: str) -> None:
        super().__init__(f"\nInvalid command: {command}\n{cli}")


class ConfigPathInvalid(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"\nInvalid configuration path: {path}")
