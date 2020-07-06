from typing import Dict, List


class InvalidCommand(Exception):
    def __init__(self, command: List[str], cli: str) -> None:
        super().__init__(f"Invalid command: {command}\n\n{cli}")


class InvalidConfigPath(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Invalid configuration path: {path}")


class InvalidOutputDir(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Invalid output directory: {path}")


class ConfigTypeError(Exception):
    def __init__(self) -> None:
        super().__init__(f"Config must be a single depth dictionary")


class MissingContext(Exception):
    def __init__(self, context: str, config: Dict) -> None:
        super().__init__(f"Missing context: {context}\nNot found in config: {config}")
