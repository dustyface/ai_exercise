""" Test prompt """
import json
import logging
import zhihu.prompt.mobile_assistant.prompt_context as prompt_context

logger = logging.getLogger(__name__)


def test_simple_conversation():
    """ Test prompt """
    rsp = prompt_context.simple_conversation()
    result = rsp.choices[0].message.content
    result_json = json.loads(result)
    logger.info("result_json=%s", result_json)
