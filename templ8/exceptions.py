from typing import Dict, List


class MissingConfig(Exception):
    def __init__(self, string: str, config: Dict) -> None:
        super().__init__(f"\n\nMissing config: {string} not found in config file")


class OutputDirInvalid(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"\n\nInvalid output directory: {path}")


class InvalidCommand(Exception):
    def __init__(self, command: List[str], cli: str) -> None:
        super().__init__(f"\n\nInvalid command: {command}\n\n{cli}")


class ConfigPathInvalid(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"\n\nInvalid configuration path: {path}")
