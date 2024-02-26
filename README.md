# Sensor Data Monitoring Service
This Python-based project monitors sensor data, including temperature, humidity, and pressure. It validates the data against configurable rules defined in a `config.json` file and logs alerts for any invalid data detected. The system is designed to run both a main monitoring service and an alert service, either concurrently or separately.

## Project Structure
* `sensors.py`: Contains the abstract sensor class and specific sensor classes (e.g., TemperatureSensor, HumiditySensor, PressureSensor) that inherit from it.
* `config.json`: Configuration file specifying the types of sensors connected and their valid data ranges.
* `run_services.py`: Script to run both the main monitoring service and the alert service concurrently using multiprocessing.
* `main_service.py`: Script for running the main monitoring service independently.
* `alert_service.py`: Script for running the alert service independently.
* `alerts.log`: File where the alert service logs all detected invalid sensor data.
## Prerequisites
Ensure Python 3.x is installed on your system. This project also uses Flask for the alert service, which can be installed via pip:
```
pip install flask
```
## Configuration
Sensor types and their valid data ranges are configured in `config.json`. Modify this file to adjust the monitoring parameters for each sensor type.

Example `config.json` structure:

```
{
  "sensors": [
    {
      "type": "TemperatureSensor",
      "valid_range": [0, 100]
    },
    {
      "type": "HumiditySensor",
      "valid_range": [0, 100]
    },
    {
      "type": "PressureSensor",
      "valid_range": [900, 1100]
    }
  ]
}
```
## Running Services Together
To run both the monitoring and alert services concurrently in the same execution environment, use the `run_services.py` script. This utilizes multiprocessing to run each service in its own process:
```
python run_services.py
```
## Running Services Separately
If you prefer to run the MainService and AlertService in separate terminals or need to debug them individually, you can use the standalone scripts.

### Main Service
To start monitoring sensor data, execute the following command in a terminal:
```
python main_service.py
```
### Alert Service
To start the alert service that listens for notifications, open a new terminal and execute:
```
python alert_service.py
```

## Alert Notifications and Logging
When `main_service.py` detects invalid sensor data, it sends an alert to `alert_service.py` via an HTTP POST request. The alert service processes these notifications and logs them to an `alerts.log` file.

### Logging to File
The alert service is configured to write logs to `alerts.log`. Each log entry contains details about the invalid sensor data received, including the timestamp, sensor type, and the invalid data value.

## Extending the Project
To add more sensor types or adjust validation logic, modify sensors.py and config.json as needed. The system is designed for easy extension to accommodate additional types of sensors and validation rules.

