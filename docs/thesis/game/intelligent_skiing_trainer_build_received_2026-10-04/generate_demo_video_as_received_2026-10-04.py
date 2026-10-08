#!/usr/bin/env python3
"""
Generate an animated MP4 demo video for the Skiing Rehabilitation Training Game.
The skier moves down the slope, dodges obstacles, and collisions trigger stage transitions.
"""

import os, math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio

W, H = 1280, 720
FPS = 24
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "skiing_game_demo.mp4")

# Colors
WHITE = (255, 255, 255)
LIGHT_BLUE = (144, 202, 249)
GREEN = (76, 175, 80)
DARK_GREEN = (46, 125, 50)
DARKER_GREEN = (27, 94, 32)
RED = (229, 57, 53)
ORANGE = (255, 152, 0)
GOLD = (255, 215, 0)
GRAY = (170, 170, 170)
SNOW = (240, 245, 255)
SKY_TOP = (135, 206, 235)
SKY_BOT = (200, 230, 250)
BROWN = (93, 64, 55)
ROCK_GRAY = (117, 117, 117)
HELMET_BLUE = (21, 101, 192)

def get_font(size, bold=False):
    paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except:
                continue
    return ImageFont.load_default()

font_hud = get_font(16, True)
font_hud_sm = get_font(14)
font_banner = get_font(32, True)
font_banner_sub = get_font(20)
font_title = get_font(44, True)
font_subtitle = get_font(24)
font_stage = get_font(60, True)
font_small = get_font(18)
font_body = get_font(20)
font_heading = get_font(28, True)
font_big = get_font(48, True)

# ─── 3D-to-2D projection helpers ───
# Simple perspective: objects at z=0 are at horizon, z=1 is closest
HORIZON_Y = 300       # y pixel of vanishing point
GROUND_BOTTOM = 700   # y pixel of bottom of slope
VP_X = 640            # vanishing point x

def project(world_x, world_z):
    """Project 3D world coords to 2D screen. z: 0=far, 1=near player."""
    z = max(world_z, 0.01)
    scale = z ** 0.8  # perspective scale
    screen_y = HORIZON_Y + (GROUND_BOTTOM - HORIZON_Y) * z
    screen_x = VP_X + world_x * scale * 500
    return int(screen_x), int(screen_y), scale

def draw_gradient_sky(draw):
    for y in range(HORIZON_Y + 40):
        t = y / (HORIZON_Y + 40)
        r = int(SKY_TOP[0] + (SKY_BOT[0] - SKY_TOP[0]) * t)
        g = int(SKY_TOP[1] + (SKY_BOT[1] - SKY_TOP[1]) * t)
        b = int(SKY_TOP[2] + (SKY_BOT[2] - SKY_TOP[2]) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

def draw_mountains(draw):
    peaks = [(100, 220), (250, 180), (420, 200), (580, 160), (740, 190),
             (900, 170), (1050, 195), (1180, 210)]
    for px, py in peaks:
        w = random.randint(80, 130)
        draw.polygon([(px - w, HORIZON_Y + 10), (px, py), (px + w, HORIZON_Y + 10)],
                     fill=(200, 210, 220))
        # snow cap
        draw.polygon([(px - 20, py + 30), (px, py), (px + 20, py + 30)], fill=WHITE)

def draw_slope(draw, scroll_offset=0):
    """Draw the snow slope with perspective lines."""
    # Main slope
    draw.polygon([(0, HORIZON_Y + 10), (W, HORIZON_Y + 10), (W, H), (0, H)], fill=SNOW)
    # Edge lines (converge to vanishing point)
    for i in range(2):
        left = VP_X - 80 - i * 300
        right = VP_X + 80 + i * 300
        t = (i + 1) * 0.35
        ly = HORIZON_Y + 10 + (GROUND_BOTTOM - HORIZON_Y) * t
        draw.line([(VP_X, HORIZON_Y + 10), (left, H)], fill=(220, 228, 238), width=2)
        draw.line([(VP_X, HORIZON_Y + 10), (right, H)], fill=(220, 228, 238), width=2)
    # Horizontal snow texture lines
    for i in range(8):
        z = 0.15 + i * 0.1
        y = int(HORIZON_Y + (GROUND_BOTTOM - HORIZON_Y) * z)
        half_w = int(150 + 600 * z)
        offset = int((scroll_offset * z * 80) % 60 - 30)
        draw.line([(VP_X - half_w, y + offset), (VP_X + half_w, y + offset)],
                  fill=(230, 238, 248), width=1)

def draw_tree_at(draw, sx, sy, scale):
    """Draw a pine tree at screen coords with given scale."""
    s = max(scale, 0.15)
    trunk_h = int(20 * s)
    trunk_w = max(int(4 * s), 2)
    # Trunk
    draw.rectangle([sx - trunk_w, sy - trunk_h, sx + trunk_w, sy], fill=BROWN)
    # Foliage layers
    for j, (h_off, w_off) in enumerate([(0, 18), (-14, 14), (-25, 10)]):
        th = int(h_off * s)
        tw = int(w_off * s)
        fh = int(12 * s)
        draw.polygon([(sx - tw, sy + th), (sx, sy + th - fh), (sx + tw, sy + th)],
                     fill=DARK_GREEN if j % 2 == 0 else DARKER_GREEN)
        # Snow on top
        sw = max(int(tw * 0.7), 2)
        sh = max(int(fh * 0.25), 2)
        draw.polygon([(sx - sw, sy + th - fh + sh + 2), (sx, sy + th - fh),
                       (sx + sw, sy + th - fh + sh + 2)], fill=(255, 255, 255, 200))

def draw_rock_at(draw, sx, sy, scale):
    s = max(scale, 0.15)
    rw = int(14 * s)
    rh = int(10 * s)
    draw.ellipse([sx - rw, sy - rh, sx + rw, sy + rh // 2], fill=ROCK_GRAY)
    draw.ellipse([sx - rw + 2, sy - rh + 2, sx + rw - 2, sy + rh // 2 - 3], fill=(145, 145, 145))

def draw_coin_at(draw, sx, sy, scale, frame=0):
    s = max(scale, 0.15)
    r = max(int(8 * s), 3)
    # Spin effect
    w = max(int(r * abs(math.cos(frame * 0.15))), 2)
    draw.ellipse([sx - w, sy - r, sx + w, sy + r], fill=GOLD)
    draw.ellipse([sx - w + 1, sy - r + 1, sx + w - 1, sy + r - 1], fill=(255, 235, 100))

def draw_skier(draw, px, py, tilt=0, flash_red=False):
    """Draw the skier character at screen position."""
    body_color = (255, 80, 80) if flash_red else RED
    # Skis
    draw.rectangle([px - 16, py + 2, px - 6, py + 5], fill=HELMET_BLUE)
    draw.rectangle([px + 6, py + 2, px + 16, py + 5], fill=HELMET_BLUE)
    # Poles
    draw.line([(px - 14, py - 25), (px - 22, py + 6)], fill=(60, 60, 60), width=2)
    draw.line([(px + 14, py - 25), (px + 22, py + 6)], fill=(60, 60, 60), width=2)
    # Body
    bx = int(tilt * 4)
    draw.rounded_rectangle([px - 10 + bx, py - 38, px + 10 + bx, py], radius=5, fill=body_color)
    # Head
    draw.ellipse([px - 8 + bx, py - 52, px + 8 + bx, py - 36], fill=(255, 204, 188))
    # Helmet
    draw.arc([px - 9 + bx, py - 54, px + 9 + bx, py - 42], 180, 360, fill=HELMET_BLUE, width=4)

def draw_hud(draw, lives, score, speed, dist, coins, trial_text, stage_info=None):
    hx, hy = W - 220, 15
    # HUD background
    draw.rounded_rectangle((hx, hy, W - 12, hy + 210), radius=10,
                           fill=(0, 0, 0, 140))
    # Trial
    draw.text((hx + 104, hy + 8), trial_text, fill=LIGHT_BLUE, font=font_hud_sm, anchor="mt")
    draw.line([(hx + 10, hy + 26), (W - 22, hy + 26)], fill=(255, 255, 255, 40))
    draw.text((hx + 10, hy + 32), "TRAINING STATUS", fill=GRAY, font=font_hud_sm)
    # Hearts
    hearts = "\u2764" * lives + "\u2661" * (3 - lives)
    draw.text((W - 22, hy + 54), hearts, fill=RED, font=font_hud, anchor="rt")
    draw.text((hx + 10, hy + 54), "Lives", fill=GRAY, font=font_hud_sm)
    # Stats
    rows = [("Score", str(score)), ("Speed", f"{speed} km/h"), ("Distance", f"{dist} m"), ("Coins", str(coins))]
    for i, (l, v) in enumerate(rows):
        yy = hy + 78 + i * 26
        draw.text((hx + 10, yy), l, fill=GRAY, font=font_hud_sm)
        draw.text((W - 22, yy), v, fill=WHITE, font=font_hud, anchor="rt")
    # Stage indicator
    if stage_info:
        draw.rounded_rectangle((hx, hy + 185, W - 12, hy + 208), radius=5, fill=stage_info[1])
        draw.text((hx + 104, hy + 196), stage_info[0], fill=WHITE, font=font_hud_sm, anchor="mm")

def draw_balance_bar(draw, value, color):
    bx, by = W // 2 - 140, H - 40
    draw.text((W // 2, by - 15), "Balance", fill=WHITE, font=font_hud_sm, anchor="mt")
    draw.rounded_rectangle((bx, by, bx + 280, by + 16), radius=8, fill=(0, 0, 0, 120))
    bar_w = max(int(280 * value / 100), 0)
    if bar_w > 0:
        c = GREEN if color == 'g' else (ORANGE if color == 'o' else RED)
        draw.rounded_rectangle((bx, by, bx + bar_w, by + 16), radius=8, fill=c)
    # center line
    draw.rectangle([bx + 138, by - 3, bx + 142, by + 19], fill=WHITE)

def draw_collision_flash(img, intensity=0.3):
    overlay = Image.new('RGBA', (W, H), (255, 50, 50, int(255 * intensity)))
    return Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')

def draw_banner(draw, text, subtitle, color, alpha=200):
    """Draw a centered stage banner."""
    by = H // 2 - 50
    draw.rounded_rectangle((80, by, W - 80, by + 100), radius=16,
                           fill=(0, 0, 0, alpha))
    # Color stripe on left
    draw.rounded_rectangle((80, by, 100, by + 100), radius=0, fill=color)
    draw.text((W // 2, by + 28), text, fill=WHITE, font=font_banner, anchor="mt")
    draw.text((W // 2, by + 64), subtitle, fill=LIGHT_BLUE, font=font_banner_sub, anchor="mt")


# ─── World objects ───
class WorldObject:
    def __init__(self, wx, wz, kind='tree'):
        self.wx = wx       # world x: -1 to 1
        self.wz = wz       # world z: distance ahead (decreases as player moves)
        self.kind = kind    # 'tree', 'rock', 'coin'
        self.alive = True
        self.collected = False

def generate_objects(count=40, coin_count=15, seed=42):
    random.seed(seed)
    objs = []
    for _ in range(count):
        wx = random.uniform(-0.8, 0.8)
        wz = random.uniform(0.5, 8.0)
        kind = 'tree' if random.random() < 0.6 else 'rock'
        objs.append(WorldObject(wx, wz, kind))
    for _ in range(coin_count):
        wx = random.uniform(-0.6, 0.6)
        wz = random.uniform(0.3, 7.0)
        objs.append(WorldObject(wx, wz, 'coin'))
    return objs


# ─── Animation timeline ───
def build_frames():
    frames = []
    total_frames = 0

    # === TITLE CARD (3s) ===
    for f in range(FPS * 3):
        img = Image.new('RGBA', (W, H))
        draw = ImageDraw.Draw(img)
        # Gradient bg
        for y in range(H):
            t = y / H
            r = int(26 + (13 - 26) * t)
            g = int(35 + (71 - 35) * t)
            b = int(126 + (161 - 126) * t)
            draw.line([(0, y), (W, y)], fill=(r, g, b))
        draw.text((W//2, 180), "Intelligent Skiing Rehabilitation", fill=WHITE, font=font_title, anchor="mt")
        draw.text((W//2, 235), "Training Game System", fill=WHITE, font=font_title, anchor="mt")
        draw.text((W//2, 310), "3-Stage Progressive Assist Demo", fill=LIGHT_BLUE, font=font_subtitle, anchor="mt")
        # Stage cards
        stages = [("Stage 1", "Normal", GREEN), ("Stage 2", "Speed -30%", ORANGE), ("Stage 3", "Clear Path", RED)]
        for i, (s, d, c) in enumerate(stages):
            bx = 200 + i * 320
            draw.rounded_rectangle((bx, 400, bx + 250, 520), radius=14, fill=(255, 255, 255, 18))
            draw.ellipse([bx + 100, 415, bx + 150, 465], fill=c)
            draw.text((bx + 125, 440), str(i+1), fill=WHITE, font=font_heading, anchor="mm")
            draw.text((bx + 125, 480), s, fill=WHITE, font=font_body, anchor="mt")
            draw.text((bx + 125, 504), d, fill=GRAY, font=font_small, anchor="mt")
        frames.append(np.array(img.convert('RGB')))

    # === GAMEPLAY ANIMATION ===
    # Simulation state
    player_x = 0.0       # -1 to 1
    player_target_x = 0.0
    scroll_z = 0.0       # how far we've traveled
    scroll_speed = 0.04   # initial speed (world units per frame)
    lives = 3
    hits = 0
    score_val = 0
    dist_val = 0
    coins_val = 0
    balance = 85
    flash_timer = 0
    stage = 1
    banner_timer = 0
    banner_text = ""
    banner_sub = ""
    banner_color = GREEN
    speed_kmh = 45

    # Pre-planned player path (frame, target_x) for dodging
    # Player weaves through obstacles, hitting specific ones at planned times
    path_events = [
        # (frame_offset, target_x) - relative to gameplay start
        (0, 0.0), (20, -0.15), (50, 0.2), (80, -0.1), (110, 0.3),
        (140, -0.25), (170, 0.1), (200, -0.3), (220, 0.15),
        # Hit obstacle 1 around frame 240
        (235, 0.0), (240, 0.0),  # move to center where a tree is
        # After hit, continue dodging
        (260, -0.2), (290, 0.25), (320, -0.15), (350, 0.1),
        (380, -0.35), (400, 0.2), (430, -0.1), (460, 0.3),
        # Hit obstacle 2 around frame 480
        (475, 0.15), (480, 0.15),
        # After hit, wider path with fewer obstacles
        (500, -0.1), (530, 0.1), (560, -0.2), (590, 0.15),
        (620, 0.0), (650, -0.1), (680, 0.2),
        # Hit obstacle 3 around frame 700 -> game over
        (695, 0.0), (700, 0.0),
    ]
    path_idx = 0

    # Generate world objects with specific ones placed for planned collisions
    objects = []
    random.seed(42)

    # Collision obstacle 1: at z offset ~240*0.04=9.6 from start, x=0
    # Collision obstacle 2: at z offset ~480*0.04=19.2, x=0.15
    # Collision obstacle 3: at z offset ~700*0.04=28.0, x=0

    # Spawn waves of obstacles
    for wave in range(12):
        base_z = 2.0 + wave * 3.0
        n_obs = 5 if wave < 8 else 3  # fewer in later waves (after stage 3)
        for i in range(n_obs):
            wx = random.uniform(-0.7, 0.7)
            wz = base_z + random.uniform(0, 2.5)
            kind = 'tree' if random.random() < 0.55 else 'rock'
            objects.append(WorldObject(wx, wz, kind))
        # Coins
        for i in range(3):
            wx = random.uniform(-0.5, 0.5)
            wz = base_z + random.uniform(0, 2.0)
            objects.append(WorldObject(wx, wz, 'coin'))

    # Place specific collision obstacles
    hit1_z = 9.6
    hit2_z = 19.2
    hit3_z = 28.0
    objects.append(WorldObject(0.0, hit1_z, 'tree'))
    objects.append(WorldObject(0.15, hit2_z, 'rock'))
    objects.append(WorldObject(0.0, hit3_z, 'tree'))

    # Show Stage 1 banner first
    banner_timer = FPS * 2
    banner_text = "STAGE 1: Normal Play"
    banner_sub = "3 Lives  |  Full Speed  |  Standard Obstacles"
    banner_color = GREEN

    gameplay_frames = FPS * 32  # 32 seconds of gameplay
    coin_collect_flash = 0

    for f in range(gameplay_frames):
        img = Image.new('RGBA', (W, H))
        draw = ImageDraw.Draw(img)

        # Update path
        while path_idx < len(path_events) - 1 and f >= path_events[path_idx + 1][0]:
            path_idx += 1
        if path_idx < len(path_events) - 1:
            f0, x0 = path_events[path_idx]
            f1, x1 = path_events[path_idx + 1]
            t = min(1.0, (f - f0) / max(f1 - f0, 1))
            t = t * t * (3 - 2 * t)  # smoothstep
            player_target_x = x0 + (x1 - x0) * t

        player_x += (player_target_x - player_x) * 0.12
        tilt = (player_target_x - player_x) * 30

        scroll_z += scroll_speed
        dist_val = int(scroll_z * 15)
        score_val = int(dist_val * 0.7 + coins_val * 10)

        if flash_timer > 0:
            flash_timer -= 1
        if coin_collect_flash > 0:
            coin_collect_flash -= 1
        if banner_timer > 0:
            banner_timer -= 1

        # Balance simulation
        if abs(tilt) > 2:
            balance -= 0.15
        else:
            balance += 0.05
        balance = max(15, min(95, balance))

        # Draw scene
        draw_gradient_sky(draw)
        random.seed(7)  # consistent mountains
        draw_mountains(draw)
        draw_slope(draw, scroll_z)

        # Sort objects by z for back-to-front rendering
        visible = [o for o in objects if o.alive and 0.05 < (o.wz - scroll_z) < 5.0]
        visible.sort(key=lambda o: o.wz - scroll_z, reverse=True)

        for obj in visible:
            rel_z = obj.wz - scroll_z
            z_norm = 1.0 - rel_z / 5.0  # 0=far, 1=near
            if z_norm < 0.02 or z_norm > 1.0:
                continue
            sx, sy, sc = project(obj.wx, z_norm)
            if obj.kind == 'tree':
                draw_tree_at(draw, sx, sy, sc)
            elif obj.kind == 'rock':
                draw_rock_at(draw, sx, sy, sc)
            elif obj.kind == 'coin' and not obj.collected:
                draw_coin_at(draw, sx, sy, sc, f)

        # Check collisions
        for obj in objects:
            if not obj.alive:
                continue
            rel_z = obj.wz - scroll_z
            if 0.0 < rel_z < 0.25 and abs(obj.wx - player_x) < 0.12:
                if obj.kind == 'coin' and not obj.collected:
                    obj.collected = True
                    obj.alive = False
                    coins_val += 1
                    coin_collect_flash = 8
                    balance = min(95, balance + 3)
                elif obj.kind in ('tree', 'rock') and flash_timer <= 0:
                    obj.alive = False
                    hits += 1
                    lives -= 1
                    flash_timer = FPS  # 1 second flash
                    balance = max(balance, 55)

                    if hits == 1:
                        # Stage 2
                        stage = 2
                        scroll_speed = 0.028  # 30% slower
                        speed_kmh = 30
                        banner_timer = FPS * 3
                        banner_text = "STAGE 2: Speed Reduced"
                        banner_sub = "1st Hit!  Speed -30%  |  Easier to dodge"
                        banner_color = ORANGE
                    elif hits == 2:
                        # Stage 3 - remove some obstacles ahead
                        stage = 3
                        speed_kmh = 30
                        banner_timer = FPS * 3
                        banner_text = "STAGE 3: Path Cleared"
                        banner_sub = "2nd Hit!  60% obstacles removed ahead"
                        banner_color = RED
                        # Remove obstacles ahead
                        for o2 in objects:
                            if o2.alive and o2.kind != 'coin' and o2.wz > scroll_z + 0.5:
                                if random.random() < 0.6:
                                    o2.alive = False
                    elif hits >= 3:
                        # Game over - will break after adding some frames
                        pass

        # Draw skier
        skier_sx, skier_sy, _ = project(player_x, 0.85)
        is_flash = flash_timer > 0 and (flash_timer // 3) % 2 == 0
        draw_skier(draw, skier_sx, skier_sy - 10, tilt, flash_red=is_flash)

        # Coin collect sparkle
        if coin_collect_flash > 0:
            for _ in range(4):
                sx2 = skier_sx + random.randint(-20, 20)
                sy2 = skier_sy - random.randint(10, 40)
                r2 = random.randint(2, 5)
                draw.ellipse([sx2 - r2, sy2 - r2, sx2 + r2, sy2 + r2], fill=GOLD)

        # HUD
        bal_color = 'g' if balance > 60 else ('o' if balance > 30 else 'r')
        stage_info = None
        if stage == 1:
            stage_info = ("Stage 1: Normal", GREEN)
        elif stage == 2:
            stage_info = ("Stage 2: Slow", ORANGE)
        elif stage == 3:
            stage_info = ("Stage 3: Clear", RED)
        draw_hud(draw, lives, score_val, speed_kmh, dist_val, coins_val,
                 "Trial 1 / 5", stage_info)
        draw_balance_bar(draw, int(balance), bal_color)

        # Banner overlay
        if banner_timer > 0:
            alpha = min(200, banner_timer * 15)
            draw_banner(draw, banner_text, banner_sub, banner_color, alpha)

        # Convert and apply collision flash
        frame_rgb = img.convert('RGB')
        if flash_timer > FPS * 0.7:  # first 0.3s of flash
            intensity = 0.25 * ((flash_timer - FPS * 0.7) / (FPS * 0.3))
            frame_rgb = draw_collision_flash(frame_rgb, intensity)

        frames.append(np.array(frame_rgb))

        # Stop after 3rd hit + a few frames
        if hits >= 3 and flash_timer <= FPS - 10:
            break

    # === GAME OVER SCREEN (3s) ===
    for f in range(FPS * 3):
        img = Image.new('RGB', (W, H), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        cx = W // 2
        draw.rounded_rectangle((cx - 260, 60, cx + 260, 660), radius=20, fill=(30, 30, 40))
        draw.text((cx, 100), "Training Complete", fill=WHITE, font=font_big, anchor="mt")
        stats = [("Score", str(score_val)), ("Distance", f"{dist_val} m"),
                 ("Coins Collected", str(coins_val)), ("Obstacles Hit", "3 / 3"),
                 ("Avg Balance", f"{int(balance)}%"), ("Max Speed", "45 km/h")]
        for i, (l, v) in enumerate(stats):
            sy = 180 + i * 42
            draw.text((cx - 200, sy), l, fill=GRAY, font=font_body)
            draw.text((cx + 200, sy), v, fill=WHITE, font=font_hud, anchor="rt")
            draw.line([(cx - 200, sy + 34), (cx + 200, sy + 34)], fill=(60, 60, 70))
        # AI advice box
        draw.rounded_rectangle((cx - 220, 440, cx + 220, 570), radius=10, fill=(30, 60, 30))
        draw.text((cx - 200, 452), "AI Training Recommendation", fill=GREEN, font=font_hud)
        advice = [
            "3 collisions. Focus on scanning ahead",
            "and planning your path. The progressive",
            "assist system helped extend your session.",
            "Practice 3 sessions/week for improvement."
        ]
        for i, line in enumerate(advice):
            draw.text((cx - 200, 478 + i * 22), line, fill=WHITE, font=font_small)
        # Button
        draw.rounded_rectangle((cx - 100, 590, cx + 100, 630), radius=10, fill=(33, 150, 243))
        draw.text((cx, 610), "Next Trial (2/5)", fill=WHITE, font=font_small, anchor="mm")
        frames.append(np.array(img))

    # === REPORT SCREEN (4s) ===
    for f in range(FPS * 4):
        img = Image.new('RGB', (W, H))
        draw = ImageDraw.Draw(img)
        for y in range(H):
            t = y / H
            draw.line([(0, y), (W, y)], fill=(int(13 + 10*t), int(27 + 10*t), int(42 + 50*t)))
        draw.text((W//2, 25), "Training Session Report", fill=WHITE, font=font_heading, anchor="mt")
        draw.text((W//2, 58), "5-Trial Rehabilitation Training Summary", fill=LIGHT_BLUE, font=font_small, anchor="mt")
        # Summary cards
        cards = [("1630", "Total Score"), ("1980m", "Distance"), ("86", "Coins"),
                 ("71%", "Avg Balance"), ("450", "Best Score")]
        for i, (v, l) in enumerate(cards):
            bx2 = 50 + i * 245
            draw.rounded_rectangle((bx2, 85, bx2 + 220, 155), radius=10, fill=(40, 50, 70))
            draw.text((bx2 + 110, 104), v, fill=WHITE, font=font_heading, anchor="mt")
            draw.text((bx2 + 110, 136), l, fill=LIGHT_BLUE, font=font_hud_sm, anchor="mt")
        # Table header
        draw.text((50, 170), "Trial-by-Trial Results", fill=LIGHT_BLUE, font=font_body)
        cols = [70, 190, 320, 430, 530, 640, 760, 880]
        hdrs = ["Trial", "Score", "Dist", "Coins", "Hits", "Balance", "Speed", "Result"]
        draw.rounded_rectangle((50, 198, W - 50, 224), radius=4, fill=(40, 55, 80))
        for j, h2 in enumerate(hdrs):
            draw.text((cols[j], 202), h2, fill=LIGHT_BLUE, font=font_hud_sm)
        rows = [("1", "340", "420m", "16", "2/3", "72%", "45", "3 Hits"),
                ("2", "180", "250m", "10", "3/3", "52%", "48", "3 Hits"),
                ("3", "280", "350m", "15", "2/3", "60%", "52", "3 Hits"),
                ("4", "380", "440m", "20", "2/3", "67%", "55", "3 Hits"),
                ("5\u2605", "450", "520m", "25", "1/3", "75%", "58", "3 Hits")]
        for i, row in enumerate(rows):
            ry = 230 + i * 25
            sc_color = GREEN if i == 4 else (RED if i == 1 else WHITE)
            for j, v in enumerate(row):
                c2 = sc_color if j == 1 else WHITE
                draw.text((cols[j], ry), v, fill=c2, font=font_hud_sm)
        # Trends
        draw.text((50, 370), "Performance Trends", fill=LIGHT_BLUE, font=font_body)
        tcols = [70, 230, 380, 520, 670]
        draw.rounded_rectangle((50, 395, W - 50, 418), radius=4, fill=(40, 55, 80))
        for j, h3 in enumerate(["Metric", "Trial 1", "Trial 5", "Change", "Trend"]):
            draw.text((tcols[j], 398), h3, fill=LIGHT_BLUE, font=font_hud_sm)
        tdata = [("Score", "340", "450", "+110", "Improving", GREEN),
                 ("Distance", "420m", "520m", "+100m", "Improving", GREEN),
                 ("Balance", "72%", "75%", "+3%", "Stable", ORANGE),
                 ("Avoidance", "1/3", "2/3", "+1", "Improving", GREEN)]
        for i, (m, t1, t5, ch, tr, tc) in enumerate(tdata):
            ry2 = 424 + i * 24
            draw.text((tcols[0], ry2), m, fill=WHITE, font=font_hud_sm)
            draw.text((tcols[1], ry2), t1, fill=WHITE, font=font_hud_sm)
            draw.text((tcols[2], ry2), t5, fill=WHITE, font=font_hud_sm)
            draw.text((tcols[3], ry2), ch, fill=tc, font=font_hud_sm)
            draw.text((tcols[4], ry2), tr, fill=tc, font=font_hud_sm)
        # AI advice
        draw.rounded_rectangle((50, 530, W - 50, 680), radius=10, fill=(30, 60, 30))
        draw.text((70, 540), "AI Training Recommendations", fill=GREEN, font=font_hud)
        recs = ["\u2022 Good score improvement. Focus on maintaining steady balance.",
                "\u2022 Average balance of 71% is strong. Consider higher difficulty.",
                "\u2022 10 total collisions - try scanning further ahead on the slope.",
                "\u2022 Moderate consistency. Keep practicing for more uniform results.",
                "\u2022 General Fitness: Continue regular sessions for athletic capability."]
        for i, r in enumerate(recs):
            draw.text((70, 565 + i * 22), r, fill=WHITE, font=font_hud_sm)
        frames.append(np.array(img))

    # === END CARD (3s) ===
    for f in range(FPS * 3):
        img = Image.new('RGB', (W, H))
        draw = ImageDraw.Draw(img)
        for y in range(H):
            t = y / H
            draw.line([(0, y), (W, y)], fill=(int(26 - 13*t), int(35 + 36*t), int(126 + 35*t)))
        draw.text((W//2, 200), "Intelligent Skiing Rehabilitation", fill=WHITE, font=font_title, anchor="mm")
        draw.text((W//2, 260), "Training Game System", fill=WHITE, font=font_title, anchor="mm")
        draw.text((W//2, 330), "3-Stage Progressive Assist System", fill=LIGHT_BLUE, font=font_subtitle, anchor="mm")
        recap = [(GREEN, "Stage 1: Normal Play - Full speed, all obstacles"),
                 (ORANGE, "Stage 2: Speed Reduced 30% after 1st collision"),
                 (RED, "Stage 3: 60% obstacles cleared after 2nd collision")]
        for i, (c, txt) in enumerate(recap):
            yy = 410 + i * 44
            draw.ellipse([W//2 - 270, yy - 10, W//2 - 250, yy + 10], fill=c)
            draw.text((W//2 - 235, yy), txt, fill=WHITE, font=font_small, anchor="lm")
        draw.text((W//2, H - 60), "Balance Training  |  AI Recommendations  |  5-Trial Reports",
                  fill=GRAY, font=font_small, anchor="mm")
        frames.append(np.array(img))

    return frames


def main():
    print("Generating animated skiing game demo video...")
    frames = build_frames()
    print(f"Total frames: {len(frames)}, Duration: {len(frames)/FPS:.1f}s at {FPS} FPS")

    writer = imageio.get_writer(OUTPUT_PATH, fps=FPS, codec='libx264',
                                quality=8, pixelformat='yuv420p')
    for frame in frames:
        writer.append_data(frame)
    writer.close()

    size_kb = os.path.getsize(OUTPUT_PATH) / 1024
    print(f"Video saved to: {OUTPUT_PATH}")
    print(f"File size: {size_kb:.0f} KB ({size_kb/1024:.1f} MB)")

if __name__ == "__main__":
    main()
