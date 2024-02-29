from typing import Any, Optional, Dict

from gunicorn.app.base import BaseApplication


class StandaloneApplication(BaseApplication):
    def __init__(
        self,
        application: Any,
        options: Optional[Dict[str, Any]] = None,
    ):
        self._options = options or {}
        self._application = application

        super().__init__()

    def load_config(self) -> None:
        config = {
            key: value
            for key, value in self._options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self) -> Any:
        return self._application
