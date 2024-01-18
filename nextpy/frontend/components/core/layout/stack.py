# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""Stack components."""
from __future__ import annotations

from typing import Literal, Optional

from nextpy.frontend.components.component import Component
from nextpy.frontend.components.el.elements.typography import Div

LiteralJustify = Literal["start", "center", "end"]
LiteralAlign = Literal["start", "center", "end", "stretch"]


class Stack(Div):
    """A stack component."""

    @classmethod
    def create(
        cls,
        *children,
        justify: Optional[LiteralJustify] = "start",
        align: Optional[LiteralAlign] = "center",
        spacing: Optional[str] = "0.5rem",
        **props,
    ) -> Component:
        """Create a new instance of the component.

        Args:
            *children: The children of the stack.
            justify: The justify of the stack elements.
            align: The alignment of the stack elements.
            spacing: The spacing between each stack item.
            **props: The properties of the stack.

        Returns:
            The stack component.
        """
        style = props.setdefault("style", {})
        style.update(
            {
                "display": "flex",
                "alignItems": align,
                "justifyContent": justify,
                "gap": spacing,
            }
        )
        return super().create(*children, **props)


class VStack(Stack):
    """A vertical stack component."""

    def _apply_theme(self, theme: Component | None):
        self.style.update({"flex_direction": "column"})


class HStack(Stack):
    """A horizontal stack component."""

    def _apply_theme(self, theme: Component | None):
        self.style.update({"flex_direction": "row"})


hstack = HStack.create
vstack = VStack.create
