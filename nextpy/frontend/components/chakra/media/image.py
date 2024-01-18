# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""An image component."""
from __future__ import annotations

from typing import Any, Optional, Union

from nextpy.backend.vars import Var
from nextpy.frontend.components.chakra import ChakraComponent, LiteralImageLoading
from nextpy.frontend.components.component import Component


class Image(ChakraComponent):
    """Display an image."""

    tag = "Image"
    alias = "ChakraImage"
    # How to align the image within its bounds. It maps to css `object-position` property.
    align: Var[str]

    # Fallback Nextpy component to show if image is loading or image fails.
    fallback: Optional[Component] = None

    # Fallback image src to show if image is loading or image fails.
    fallback_src: Var[str]

    # How the image to fit within its bounds. It maps to css `object-fit` property.
    fit: Var[str]

    # The native HTML height attribute to the passed to the img.
    html_height: Var[str]

    # The native HTML width attribute to the passed to the img.
    html_width: Var[str]

    # If true, opt out of the fallbackSrc logic and use as img.
    ignore_fallback: Var[bool]

    # "eager" | "lazy"
    loading: Var[LiteralImageLoading]

    # The path/url to the image or PIL image object.
    src: Var[Any]

    # The alt text of the image.
    alt: Var[str]

    # Provide multiple sources for an image, allowing the browser
    # to select the most appropriate source based on factors like
    # screen resolution and device capabilities.
    # Learn more _[here](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)_
    src_set: Var[str]

    def get_event_triggers(self) -> dict[str, Union[Var, Any]]:
        """Get the event triggers for the component.

        Returns:
            The event triggers.
        """
        return {
            **super().get_event_triggers(),
            "on_error": lambda: [],
            "on_load": lambda: [],
        }

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create an Image component.

        Args:
            *children: The children of the image.
            **props: The props of the image.

        Returns:
            The Image component.
        """
        src = props.get("src", None)
        if src is not None and not isinstance(src, (Var)):
            props["src"] = Var.create(value=src, _var_is_string=True)
        return super().create(*children, **props)
