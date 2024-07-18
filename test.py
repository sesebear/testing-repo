import time
import logging
import sys
import os
from os import listdir
from os.path import isfile, join

def getEnvVar(envVarName: str) -> str:
    result = os.environ[envVarName]
    if not result:
        logging.error(f"Missing environment variable: {envVarName}")
        sys.exit(1)
    return result

logging.basicConfig(level=logging.INFO)

logging.info("Script Start")
logging.info("Part One: Looping/Sleeping/Logging")

sleepPeriod: int = int(getEnvVar("SLEEP_PERIOD"))
sleepLoop: int = int(getEnvVar("SLEEP_LOOP"))
logging.info("using the settings: SLEEP_PERIOD=%s, SLEEP_LOOP=%s", sleepPeriod, sleepLoop)

for i in range(sleepLoop):
    logging.info("%s of %s: sleeping for %s seconds", i, sleepLoop, sleepPeriod)
    time.sleep(sleepPeriod)
    logging.info("waking")


logging.info("Part 2: Enumerate Files")
filepath = getEnvVar("STORAGE_FILESHARE_PATH")
logging.info("using the file path: %s", filepath)
files = [f for f in listdir(filepath) if isfile(join(filepath, f))]
for file in files:
    logging.info(file)

logging.info("Script End")