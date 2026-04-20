from datetime import datetime, timedelta
from dataclasses import dataclass
import numpy as np


@dataclass
class Trajectory:
    time: np.ndarray
    position: np.ndarray
    velocity: np.ndarray


def propagate(
    mass: float,
    initial_velocity: np.ndarray,
    epoch_time: datetime,
    time_step: timedelta,
    propagation_time: timedelta,
) -> Trajectory:

    # balloon state historyの初期化
    # trajectory
    time_list = [epoch_time]
    position_vector_list = [np.array([0.0, 0.0, 0.0], dtype=float)]
    velocity_vector_list = [initial_velocity.copy()]

    # propagatorの初期化
    current_time = epoch_time
    end_time = epoch_time + propagation_time
    time_step_seconds = time_step.total_seconds()  # タイムステップを秒に変換

    # propagationループ
    while current_time < end_time:
        # 簡易的なオイラー法での位置と速度の伝搬
        velocity = velocity_vector_list[-1]
        position = position_vector_list[-1] + velocity * time_step_seconds

        # 時刻を保存
        current_time += time_step

        # 更新されたtrajectoryを保存
        time_list.append(current_time)
        position_vector_list.append(position)
        velocity_vector_list.append(velocity)

    # Trajectoryオブジェクトを作成して返す
    return Trajectory(
        time=np.array(time_list, dtype=object),
        position=np.array(position_vector_list, dtype=float),
        velocity=np.array(velocity_vector_list, dtype=float),
    )
