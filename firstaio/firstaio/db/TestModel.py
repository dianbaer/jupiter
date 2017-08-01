import time
import uuid

import logging

from firstaio.db.Model import TestModelC

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    test = TestModelC(id=uuid.uuid4().hex, admin=False, create_at=time.time, content='xxxxxx', count=1)
    print(test)
