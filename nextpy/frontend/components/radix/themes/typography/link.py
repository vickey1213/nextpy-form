# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""Components for rendering heading.

https://www.radix-ui.com/themes/docs/theme/typography
"""
from __future__ import annotations

from typing import Literal

from nextpy.backend.vars import Var
from nextpy.frontend.components.el.elements.inline import A

from ..base import (
    CommonMarginProps,
    LiteralAccentColor,
    RadixThemesComponent,
)
from .base import (
    LiteralTextSize,
    LiteralTextTrim,
    LiteralTextWeight,
)

LiteralLinkUnderline = Literal["auto", "hover", "always"]


class Link(CommonMarginProps, RadixThemesComponent, A):
    """A semantic element for navigation between pages."""

    tag = "Link"

    # Change the default rendered element for the one passed as a child, merging their props and behavior.
    as_child: Var[bool]

    # Text size: "1" - "9"
    size: Var[LiteralTextSize]

    # Thickness of text: "light" | "regular" | "medium" | "bold"
    weight: Var[LiteralTextWeight]

    # Removes the leading trim space: "normal" | "start" | "end" | "both"
    trim: Var[LiteralTextTrim]

    # Sets the visibility of the underline affordance: "auto" | "hover" | "always"
    underline: Var[LiteralLinkUnderline]

    # Overrides the accent color inherited from the Theme.
    color: Var[LiteralAccentColor]

    # Whether to render the text with higher contrast color
    high_contrast: Var[bool]
