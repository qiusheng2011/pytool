
from unittest import TestCase
from pydingding.src.pydingding.dingding import DingDingGroupRobot, TextMessage, LinkMessage, MarkdownMessage, BasicMessage, ActionCardMessage, MultiActionCardMessage, DingRobotSecuritySetting
import asyncio

# https://oapi.dingtalk.com/robot/send?access_token=b14c5294ea99127014bf828c6a7528763539ee594b64fb34e43f30eb891f6898
class DingDingGroupRobotUnittest(TestCase):

    def setUp(self) -> None:
        self.baseurl = "https://oapi.dingtalk.com"
        self.access_token = "a6a968e78f9052a2284066589babd470d4d1eafd89d16fd9ff41622879c3cd31"
        self.group_robot = DingDingGroupRobot(baseurl=self.baseurl, access_token=self.access_token)
        
        self.access_token2 = "b14c5294ea99127014bf828c6a7528763539ee594b64fb34e43f30eb891f6898"
        self.group_robot = DingDingGroupRobot(baseurl=self.baseurl, access_token=self.access_token2, security_setting=DingRobotSecuritySetting.TIMESTAMPSIGN, secret='SEC5aac05ec3ffcb1f0f866e9c97538af54f7ff4a2bf7b823c66ae25478959f04ef')
        self.loop = asyncio.get_event_loop()
        return super().setUp()

    def test_textmsg(self):

        msg = TextMessage()
        msg.text.content = "TextMessage"
        msg.at.atMobiles = ["18513279524"]
        msg.at.isAtAll = False

        
        status, msg =  self.loop .run_until_complete(self.group_robot.async_send_group_message(msg))
        self.assertTrue(status, msg)

    def test_linkmsg(self):
        msg = LinkMessage()
        msg.link.title = "LinkMessage"
        msg.link.text = "LinkMessage"
        msg.link.picUrl= "https://s3.bmp.ovh/imgs/2022/02/ddf12e19b1e8ee60.png"
        msg.link.messageUrl = "https://www.aliyun.com"
        
        status, msg = self.loop .run_until_complete(self.group_robot.async_send_group_message(msg))
        self.assertTrue(status, msg)
    
    def test_markdown(self):
        msg = MarkdownMessage()
        msg.markdown.title = "MarkdownMessage"
        msg.markdown.text  = "# MarkdownMessage \n ## MarkdownMessage"
        
        status, msg = self.loop.run_until_complete(self.group_robot.async_send_group_message(msg))
        self.assertTrue(status, msg)
        
    def test_actioncard(self):
        
        msg = ActionCardMessage()
        msg.actionCard.title = "ActionCardMessage"
        msg.actionCard.text = "ActionCardMessage"
        msg.actionCard.singleTitle = "ActionCardMessage.singleTitle"
        msg.actionCard.singleUrl = "https://www.aliyun.com"
        
        status, msg = self.loop.run_until_complete(self.group_robot.async_send_group_message(msg))
        self.assertTrue(status, msg)
    
    def test_multiactioncard(self):
        msg = MultiActionCardMessage()
        msg.actionCard.title = "ActionCardMessage"
        msg.actionCard.text = "ActionCardMessage"
        msg.actionCard.btnOrientation = "1"
        msg.actionCard.btns.append(MultiActionCardMessage.ActionCard.Btns(title="title1",actionUrl="https://www.aliyun.com"))
        msg.actionCard.btns.append(MultiActionCardMessage.ActionCard.Btns(title="title2",actionUrl="https://www.aliyun.com"))
        
        status, msg = self.loop.run_until_complete(self.group_robot.async_send_group_message(msg))
        self.assertTrue(status, msg)
        
        
        msg = MultiActionCardMessage()
        msg.actionCard.title = "ActionCardMessage"
        msg.actionCard.text = "ActionCardMessage"
        msg.actionCard.btnOrientation = "0"
        msg.actionCard.btns.append(MultiActionCardMessage.ActionCard.Btns(title="title1",actionUrl="https://www.aliyun.com"))
        msg.actionCard.btns.append(MultiActionCardMessage.ActionCard.Btns(title="title2",actionUrl="https://www.aliyun.com"))
        
        status, msg = self.loop.run_until_complete(self.group_robot.async_send_group_message(msg))
        self.assertTrue(status, msg)