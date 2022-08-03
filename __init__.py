"""Top-level package for FruitBasket."""
# fruitBasket/__init__.py

__app_name__ = "fruitBasket"
__version__ = "0.1.0"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    NOT_FOUND_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(8)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    NOT_FOUND_ERROR: "file not found error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    ID_ERROR: "to-do id error",
}