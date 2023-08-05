# Clock Api Project

This project aims to provide a functionality to calculate the smallest angle between the two clock arrows, given the values of hour and minute represented. The interaction with the application is done via GET request, still providing the possibility of persisting operations recordings in a local dB.

## Prerequisites

- Python 3.x
- Flask 2.3.2
- PostgreSQL (if using it locally, with persistance, and the database "test_db" must be previously created)

## Files disposition

```
│
├─ app.py: application entrypoint
│
│        ┌─clock_calculator.py: business rules for obtaining final result
├─ src  ─┤
│        └─tools.py: business rules unrelated to the calculation
│
├─ db   ── connector.py: functions required to connect to the database
│
├─ logs ── app.log:
│
│        ┌─conftest.py: Definition of fixtures for the tests
│        │
├─ tests ┼─int_test.py: Integration tests
│        │
│        └─unit_test.py:Unit tests
│
├──Dockerfile: Commands to create the container
│
├─ README.md:  readme file
│
└─ requirements.txt: Definition of dependencies

```

## Installation

1. Clone the repository:

    <div align="center">

   ```bash
   git clone https://github.com/aogdrummond/clock-api.git
   ```
2. Navigate to the project directory:
    <div align="center">

    ```bash
    cd clock-api
    ```
3. Create virtual environment:
    <div align="center">

    ```bash
    python3 -m venv clock_api_venv
    ```
4. Activate the virtual environment:
    <div align="center">

    ```bash
    venv/Scripts/activate (Windows)
    or
    venv/bin/activate (Linux)
    ```

5. Install the required dependencies in virtual enviroonment:
    <div align="center">

    ```bash
    pip install -r requirements.txt
    ```

# Usage

### Local:

```
python3 app.py

```
### Containerized:

```
1. docker build –tag clock-api .
```
```
2. docker run -d -p 5000:5000 clock-api
```


# How to use the automatted tests

### Unit tests:

```
python3 tests\unit_tests.py 
```
### Integration tests (requires the application to be running):.

```
python3 tests\int_tests.py 
```