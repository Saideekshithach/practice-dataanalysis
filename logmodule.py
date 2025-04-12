import logging
#og.basicConfig(level=logging.DEBUG)
'''logging.debug("Hello,Debug!")
logging.info("Hello,Info!")
logging.warning("Hello,warning!")
logging.error('Hello,Error!')
logging.critical('Hello,Critical!')'''

logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    filemode='a',
                    format='%(name)s-%(levelname)s-%(message)s')
logging.debug("Hello,Debug!")
logging.info("Hello,Info!")
logging.warning("Hello,warning!")
logging.error('Hello,Error!')
logging.critical('Hello,Critical!')


              
                