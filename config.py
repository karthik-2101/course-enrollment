class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sql_server:21012002@localhost/flaskapi?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False