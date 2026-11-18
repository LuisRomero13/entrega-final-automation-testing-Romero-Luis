import logging
import pathlib
from logging.handlers import RotatingFileHandler

# Carpeta donde se almacenan los logs de la suite
audit_dir = pathlib.Path(__file__).resolve().parent.parent / "logs"
audit_dir.mkdir(exist_ok=True)

# Logger centralizado para toda la suite
logger = logging.getLogger("talentolab")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = RotatingFileHandler(
        audit_dir / "suite.log",
        maxBytes=1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    logger.addHandler(handler)
    logger.propagate = False
