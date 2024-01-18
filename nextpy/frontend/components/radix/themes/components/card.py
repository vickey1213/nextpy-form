# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""Interactive components provided by @radix-ui/themes."""
from typing import Literal

from nextpy import el
from nextpy.backend.vars import Var

from ..base import (
    CommonMarginProps,
    RadixThemesComponent,
)


class Card(el.Div, CommonMarginProps, RadixThemesComponent):
    """Trigger an action or event, such as submitting a form or displaying a dialog."""

    tag = "Card"

    # Change the default rendered element for the one passed as a child, merging their props and behavior.
    as_child: Var[bool]

    # Button size "1" - "5"
    size: Var[Literal["1", "2", "3", "4", "5"]]

    # Variant of button: "solid" | "soft" | "outline" | "ghost"
    variant: Var[Literal["surface", "classic", "ghost"]]
