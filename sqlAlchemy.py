from sqlalchemy import create_engine

engine = create_engine(
    'snowflake://{user}:{password}@{account}/'.format(
        user='sunilmakwana',
        password='Azl-886628',
        account='wn87522.west-europe.azure'
    )
)
try:
    connection = engine.connect()
    results = connection.execute('select current_version()').fetchone()
    print(results[0])
finally:
    connection.close()
    engine.dispose()
