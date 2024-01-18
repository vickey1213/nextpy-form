# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""React-Player component."""

from __future__ import annotations

from nextpy.backend.vars import Var
from nextpy.frontend.components.component import NoSSRComponent


class ReactPlayer(NoSSRComponent):
    """Using react-player and not implement all props and callback yet.
    reference: https://github.com/cookpete/react-player.
    """

    library = "react-player@2.12.0"

    tag = "ReactPlayer"

    is_default = True

    # The url of a video or song to play
    url: Var[str]

    # Set to true or false to pause or play the media
    playing: Var[bool]

    # Set to true or false to loop the media
    loop: Var[bool]

    # Set to true or false to display native player controls.
    controls: Var[bool] = True  # type: ignore

    # Set to true to show just the video thumbnail, which loads the full player on click
    light: Var[bool]

    # Set the volume of the player, between 0 and 1
    volume: Var[float]

    # Mutes the player
    muted: Var[bool]

    # Set the width of the player: ex:640px
    width: Var[str]

    # Set the height of the player: ex:640px
    height: Var[str]
