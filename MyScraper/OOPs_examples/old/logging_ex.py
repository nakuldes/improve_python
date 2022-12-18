import logging
import time

start_time = time.perf_counter()
logging.basicConfig(filename='logging_ex.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

logging.debug('This message should go to the log file')
time.sleep(1)
logging.info('So should this')
time.sleep(1)
logging.warning('And this, too')
time.sleep(1)
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
time.sleep(1)
logging.critical('Bahut critical')

end_time = time.perf_counter()

print(end_time - start_time)
