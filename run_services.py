from main_service import MainService 
from alert_service import AlertService
from multiprocessing import Process

def run_alert_service():
    alert_service = AlertService()

def run_main_service():
    config_file = 'config.json'
    main_service = MainService(config_file)
    main_service.start_monitor()

if __name__ == '__main__':
    #run both services with multiprocessing
    alert_service_process = Process(target=run_alert_service)
    main_service_process = Process(target=run_main_service)

    alert_service_process.start()
    main_service_process.start()

    alert_service_process.join()
    main_service_process.join()