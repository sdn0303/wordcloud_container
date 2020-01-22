# -*- Coding: UTF-8 -*-
import uuid

import responder

from app.models.wordcloud import text_parser
from app.models.wordcloud import new_wordcloud_client
from app.utils.errors import InvalidKeyError
from app.utils.logger import Logger

# Settings
api = responder.API(cors=True, allowed_hosts=["*"])
LOGGER = Logger.get_logger(__file__)


@api.route("/api/v1/word")
class WordsResource(object):
    async def on_post(self, req, resp):
        @api.background.task
        def wordcloud_task(uid, words):
            text = text_parser(words)
            wcc = new_wordcloud_client(text)
            wcc.to_file(f"/app/storage/{uid}.png")

        uuid4 = str(uuid.uuid4())

        data = await req.media()
        if "text" not in data.keys():
            msg = "must to set 'text' in json key"
            resp.status_code = api.status_codes.HTTP_500
            resp.text = msg
            raise InvalidKeyError(msg)

        wordcloud_task(uuid4, data["text"])
        resp.media = {
            "uid": uuid4,
            "msg": "Start to analyze text."
        }


@api.route("/")
def hello(req, resp):
    """ Confirmation survival"""
    resp.text = "hello, this is test wordcloud api"


if __name__ == "__main__":
    api.run(address="0.0.0.0", port=8080, log_level="debug", debug=True)
