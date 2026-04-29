
from tools.analyzer import analyze_flight
from tools.optimizer import optimize_params
import json
import os

class FlightAgent:
    def __init__(self):
        self.memory = self.load_memory()

    def load_memory(self):
        path = os.path.join("memory", "cases.json")
        try:
            with open(path, "r") as f:
                return json.load(f)
        except:
            return []

    def run(self, flight_data, params):
        analysis = analyze_flight(flight_data)
        similar_case = self.retrieve_case(analysis)

        new_params, suggestion = optimize_params(
            analysis, params, similar_case
        )

        return {
            "diagnosis": analysis["problem"],
            "suggestion": suggestion,
            "new_params": new_params
        }

    def retrieve_case(self, analysis):
        for case in self.memory:
            if case["problem"] == analysis["problem"]:
                return case
        return None
