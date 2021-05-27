from configparser import ConfigParser

def credentials(filename='database.ini', section='postgresql'):
    """Fetches database credentials.

    Retrieves PostgreSQL Database credentials by reading .ini file using ConfigParser()

    Args:
        filename: Path of the file that contains database credentials to be read.
        section: Specifies which section of the file is to be read.

    Returns:
        A dictionary which contains database credentials as key-value pairs.

        For example: 
            {
                "host":"localhost",
                "database": "databaseName"
                "user":"userName"
                "password"="1234"
            } 
    """

    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db
