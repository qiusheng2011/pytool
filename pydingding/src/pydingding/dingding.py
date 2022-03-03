
from pydantic import BaseModel
from typing import List
import aiohttp


class BasicMessage(BaseModel):

    class At(BaseModel):
        atMobiles: List[str] = []
        atUserIds: List[str] = []
        isAtAll: bool = False

    msgtype: str = ""
    at: At = At()


class TextMessage(BasicMessage):
    """ 文本消息
    """
    class Text(BaseModel):
        content: str = ""

    text: Text = Text()
    msgtype: str = "text"


class LinkMessage(BasicMessage):
    """链接消息
    """
    class Link(BaseModel):
        text: str = ""
        title: str = ""
        picUrl: str = ""
        messageUrl: str = ""
    link: Link = Link()
    msgtype: str = "link"


class MarkdownMessage(BasicMessage):
    """Markdown 消息"""
    class Markdown(BaseModel):
        title: str = ""
        text: str = ""

    markdown: Markdown = Markdown()

    msgtype = "markdown"


class ActionCardMessage(BasicMessage):
    """ 整体跳转actionCard类型消息 """
    class ActionCard(BaseModel):
        title: str = ""
        text: str = ""
        singleTitle: str = ""
        singleUrl: str = ""
    msgtype = "actionCard"
    actionCard: ActionCard = ActionCard()


class MultiActionCardMessage(BasicMessage):
    """ 多跳转消息
    """
    class ActionCard(BaseModel):
        class Btns(BaseModel):
            title: str = ""
            acttionUrl: str = ""
        title: str = ""
        text: str = ""
        btnOrientation: str = "0"
        btns: List[Btns] = []
    msgtype = "actionCard"
    actionCard: ActionCard = ActionCard()


class DingDingGroupRobot(BaseModel):
    """ 钉钉群聊机器人 """
    baseurl: str = ""
    access_token: str = ""

    async def async_send_group_message(self, msgobj: BasicMessage):

        async with aiohttp.ClientSession() as session:

            async with session.post(f"{self.baseurl}/robot/send", params={"access_token": self.access_token}, json=msgobj.dict()) as response:
                text = await response.text()

                if response.status == 200:
                    data = await response.json()
                    if data["errcode"] == 0:
                        return True, "ok"
                    else:
                        return False, data["errmsg"]
                else:
                    return False, text