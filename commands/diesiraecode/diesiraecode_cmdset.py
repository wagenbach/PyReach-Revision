"""
Dies Irae Code Command Set

This cmdset includes all Dies Irae-specific custom commands.
"""

from evennia import CmdSet

from commands.diesiraecode.CmdAlias import CmdAlias
from commands.diesiraecode.CmdAlts import CmdAlts
from commands.diesiraecode.CmdEmit import CmdEmit
from commands.diesiraecode.CmdGain import CmdGain
from commands.diesiraecode.CmdLanguage import CmdLanguage
from commands.diesiraecode.CmdPage import CmdPage
from commands.diesiraecode.CmdPool import CmdPool
from commands.diesiraecode.CmdPose import CmdPose
from commands.diesiraecode.CmdSay import CmdSay
from commands.diesiraecode.CmdShortDesc import CmdShortDesc
from commands.diesiraecode.CmdSpend import CmdSpend
from commands.diesiraecode.CmdStaff import CmdStaff
from commands.diesiraecode.CmdTableTalk import CmdTableTalk
from commands.diesiraecode.CmdTxt import CmdText
from commands.diesiraecode.CmdWatch import CmdWatch
from commands.diesiraecode.CmdWeather import CmdWeather
from commands.diesiraecode.CmdWho import CmdWho, CmdCensus


class DiesIraeCmdSet(CmdSet):
    """
    This cmdset includes all Dies Irae custom commands.
    """
    key = "DiesIrae"
    priority = 1

    def at_cmdset_creation(self):
        """
        Populates the cmdset with all Dies Irae commands.
        """
        # Character and roleplay commands
        self.add(CmdAlias())
        self.add(CmdAlts())
        self.add(CmdEmit())
        self.add(CmdPose())
        self.add(CmdSay())
        self.add(CmdShortDesc())
        self.add(CmdTableTalk())
        
        # Communication commands
        self.add(CmdPage())
        self.add(CmdText())
        
        # Information and social commands
        self.add(CmdStaff())
        self.add(CmdWatch())
        self.add(CmdWeather())
        self.add(CmdWho())
        self.add(CmdCensus())
        
        # Game mechanics commands
        self.add(CmdPool())
        self.add(CmdSpend())
        self.add(CmdGain())
        self.add(CmdLanguage())

