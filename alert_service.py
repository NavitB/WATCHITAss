from flask import Flask, request
import logging


class AlertService:
    
    def __init__(self):
        logging.basicConfig(filename='alerts.log', level=logging.WARNING, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger('werkzeug') #Flask app logs
        logger.setLevel(logging.ERROR) #log only errors for Flask app
        self.app = Flask(__name__)

        self.setup_routes()
        self.app.run(host='localhost', port=5000) #the alert_service will start run when initiated

    def setup_routes(self):
        @self.app.route('/alert', methods=['POST'])
        def alert():
            alert_data = request.json
            logging.warning(f"Alert received: {alert_data}")
            #print to terminal also
            # print(f"Alert received: {alert_data}")
            return "Alert processed", 200
    

#run the alert service seperatly 
if __name__ == "__main__":
    service = AlertService()