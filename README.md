# pythonTestParallel
Investigate how to work with parallel in python

- use  pytest -n8 to run tests where '-n' flag to identify number of streams streams

#xdist
- pip install pytest-xdist
 - поддерживает несколько типов планировщиков:

- load (по умолчанию): каждый тест выполняется в отдельном воркере
- loadscope: тесты-функции из одного файла выполняются в одном воркере, тесты-методы из одного тесткласса выполняются в одном воркере
- loadfile: тесты из одного файла выполняются в одном воркере
- each: весь набор тестов прогоняется в каждом воркере отдельно, т.е. как если бы прогон тестов выполнялся параллельно в нескольких терминалах сразу.

В самом тесте это не настраивается, но можно вынести опции в файл конфигурации pytest.ini:

[pytest]

addopts = --dist=loadfile
