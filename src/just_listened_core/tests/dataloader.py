from pathlib import WindowsPath

from just_listened_core.adapters import deserializer_adapter_function


class PathWithLoaders(WindowsPath):
    def from_json(self) -> dict:
        return deserializer_adapter_function(self.read_bytes())


_DATA_PATH = PathWithLoaders(__file__).parent / "data"


class DataPath:
    def __init__(self, rel_file_path: str):
        self._file = _DATA_PATH / rel_file_path
        assert self._file.exists(), f"testing data '{self._file}' not found"

    def __get__(self, obj, objtype=None):
        return self._file


class DataLoader:
    OAUTH_VERIFY_TOKEN_RESPONSE = DataPath("requests/oauth_verify_token_response.json")
    SPOTIFY_SEARCH_RESULT = DataPath("json/spotify_search_result.json")
