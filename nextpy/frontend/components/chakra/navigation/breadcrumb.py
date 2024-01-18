# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""Breadcrumb components."""

from nextpy.backend.vars import Var
from nextpy.frontend.components.chakra import ChakraComponent
from nextpy.frontend.components.chakra.navigation.link import Link
from nextpy.frontend.components.component import Component
from nextpy.frontend.components.core.foreach import Foreach


class Breadcrumb(ChakraComponent):
    """The parent container for breadcrumbs."""

    tag = "Breadcrumb"

    # The visual separator between each breadcrumb item
    separator: Var[str]

    # The left and right margin applied to the separator
    separator_margin: Var[str]

    @classmethod
    def create(cls, *children, items=None, **props) -> Component:
        """Create a breadcrumb component.

        If the kw-args `items` is provided and is a list, they will be added as children.

        Args:
            *children: The children of the component.
            items (list): The items of the breadcrumb: (label, link)
            **props: The properties of the component.

        Returns:
            The breadcrumb component.
        """
        if len(children) == 0:
            if isinstance(items, Var):
                children = [
                    Foreach.create(
                        items,
                        lambda item: BreadcrumbItem.create(label=item[0], href=item[1]),
                    ),
                ]

            else:
                children = []
                for label, link in items or []:
                    children.append(BreadcrumbItem.create(label=label, href=link))
        return super().create(*children, **props)


class BreadcrumbItem(ChakraComponent):
    """Individual breadcrumb element containing a link and a divider."""

    tag = "BreadcrumbItem"

    # Is the current page of the breadcrumb.
    is_current_page: Var[bool]

    # Is the last child of the breadcrumb.
    is_last_child: Var[bool]

    # The visual separator between each breadcrumb item
    separator: Var[str]

    # The left and right margin applied to the separator
    spacing: Var[str]

    @classmethod
    def create(cls, *children, label=None, href=None, **props):
        """Create a Breadcrumb Item component.

        Args:
            *children: The children of the component.
            label: The label used in the link. Defaults to None.
            href: The URL of the link. Defaults to None.
            **props: The properties of the component.

        Returns:
            The BreadcrumbItem component
        """
        if len(children) == 0:
            children = [BreadcrumbLink.create(label or "", href=href or "")]  # type: ignore
        return super().create(*children, **props)


class BreadcrumbSeparator(ChakraComponent):
    """The visual separator between each breadcrumb."""

    tag = "BreadcrumbSeparator"


class BreadcrumbLink(Link):
    """The breadcrumb link."""

    tag = "BreadcrumbLink"

    # Is the current page of the breadcrumb.
    is_current_page: Var[bool]
