# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""An icon button component."""

from typing import Optional

from nextpy.backend.vars import Var
from nextpy.frontend.components.chakra.typography.text import Text
from nextpy.frontend.components.component import Component


class IconButton(Text):
    """A button with an icon."""

    tag = "IconButton"

    # The type of button.
    type: Var[str]

    #  A label that describes the button
    aria_label: Var[str]

    # The icon to be used in the button.
    icon: Optional[Component]

    # If true, the button will be styled in its active state.
    is_active: Var[bool]

    # If true, the button will be disabled.
    is_disabled: Var[bool]

    # If true, the button will show a spinner.
    is_loading: Var[bool]

    # If true, the button will be perfectly round. Else, it'll be slightly round
    is_round: Var[bool]

    # Replace the spinner component when isLoading is set to true
    spinner: Var[str]
