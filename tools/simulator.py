
import numpy as np

def simulate_flight(params):
    t = np.linspace(0, 1, 50)

    asymmetry = params["servo_right_mid"] - params["servo_left_mid"]
    roll = asymmetry * 0.05 * np.sin(10 * t)

    pitch = -params["flap_amplitude"] * 0.2 + np.random.randn(50)

    return {
        "roll": roll.tolist(),
        "pitch": pitch.tolist()
    }
