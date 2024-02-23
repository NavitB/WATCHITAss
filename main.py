from MainService import MainService 

if __name__ == "__main__":
    config_file = 'config.json'
    main_service = MainService(config_file)
    main_service.start()
