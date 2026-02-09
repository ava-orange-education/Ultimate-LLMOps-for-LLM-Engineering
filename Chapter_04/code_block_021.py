@dataclass
class ChainResult:
   intent: str
   rag_context: str
   final_response: str
   latency_ms: Dict[str, float]
   errors: list