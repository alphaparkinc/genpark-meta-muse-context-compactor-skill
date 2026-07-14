class MetaMuseContextCompactorClient:
    def compact(self, large_context: str) -> dict:
        return {"compacted_context": large_context[:200] + "... [Compacted]"}