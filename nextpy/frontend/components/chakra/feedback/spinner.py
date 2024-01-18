# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""Container to stack elements with spacing."""

from nextpy.backend.vars import Var
from nextpy.frontend.components.chakra import ChakraComponent, LiteralSpinnerSize


class Spinner(ChakraComponent):
    """The component that spins."""

    tag = "Spinner"

    # The color of the empty area in the spinner
    empty_color: Var[str]

    # For accessibility, it is important to add a fallback loading text. This text will be visible to screen readers.
    label: Var[str]

    # The speed of the spinner must be as a string and in seconds '1s'. Default is '0.45s'.
    speed: Var[str]

    # The thickness of the spinner.
    thickness: Var[int]

    # "xs" | "sm" | "md" | "lg" | "xl"
    size: Var[LiteralSpinnerSize]
