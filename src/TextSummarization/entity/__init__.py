from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
   root_dir: Path
   source_URL: str
   local_data_file: Path
   unzip_dir: Path


                                         # frozen means once the instance of the class is created, you cannot change its attributes.
@dataclass(frozen=True)                  # This can be useful for creating objects that should not be changed after they are created.
class DataValidationConfig:
   root_dir: Path
   STATUS_FILE: str
   ALL_REQUIRED_FILES: list