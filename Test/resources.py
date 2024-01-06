import json
import requests

from robot.api import logger
from robot.api.deco import keyword


@keyword
def check_realtime_data_received_for_id(facility_id:int):
    call = f"realtime/{facility_id}"
    response = _get(call)
    # Check that expected code is returned
    if response.status_code == 200:
        logger.info(response.text)
        result = json.loads(response.text)[0]
        # Confirm that correct facility id is returned
        assert result["facilityId"] == facility_id

@keyword
def check_error_message_received_for_nonexisting_id(facility_id, msg):
    call = f"realtime/{facility_id}"
    response = _get(call)
    logger.info(response.text)
    logger.info(msg)
    # Confirm that the expected message is returned by the api
    assert response.text == msg

@keyword
def get_saved_data(facility_id):
    call = f"saved/{facility_id}"
    response = _get(call)
    assert response.status_code == 200

def _get(call):
    return requests.get(f"http://127.0.0.1:8000/{call}")
