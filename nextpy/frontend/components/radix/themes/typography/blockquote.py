# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""Components for rendering heading.

https://www.radix-ui.com/themes/docs/theme/typography
"""
from __future__ import annotations

from nextpy import el
from nextpy.backend.vars import Var

from ..base import (
    CommonMarginProps,
    LiteralAccentColor,
    RadixThemesComponent,
)
from .base import (
    LiteralTextSize,
    LiteralTextWeight,
)


class Blockquote(el.Blockquote, CommonMarginProps, RadixThemesComponent):
    """A block level extended quotation."""

    tag = "Blockquote"

    # Text size: "1" - "9"
    size: Var[LiteralTextSize]

    # Thickness of text: "light" | "regular" | "medium" | "bold"
    weight: Var[LiteralTextWeight]

    # Overrides the accent color inherited from the Theme.
    color: Var[LiteralAccentColor]

    # Whether to render the text with higher contrast color
    high_contrast: Var[bool]
