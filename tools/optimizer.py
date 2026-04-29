
def optimize_params(analysis, params, case):
    new_params = params.copy()
    suggestion = ""

    if analysis["problem"] == "严重翻滚":
        diff = params["servo_right_mid"] - params["servo_left_mid"]
        new_params["servo_right_mid"] -= diff * 0.5
        suggestion = "检测到左右不对称，已自动修正舵机中位值"

    elif analysis["problem"] == "持续俯冲":
        new_params["flap_amplitude"] -= 5
        new_params["pid_p"] *= 0.9
        suggestion = "降低扑翼幅度并减小P参数以减少俯冲"

    else:
        suggestion = "状态稳定，无需调整"

    if case:
        new_params.update(case["good_params"])
        suggestion += "（参考历史最优参数）"

    return new_params, suggestion
