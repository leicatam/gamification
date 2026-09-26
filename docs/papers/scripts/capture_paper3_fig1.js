const { chromium } = require('playwright-core');
(async () => {
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
    args: ['--no-sandbox']
  });
  const LEVELS = [
    [1, 0.40,  35,  5],
    [2, 0.65,  55,  7],
    [3, 0.90,  98,  9],
    [4, 1.15, 116, 10],
    [5, 1.40, 218, 12],
  ];
  for (const [lvl, diff, dist, playSec] of LEVELS) {
    const ctx = await browser.newContext({ viewport: { width: 1000, height: 1000 }, deviceScaleFactor: 3 });
    const page = await ctx.newPage();
    await page.goto('file:///home/user/gamification/docs/thesis/game/Alpine_Coordination_Game_Stage3_v2.2.html');
    await page.fill('#pid', 'FIG');
    await page.selectOption('#sessno', '1');
    await page.evaluate(() => { const g = document.getElementById('goal'); g.value = '400'; });
    await page.click('#startBtn');
    // freeze adaptation, force the staged difficulty
    await page.evaluate(d => { S.diff = d; S.lastEval = 1e9; }, diff);
    // let the run play so spawns reflect the difficulty
    await page.waitForFunction(t => S && S.playT >= t, playSec, { timeout: 60000 });
    // stage the display distance (as the original figure did), avoid hit-flash
    await page.evaluate(d => { S.dist = d; }, dist);
    await page.waitForFunction(() => S.playT > (S.flashUntil || 0));
    await page.waitForTimeout(120); // let HUD repaint
    const el = await page.$('#gameWrap');
    await el.screenshot({ path: `panel${lvl}.png` });
    const hud = await page.evaluate(() => [
      document.getElementById('hudL').textContent,
      document.getElementById('hudM').textContent,
      document.getElementById('hudR').textContent].join(' | '));
    console.log(`panel${lvl}: diff x${diff} | ${hud}`);
    await ctx.close();
  }
  await browser.close();
})();
