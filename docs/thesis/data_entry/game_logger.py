"""game_logger.py — drop-in CSV logger for the FRA skiing game (Layer 3).

Writes the two run-time log files in exactly the format that
stage3_import.py and the Stage-3 entry template expect:

    logs/sessions.csv       one row per session (written at session end)
    logs/state_changes.csv  one row per L2 difficulty adjustment

Usage inside the game:

    from game_logger import GameLogger

    log = GameLogger(participant_id="3001", session_no=1)   # at Assessment

    # whenever the adaptive layer (L2) changes difficulty:
    log.state_change(play_time_s=300, old_mult=0.60, new_mult=0.70,
                     reason="success rate 86% > 80% -> step up")

    # once, when the round/session ends:
    log.session_end(duration_min=8.5, distance_m=1240, coins=42,
                    obstacles_hit=1, lives_lost=0, avg_balance_pct=78.2,
                    max_speed=6.1, ai_diffmult=0.70, reached_gameover=False,
                    post_fra_index=59.0, notes="")

Appends only — never overwrites. Files and headers are created on first use.
Only stdlib; no dependencies. Records exactly what happened; derives nothing.
"""
import csv
import datetime
import os

SESSION_HEADERS = ["Participant_ID", "Session_No", "Session_Date", "Duration_Min",
                   "Distance_m", "Coins", "Obstacles_Hit", "Lives_Lost",
                   "Avg_Balance_pct", "Max_Speed", "AI_DiffMult",
                   "Reached_GameOver", "Post_FRA_Index", "Notes"]
STATE_HEADERS = ["Participant_ID", "Session_No", "Play_Time_s",
                 "Old_DiffMult", "New_DiffMult", "Reason"]


class GameLogger:
    def __init__(self, participant_id, session_no, log_dir="logs",
                 session_date=None):
        self.pid = str(participant_id)
        self.session_no = int(session_no)
        self.date = session_date or datetime.date.today().isoformat()
        self.dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        self._sessions = os.path.join(log_dir, "sessions.csv")
        self._states = os.path.join(log_dir, "state_changes.csv")
        self._session_written = False

    def _append(self, path, headers, row):
        new = not os.path.exists(path) or os.path.getsize(path) == 0
        with open(path, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new:
                w.writerow(headers)
            w.writerow(row)

    def state_change(self, play_time_s, old_mult, new_mult, reason=""):
        """Call every time Layer 2 adjusts the difficulty multiplier."""
        self._append(self._states, STATE_HEADERS, [
            self.pid, self.session_no, int(play_time_s),
            round(float(old_mult), 2), round(float(new_mult), 2), reason])

    def session_end(self, duration_min, distance_m, coins, obstacles_hit,
                    lives_lost, avg_balance_pct, max_speed, ai_diffmult,
                    reached_gameover, post_fra_index="", notes=""):
        """Call once when the session ends (any exit path, including Game Over)."""
        if self._session_written:
            raise RuntimeError("session_end() already called for this session")
        self._append(self._sessions, SESSION_HEADERS, [
            self.pid, self.session_no, self.date,
            round(float(duration_min), 2), int(distance_m), int(coins),
            int(obstacles_hit), int(lives_lost),
            round(float(avg_balance_pct), 1), round(float(max_speed), 1),
            round(float(ai_diffmult), 2),
            "TRUE" if reached_gameover else "FALSE",
            post_fra_index if post_fra_index != "" else "",
            notes])
        self._session_written = True


if __name__ == "__main__":
    # smoke test: writes sample rows to ./logs_smoketest and prints them
    log = GameLogger("SAMPLE-DELETE-ME", 1, log_dir="logs_smoketest")
    log.state_change(300, 0.60, 0.70, "success rate 86% > 80% -> step up")
    log.session_end(8.5, 1240, 42, 1, 0, 78.2, 6.1, 0.70, False, 59.0)
    for f in ("sessions.csv", "state_changes.csv"):
        print(f"--- logs_smoketest/{f}")
        print(open(os.path.join("logs_smoketest", f)).read())
