from pathlib import Path
import traceback

from chat_thief.irc import send_twitch_msg
from chat_thief.audioworld.soundeffects_library import SoundeffectsLibrary
from chat_thief.models.play_soundeffect_request import PlaySoundeffectRequest
from chat_thief.models.command import Command


DEFAULT_WELCOME_FILE = Path(__file__).parent.parent.joinpath(".welcome")


class WelcomeCommittee:
    def __init__(self, welcome_file=DEFAULT_WELCOME_FILE):
        self.welcome_file = welcome_file

    def present_users(self):
        if self.welcome_file.is_file():
            return self.welcome_file.read_text().split()
        else:
            self.welcome_file.touch()
            return []

    def welcome_new_users(self, user):
        if user not in self.present_users():
            self._welcome(user)

            with open(self.welcome_file, "a") as f:
                f.write(f"{user}\n")

    def _welcome(self, user):
        sound_effect_files = SoundeffectsLibrary.find_soundeffect_files(user)

        if sound_effect_files:
            effect = sound_effect_files[0]
            command = Command(user)
            command.update_health(1)
            PlaySoundeffectRequest(user=user, command=user).save()
        else:
            send_twitch_msg(
                f"Welcome @{user}! You need a Theme song (max 5 secs): !soundeffect YOUTUBE-URL @{user} 00:03 00:07"
            )
