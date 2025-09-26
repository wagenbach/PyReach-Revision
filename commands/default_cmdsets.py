"""
Command sets

All commands in the game must be grouped in a cmdset.  A given command
can be part of any number of cmdsets and cmdsets can be added/removed
and merged onto entities at runtime.

To create new commands to populate the cmdset, see
`commands/command.py`.

This module wraps the default command sets of Evennia; overloads them
to add/remove commands from the default lineup. You can create your
own cmdsets by inheriting from them or directly from `evennia.CmdSet`.

"""

from evennia import default_cmds

# from mux_compatibility import TinyMuxCmdSet
# from mux_extra_commands import TinyMuxExtendedCmdSet
from .dice_commands import CmdRoll
from .experience import CmdExperience
from .conditions import CmdCondition
from .tilts import CmdTilt
from .CmdSheet import CmdSheet
from .stats import CmdStat, CmdRecalc
from .aspirations import CmdAspiration
from .social import CmdSocial
from .investigation import CmdInvestigation
from .combat import CmdCombat, CmdEquippedGear, CmdCombatHelp
from .integrity import CmdIntegrity
from .equipment import CmdEquipment
from .groups import CmdGroups, CmdRoster
from .npc import CmdNPC
from commands.diesiraecode.CmdPool import CmdPool
from commands.diesiraecode.CmdSpend import CmdSpend
from commands.diesiraecode.CmdGain import CmdGain  
from .CmdHealth import CmdHealth
from .template_admin import CmdTemplate
from .admin_commands import CmdMigrate
from .building import (CmdAreaManage, CmdRoomSetup, CmdPlaces, CmdRoomInfo, CmdMap)
from .admin_area_init import CmdInitAreaManager
from .mystery_admin import CmdMysteryAdmin, CmdClueObject
from .storyteller_admin import CmdStoryteller, CmdStorytellerWho
from .jobs.jobs_commands import CmdJobs
from commands.diesiraecode.CmdAlias import CmdAlias
from commands.diesiraecode.CmdAlts import CmdAlts
from commands.diesiraecode.CmdEmit import CmdEmit
from commands.diesiraecode.CmdPose import CmdPose
from commands.diesiraecode.CmdLanguage import CmdLanguage
from commands.diesiraecode.CmdSay import CmdSay
from commands.diesiraecode.CmdShortDesc import CmdShortDesc
from commands.diesiraecode.CmdStaff import CmdStaff
from commands.diesiraecode.CmdTableTalk import CmdTableTalk
from commands.diesiraecode.CmdTxt import CmdText
from commands.diesiraecode.CmdWatch import CmdWatch
from commands.diesiraecode.CmdWeather import CmdWeather
from commands.diesiraecode.CmdWho import CmdWho, CmdCensus
from .lookup import CmdLookup
from .voting import CmdVote, CmdRecommend, CmdVoteAdmin
from .test_xp_integration import CmdTestXP

# Uncomment the line below to use custom help command with forced 80-character width
# from .help_custom import CmdHelp

class CharacterCmdSet(default_cmds.CharacterCmdSet):
    """
    The `CharacterCmdSet` contains general in-game commands like `look`,
    `get`, etc available on in-game Character objects. It is merged with
    the `AccountCmdSet` when an Account puppets a Character.
    """

    key = "DefaultCharacter"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super().at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #
        # Core commands
        self.add(CmdRoll())
        self.add(CmdExperience())
        self.add(CmdCondition())
        self.add(CmdTilt())
        self.add(CmdJobs())
        # Sheet management and stat views
        self.add(CmdSheet())
        self.add(CmdPool())
        self.add(CmdSpend())
        self.add(CmdGain())
        self.add(CmdHealth())
        
        # Character management
        self.add(CmdStat())
        self.add(CmdRecalc())
        self.add(CmdAspiration())
        self.add(CmdIntegrity())
        self.add(CmdEquipment())
        self.add(CmdAlias())
        self.add(CmdAlts())
        self.add(CmdEmit())
        self.add(CmdPose())
        self.add(CmdLanguage())
        self.add(CmdSay())
        self.add(CmdShortDesc())
        self.add(CmdStaff())
        self.add(CmdTableTalk())
        self.add(CmdText())
        self.add(CmdWatch())
        self.add(CmdWeather())
        self.add(CmdWho())
        self.add(CmdCensus())
        self.add(CmdLookup())
        
        # Voting and recommendations
        self.add(CmdVote())
        self.add(CmdRecommend())
        self.add(CmdVoteAdmin())
        
        # Testing (remove after verification)
        self.add(CmdTestXP())
        
        # Social and investigation
        self.add(CmdSocial())
        self.add(CmdInvestigation())
        self.add(CmdGroups())
        self.add(CmdRoster())

        # Combat
        self.add(CmdCombat())
        self.add(CmdEquippedGear())
        self.add(CmdCombatHelp())
        
        # NPCs
        self.add(CmdNPC())
        
        # Admin commands
        self.add(CmdMigrate())
        self.add(CmdTemplate())
        self.add(CmdInitAreaManager())
        self.add(CmdMysteryAdmin())
        self.add(CmdClueObject())
        self.add(CmdStoryteller())
        self.add(CmdStorytellerWho())
        
        # Building commands (areas, rooms, places, mapping)
        self.add(CmdAreaManage())
        self.add(CmdRoomSetup())
        self.add(CmdRoomInfo())
        self.add(CmdPlaces())
        self.add(CmdMap())
        
        # Uncomment the line below to use custom help command with forced width
        # self.add(CmdHelp())

        # TinyMUX commands
        # self.add(TinyMuxCmdSet())
        # self.add(TinyMuxExtendedCmdSet())

class AccountCmdSet(default_cmds.AccountCmdSet):
    """
    This is the cmdset available to the Account at all times. It is
    combined with the `CharacterCmdSet` when the Account puppets a
    Character. It holds game-account-specific commands, channel
    commands, etc.
    """

    key = "DefaultAccount"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super().at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #


class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    """
    Command set available to the Session before being logged in.  This
    holds commands like creating a new account, logging in, etc.
    """

    key = "DefaultUnloggedin"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super().at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #


class SessionCmdSet(default_cmds.SessionCmdSet):
    """
    This cmdset is made available on Session level once logged in. It
    is empty by default.
    """

    key = "DefaultSession"

    def at_cmdset_creation(self):
        """
        This is the only method defined in a cmdset, called during
        its creation. It should populate the set with command instances.

        As and example we just add the empty base `Command` object.
        It prints some info.
        """
        super().at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #
