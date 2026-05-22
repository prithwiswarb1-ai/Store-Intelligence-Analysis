import uuid


class VisitorTracker:

    def __init__(self):
        self.active_visitors = {}

    def assign_visitor(self, track_id):

        if track_id not in self.active_visitors:
            self.active_visitors[track_id] = f"VIS_{uuid.uuid4().hex[:6]}"

        return self.active_visitors[track_id]