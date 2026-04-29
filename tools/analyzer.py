
import numpy as np

def analyze_flight(data):
    roll = np.array(data["roll"])
    pitch = np.array(data["pitch"])

    roll_rate = np.max(np.abs(np.diff(roll)))
    pitch_trend = np.mean(pitch)

    if roll_rate > 15:
        problem = "严重翻滚"
    elif pitch_trend < -10:
        problem = "持续俯冲"
    else:
        problem = "基本稳定"

    return {
        "problem": problem,
        "roll_rate": float(roll_rate),
        "pitch_trend": float(pitch_trend)
    }
