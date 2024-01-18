# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""List components."""

from __future__ import annotations

from nextpy.backend.vars import Var
from nextpy.frontend.components.chakra import ChakraComponent
from nextpy.frontend.components.component import Component
from nextpy.frontend.components.core.foreach import Foreach


class List(ChakraComponent):
    """Display a list of items."""

    tag = "List"

    # The space between each list item
    spacing: Var[str]

    # Shorthand prop for listStylePosition
    style_position: Var[str]

    # Shorthand prop for listStyleType
    style_type: Var[str]

    @classmethod
    def create(
        cls, *children, items: list | Var[list] | None = None, **props
    ) -> Component:
        """Create a list component.

        Args:
            *children: The children of the component.
            items: A list of items to add to the list.
            **props: The properties of the component.

        Returns:
            The list component.
        """
        if len(children) == 0:
            if isinstance(items, Var):
                children = [Foreach.create(items, ListItem.create)]
            else:
                children = [ListItem.create(item) for item in items or []]
        return super().create(*children, **props)


class ListItem(ChakraComponent):
    """A single list item."""

    tag = "ListItem"


class OrderedList(List):
    """An ordered list component with numbers."""

    tag = "OrderedList"


class UnorderedList(List):
    """An unordered list component with bullets."""

    tag = "UnorderedList"
