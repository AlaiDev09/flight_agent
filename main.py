
from agent import FlightAgent
from tools.simulator import simulate_flight

# 初始参数（故意设成不稳定）
params = {
    "servo_left_mid": 1500,
    "servo_right_mid": 1700,
    "flap_amplitude": 30,
    "pid_p": 1.2,
    "pid_d": 0.3
}

agent = FlightAgent()

for step in range(5):
    print(f"\n===== 第 {step+1} 次飞行 =====")

    flight_data = simulate_flight(params)

    result = agent.run(flight_data, params)

    print("诊断:", result["diagnosis"])
    print("建议:", result["suggestion"])

    params.update(result["new_params"])

    print("新参数:", params)
