# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""Component for displaying a plotly graph."""

from typing import Any, Dict, List

from nextpy.backend.vars import Var
from nextpy.frontend.components.component import NoSSRComponent

try:
    from plotly.graph_objects import Figure
except ImportError:
    Figure = Any  # type: ignore


class PlotlyLib(NoSSRComponent):
    """A component that wraps a plotly lib."""

    library = "react-plotly.js@2.6.0"

    lib_dependencies: List[str] = ["plotly.js@2.22.0"]


class Plotly(PlotlyLib):
    """Display a plotly graph."""

    tag = "Plot"

    is_default = True

    # The figure to display. This can be a plotly figure or a plotly data json.
    data: Var[Figure]

    # The layout of the graph.
    layout: Var[Dict]

    # The width of the graph.
    width: Var[str]

    # The height of the graph.
    height: Var[str]

    # If true, the graph will resize when the window is resized.
    use_resize_handler: Var[bool]
