import configparser

# Load config.ini
parser = configparser.ConfigParser()
parser.read("src/conf/config.ini")

# Read DB credentials from the config file
db_user = parser.get("DB", "USER")
db_password = parser.get("DB", "PASSWORD")
db_name = parser.get("DB", "DB_NAME")
db_host = parser.get("DB", "DOMAIN")
db_port = parser.get("DB", "PORT")


class Config:
    DB_URL = (
        f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )


config = Config
