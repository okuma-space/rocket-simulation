from datetime import datetime, timedelta
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

from dynamics import vertical_dynamics
from dynamics.vertical_dynamics import Trajectory


def save_altitude_history_plots(
    mass: float,
    initial_velocity: np.ndarray,
    epoch_time: datetime,
    time_step: timedelta,
    propagation_time: timedelta,
    output_dir: str | Path,
    file_stem: str = "rocket_trajectory",
) -> Trajectory:
    output_dir = Path(output_dir)

    html_dir = output_dir / "html"
    png_dir = output_dir / "png"

    html_dir.mkdir(parents=True, exist_ok=True)
    png_dir.mkdir(parents=True, exist_ok=True)

    trajectory = vertical_dynamics.propagate(
        mass=mass,
        initial_velocity=initial_velocity,
        epoch_time=epoch_time,
        time_step=time_step,
        propagation_time=propagation_time,
    )

    elapsed_seconds = np.array(
        [(t - trajectory.time[0]).total_seconds() for t in trajectory.time],
        dtype=float,
    )

    altitude = trajectory.position[:, 2]
    vertical_velocity = trajectory.velocity[:, 2]

    # PNG保存: matplotlib
    fig = plt.figure(figsize=(8, 6))
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()

    line1 = ax1.plot(
        elapsed_seconds,
        altitude,
        linestyle="-",
        label="Altitude",
    )[0]

    line2 = ax2.plot(
        elapsed_seconds,
        vertical_velocity,
        linestyle="--",
        label="Vertical Velocity",
    )[0]

    ax1.set_xlabel("Time [s]")
    ax1.set_ylabel("Altitude [m]")
    ax2.set_ylabel("Vertical Velocity [m/s]")
    ax1.set_title("Altitude / Vertical Velocity vs Time")
    ax1.grid(True)

    lines = [line1, line2]
    labels = [line.get_label() for line in lines]
    ax1.legend(lines, labels, loc="best")

    fig.tight_layout()
    fig.savefig(png_dir / f"{file_stem}_altitude_history.png", dpi=150)
    plt.close(fig)

    # HTML保存: plotly
    fig_html = go.Figure()

    fig_html.add_trace(
        go.Scatter(
            x=elapsed_seconds,
            y=altitude,
            mode="lines",
            name="Altitude",
            yaxis="y1",
            line=dict(dash="solid"),
        )
    )

    fig_html.add_trace(
        go.Scatter(
            x=elapsed_seconds,
            y=vertical_velocity,
            mode="lines",
            name="Vertical Velocity",
            yaxis="y2",
            line=dict(dash="dash"),
        )
    )

    fig_html.update_layout(
        title="Altitude / Vertical Velocity vs Time",
        xaxis_title="Time [s]",
        yaxis=dict(title="Altitude [m]"),
        yaxis2=dict(
            title="Vertical Velocity [m/s]",
            overlaying="y",
            side="right",
        ),
    )

    fig_html.write_html(str(html_dir / f"{file_stem}_altitude_history.html"))

    return trajectory


def main() -> None:
    output_dir = Path("docs")

    save_altitude_history_plots(
        mass=100.0,
        initial_velocity=np.array([0.0, 0.0, 100.0], dtype=float),
        epoch_time=datetime.now(),
        time_step=timedelta(seconds=1.0),
        propagation_time=timedelta(seconds=30.0),
        output_dir=output_dir,
        file_stem="rocket",
    )


if __name__ == "__main__":
    main()
