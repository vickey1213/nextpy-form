# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""Statistics components."""

from nextpy.backend.vars import Var
from nextpy.frontend.components.chakra import ChakraComponent
from nextpy.frontend.components.component import Component


class Stat(ChakraComponent):
    """The Stat component is used to display some statistics. It can take in a label, a number and a help text."""

    tag = "Stat"

    @classmethod
    def create(
        cls, *children, label=None, number=0, help_text=None, arrow_type=None, **props
    ) -> Component:
        """Create a stat component.

        Args:
            *children: The children of the component.
            label: A label for the stat component.
            number: The value of the stat component.
            help_text: A text added to the stat component.
            arrow_type: The type of the arrow ("increase", "decrease", None)
            **props: The properties of the component.

        Returns:
            The stat component.
        """
        if len(children) == 0:
            children = []
            if label:
                children.append(StatLabel.create(label))

            children.append(StatNumber.create(number))

            if help_text:
                if arrow_type:
                    children.append(
                        StatHelpText.create(
                            help_text, StatArrow.create(type_=arrow_type)
                        )
                    )
                else:
                    children.append(StatHelpText.create(help_text))

        return super().create(*children, **props)


class StatLabel(ChakraComponent):
    """A stat label component."""

    tag = "StatLabel"


class StatNumber(ChakraComponent):
    """The stat to display."""

    tag = "StatNumber"


class StatHelpText(ChakraComponent):
    """A helper text to display under the stat."""

    tag = "StatHelpText"


class StatArrow(ChakraComponent):
    """A stat arrow component indicating the direction of change."""

    tag = "StatArrow"

    # The type of arrow, either increase or decrease.
    type_: Var[str]


class StatGroup(ChakraComponent):
    """A stat group component to evenly space out the stats."""

    tag = "StatGroup"
