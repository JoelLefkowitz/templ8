from dataclases import dataclass
from typing import Optional
import subprocess


@dataclass
class Callback:
    name: str
    call: str
    cwd: Optional[str] = None

    def __call__(self, output_dir: str) -> subprocess.CompletedProcess:
        call = self.call.split(" ")
        cwd = os.path.join(output_dir, self.cwd) if self.cwd else output_dir
        return subprocess.run(call, cwd=cwd)

    def __repr__(self) -> str:
        return str(self.__dict__)
