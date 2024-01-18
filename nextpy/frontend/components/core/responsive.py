# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""Responsive components."""

from nextpy.frontend.components.chakra.layout.box import Box


# Add responsive styles shortcuts.
def mobile_only(*children, **props):
    """Create a component that is only visible on mobile.

    Args:
        *children: The children to pass to the component.
        **props: The props to pass to the component.

    Returns:
        The component.
    """
    return Box.create(*children, **props, display=["block", "none", "none", "none"])


def tablet_only(*children, **props):
    """Create a component that is only visible on tablet.

    Args:
        *children: The children to pass to the component.
        **props: The props to pass to the component.

    Returns:
        The component.
    """
    return Box.create(*children, **props, display=["none", "block", "block", "none"])


def desktop_only(*children, **props):
    """Create a component that is only visible on desktop.

    Args:
        *children: The children to pass to the component.
        **props: The props to pass to the component.

    Returns:
        The component.
    """
    return Box.create(*children, **props, display=["none", "none", "none", "block"])


def tablet_and_desktop(*children, **props):
    """Create a component that is only visible on tablet and desktop.

    Args:
        *children: The children to pass to the component.
        **props: The props to pass to the component.

    Returns:
        The component.
    """
    return Box.create(*children, **props, display=["none", "block", "block", "block"])


def mobile_and_tablet(*children, **props):
    """Create a component that is only visible on mobile and tablet.

    Args:
        *children: The children to pass to the component.
        **props: The props to pass to the component.

    Returns:
        The component.
    """
    return Box.create(*children, **props, display=["block", "block", "block", "none"])
