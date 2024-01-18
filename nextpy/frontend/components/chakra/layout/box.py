# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""A box component that can contain other components."""

from nextpy.backend.vars import Var
from nextpy.frontend.components.chakra import ChakraComponent
from nextpy.frontend.components.tags import Tag


class Box(ChakraComponent):
    """A generic container component that can contain other components."""

    tag = "Box"

    # The type element to render. You can specify an image, video, or any other HTML element such as iframe.
    element: Var[str]

    # The source of the content.
    src: Var[str]

    # The alt text of the content.
    alt: Var[str]

    def _render(self) -> Tag:
        return (
            super()
            ._render()
            .add_props(
                **{
                    "as": self.element,
                }
            )
        )
