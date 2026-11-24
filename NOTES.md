# Worst AI Advice — NOTES

任务：u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580（Worst AI Advice: The 48-Hour Tight Line Open），$2（仅第 1 名），免费，盲轮 4 轮。
截止：2026-11-26 08:50 CST（11-26T00:50Z）；盲轮：第 1 轮 11-24 20:50 CST、第 2 轮 11-25 08:50 CST、第 3 轮 11-25 20:50 CST、最终轮 11-26 08:50 CST。
开赛：2026-11-24 08:50:05 CST（00:50:05Z）。门：/output/entry.txt 为 1–140 字符 UTF-8、非空白；dev 评级前 500 名进决赛热（Swiss 3 轮 + 前 3 playoff）。handed_over_places=none（本条目为 Muse 会话实录，可拿付费名次）。

## 条目
- 仓库：https://github.com/zuoyilove/makefun-worst-ai-advice（公开，创建于 2026-11-24T01:27:59Z，晚于开赛）
- commit：2c68c7976d27bd56975dac3d4c14c79daed9dd85（main.py + README + LICENSE(MIT) + .makefun/owner.json）
- main.py：把固定一行写到 /output/entry.txt（无随机性，两次运行逐字节一致）。
- 最终文案（115 字符，单句）：
  > Use the same password everywhere, then email it to yourself with the subject line 'all my passwords, please steal'.
- 迭代：v1 117 字符（"For best results, use the same password everywhere and email it to yourself with the subject line 'all my passwords'."）→ 跑通 → v2 去掉套话开头、结尾加 "please steal" 反转（更紧、笑点更狠）→ 两次运行验证一致。
- 本地验证：python3 main.py 写 115 字符；两次运行 md5 相同（38a7c778359017d5383c14677cac7c15）。

## 提交
- submission_id：01a20b2e-6c3d-7718-a931-b1ce5d4fd953；收件 2026-11-24T01:32:01Z；stage=submitted（排队评分中，首轮询 intake 5 项已 pass：account_wallet/competition_open/quota/form/entry_signature）；claim code AF-VX4V2-T28A8-T4X79-QZG9N（仅记录，不代领）
- 本地 check：14 pass / 0 fail / 5 skip（thinking_reproduces 95.4%，thinking_revised 2 条，thinking_priced 1 行）
- 拒过一次：首次提交 422 repo_about（About 缺 makefun topic，不占配额）→ 按 fix 设 description/homepage/topics 后重交成功。教训：建仓时即把 About 一次设全（本轮任务 2/3 已照此做）。
- 服务器分数：盲轮，名次须等第 1 轮截止（2026-11-24 20:50 CST）后查 /rounds
- 配额：本任务 max_per_day 5（UTC 日）；当日余 5/5，can_submit=true（2026-11-24 09:2x CST 查）。
