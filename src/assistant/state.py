import operator
from dataclasses import dataclass, field
from typing_extensions import TypedDict, Annotated

@dataclass(kw_only=True)
class SummaryState:
    research_topic: str | None = field(default=None)
    search_query: str | None = field(default=None)
    web_research_results: Annotated[list, operator.add] = field(default_factory=list)
    sources_gathered: Annotated[list, operator.add] = field(default_factory=list)
    research_loop_count: int = field(default=0)
    running_summary: str | None = field(default=None)

class SummaryStateInput(TypedDict):
    research_topic: str | None  # Use NotRequired[str] if using typing_extensions > 3.10

class SummaryStateOutput(TypedDict):
    running_summary: str | None